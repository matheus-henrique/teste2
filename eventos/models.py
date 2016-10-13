from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime


class Eventos(models.Model):
	nome = models.CharField(max_length=100)
	descricao = models.TextField()
	local = models.CharField(max_length=100)
	latitude = models.CharField(max_length=100, blank=True, null=True)
	longitude = models.CharField(max_length=100, blank=True, null=True)
	cidade = models.CharField(max_length=100)
	author = models.ForeignKey('auth.User')
	valor = models.CharField(max_length=5, blank=True, null=True)
	imagem = models.FileField(default='')
	hora = models.CharField(max_length=5)
	estilos = models.CharField(max_length=100)
	data = models.CharField(max_length=10)
	num_participantes = models.IntegerField(default=0)

	def __str__(self):
		return str(self.id)



class RespostaComentarios(models.Model):
	id_author = models.ForeignKey('auth.User')
	resposta = models.TextField()
	data = models.DateTimeField(default=datetime.now, blank=True)

class Comentarios(models.Model):
	id_author = models.ForeignKey('auth.User')
	comentario = models.TextField()
	data = datetime.now()
	evento = models.ForeignKey(Eventos,related_name='evt')
	resposta = models.ForeignKey(RespostaComentarios, null=True, blank=True)

class Notifications(models.Model):
	id_author = models.ForeignKey('auth.User')
	texto = models.TextField()
	img_link = models.TextField(default="http://pcswired.com/headsetperson35.png")
	lido = models.BooleanField(default=False)