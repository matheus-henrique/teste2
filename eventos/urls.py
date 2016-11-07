from django.conf.urls import include, url
from eventos import views



urlpatterns = [
    url(r'^eventos/$', views.ListaDeEventos.as_view()),
    url(r'^eventos/(?P<pk>[0-9]+)/$', views.EventoDetalhado.as_view()),
    url(r'^eventos/cidade/(?P<cidade>[a-zA-Z ã,á,à,â,ê,í,ú,õ,é,ü-]+)/$', views.EventoCidade.as_view()),
    url(r'^eventos/comentarios/(?P<pk>[0-9]+)/$', views.EventoComentarios.as_view()),
    url(r'^eventos/comentarios/resposta/(?P<pk>[0-9]+)/$', views.RespostaEventosComentarios.as_view()),
    url(r'^eventos/comentarios/id/(?P<pk>[0-9]+)/$', views.EventoComentarioID.as_view()),
    url(r'^eventos/user/$', views.EventoUser.as_view()),
    url(r'^$',views.home),
    url(r'^evento/cadastrar/$', views.cadastrarEvento),
    url(r'^teste-login/', views.Teste.as_view()),
    url(r'^perfil/$',views.perfil),
    url(r'^evento/(?P<pk>[0-9]+)/$',views.mostrarEvento),
    url(r'^logout/$',views.deslogar),
    url(r'^eventos/cidades/(?P<cidade>[a-zA-Z ã,á,à,â,ê,í,ú,õ,é,ü]+)/$',views.mostrarEventoCidade),
    url(r'^registrar/$',views.registrar),
    url(r'^register/$',views.register),
    url(r'^notifications/(?P<pk>[0-9]+)/$',views.NotificationsView.as_view()),
    url(r'^evento/confirmarpresenca/(?P<pk>[0-9]+)/$',views.ConfirmarPresença.as_view()),
    url("^soc/", include("social.apps.django_app.urls", namespace="social"))
]