from django.contrib import admin
from usuarios.models import Usuario,Ficha,Integrantes,Proyecto
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ficha)
admin.site.register(Integrantes)
admin.site.register(Proyecto)