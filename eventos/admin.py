from django.contrib import admin
from .models import Eventos
from .models import Comentarios,RespostaComentarios,Notifications
# Register your models here.
admin.site.register(Eventos)
admin.site.register(Comentarios)
admin.site.register(RespostaComentarios)
admin.site.register(Notifications)