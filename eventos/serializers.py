from rest_framework import serializers
from .models import Eventos,Comentarios,RespostaComentarios,Notifications
from django.contrib.auth.models import User



class EventosSerializers(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(slug_field='username',read_only=True)
	class Meta:
		model = Eventos
		fields = ('id','nome','descricao','local','latitude','longitude','author','cidade','imagem','valor','hora','estilos','descricao','data','num_participantes')



class RespostaComentariosEventosSerializes(serializers.ModelSerializer):
	id_author = serializers.SlugRelatedField(slug_field='username',read_only=True)
	class Meta:
		model = RespostaComentarios
		fields = ('id_author','resposta','data')

class ComentarioEventosSerializers(serializers.ModelSerializer):
	evento = serializers.PrimaryKeyRelatedField(read_only=True)
	resposta = RespostaComentariosEventosSerializes(read_only=True)
	id_author = serializers.SlugRelatedField(slug_field='username',read_only=True)
	class Meta:
		model = Comentarios
		fields = ('id','comentario','id_author','data','evento','resposta',)

class NotificationsSerializers(serializers.ModelSerializer):
	class Meta:
		model = Notifications
		fields = ('id_author','texto','lido','img_link')




 