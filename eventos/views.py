from eventos.models import Eventos,Comentarios,RespostaComentarios,Notifications
from eventos.serializers import EventosSerializers,ComentarioEventosSerializers,RespostaComentariosEventosSerializes,NotificationsSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,parsers,renderers
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.http import HttpResponseRedirect
import datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from datetime import datetime
from django.core import serializers
from rest_framework.parsers import JSONParser,MultiPartParser,FileUploadParser,FormParser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponse


class Teste(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        login(request, user)
        return redirect('/perfil/')


obtain_auth_token = Teste.as_view()



def mostrarEventoCidade(request,cidade):
    print(cidade)
    return render(request,"telaeventos.html",{'cidade':cidade})

@login_required
def cadastrarEvento(request):
    return render(request,"cadastrarevento.html",{})


def registrar(request):
    return render(request,"registrar.html",{})

def register(request):
    user = User.objects.create_user(username=request.POST.get("username"),email='owna@owna.con',password=request.POST.get("password"))
    user.save()
    user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
    login(request,user)
    Notifications.objects.create(id_author=request.user,texto="Seja bem vindo")
    return HttpResponseRedirect("/")

@login_required
def perfil(request):
     return render(request,"perfil.html",{})

def deslogar(request):
    logout(request)
    return HttpResponseRedirect("/")

def mostrarEvento(request,pk):
    try:
        evento = Eventos.objects.get(id=pk)
        return render(request,"evento.html",{'evento':evento})
    except:
        return render(request,"index.html",{})



def home(request):
    return render(request,"home.html",{})


def logar(request):
    print(request.POST.get('user'))
    print(request.POST.get('pass'))



class NotificationsView(APIView):
    def get_queryset(self,pk):
        notifications = Notifications.objects.filter(id_author=pk)
        if notifications.count() > 0:
            return notifications
        return False

    def get(self,request,pk):
        notifications = self.get_queryset(pk)
        serializer = NotificationsSerializers(notifications, many=True)
        return Response(serializer.data)
    def put(self,request,pk):
        notifications = self.get_queryset(pk)
        for notification in notifications:
            notification.lido = True
            notification.save()
       
        serializer = NotificationsSerializers(notification,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(null)

class ConfirmarPresença(APIView):
    def get_queryset(self,pk):
        try:
            return Eventos.objects.get(id=pk)
        except Eventos.DoesNotExist:
            raise Http404
    def put(self,request,pk):
        eventos = self.get_queryset(pk)
        eventos.num_participantes += 1
        Notifications.objects.create(id_author=eventos.author,texto="<a href='#'>"+request.user.username+"</a> marcou <strong>presença</strong> no seu evento <a href='/evento/"+str(eventos.id)+"/'>"+eventos.nome+"</a>",img_link=eventos.imagem)
        serializer = EventosSerializers(eventos,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(Http404)


class ListaDeEventos(generics.ListCreateAPIView):
    serializer_class = EventosSerializers
    queryset = Eventos.objects.all()

    permission_classes = (IsOwnerOrReadOnly,)
    parser_classes = (FormParser,MultiPartParser,)


    def get(self,request):
        eventos = Eventos.objects.all()
        serializer = EventosSerializers(eventos, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = EventosSerializers(data = request.data)
        print(request.FILES['imagem'])
        print(request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    
class EventoComentarios(APIView):
    def get_queryset(self,pk):
        comentario = Comentarios.objects.filter(evento=pk)
        if comentario.count() > 0:
            return comentario
        return null
    def get(self,request,pk):
        comentario = self.get_queryset(pk)
        serializer = ComentarioEventosSerializers(comentario, many=True)
        return Response(serializer.data)

    def post(self,request,pk):
        request.data['id_author'] = request.user.id
        request.data['data'] = datetime.now()
        serializer = ComentarioEventosSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save(evento=Eventos.objects.get(id=pk),id_author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)



class RespostaEventosComentarios(APIView):
    permission_classes = (AllowAny,)
    def get(self,request,pk):
        resposta = RespostaComentarios.objects.all()
        serializer = RespostaComentariosEventosSerializes(resposta,many=True)
        return Response(serializer.data)
    def put(self,request,pk):
        comentario = Comentarios.objects.get(id=pk)
        serializer = ComentarioEventosSerializers(comentario,data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save(id_author = request.user.id, comentario=comentario.comentario, data=comentario.data, evento=comentario.evento,resposta=RespostaComentarios.objects.get(id=1))
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
 


class EventoComentarioID(APIView):
    def get_queryset(self,pk):
        try:
            return Comentarios.objects.get(id=pk)
        except Comentarios.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        comentario = self.get_queryset(pk)
        serializer = ComentarioEventosSerializers(comentario)
        return Response(serializer.data)


    def put(self, request,pk):
        comentario = self.get_queryset(pk)
        teste = RespostaComentarios.objects.create(id_author=request.user,resposta=request.data['resposta'],data=datetime.now())
        comentario.resposta = teste
        serializer = ComentarioEventosSerializers(comentario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class EventoDetalhado(generics.ListCreateAPIView):
    serializer_class = EventosSerializers
    permission_classes = (IsOwnerOrReadOnly,)

    def get_object(self,pk):
        try:
            return Eventos.objects.get(id=pk)
        except Eventos.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        evento = self.get_object(pk)
        serializer = EventosSerializers(evento)
        return Response(serializer.data)

    def put(self,request,pk):
        evento = self.get_object(pk)
        serializer = EventosSerializers(evento, data=request.data)
        if serializer.is_valid():
            request.data['id_author'] = request.user.id
            request.data['data'] = datetime.now()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        eventos = self.get_object(pk)
        eventos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class EventoCidade(APIView):
    def get_queryset(self,cidade):
        evento = Eventos.objects.filter(cidade=cidade)
        if evento.count() > 0:
            return evento
    def get(self,request,cidade):
        evento = self.get_queryset(cidade)
        serializer = EventosSerializers(evento, many=True)
        return Response(serializer.data)

class EventoUser(APIView):
    def get_queryset(self,author):
        evento = Eventos.objects.filter(author=author)
        if evento.count() > 0:
            return evento
        return null

    def get(self,request):
        evento = self.get_queryset(request.user)
        serializer = EventosSerializers(evento, many=True)
        return Response(serializer.data)