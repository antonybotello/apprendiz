from django.contrib import admin
from usuarios.models import Usuario,Ficha,Usuarios_Ficha
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ficha)
admin.site.register(Usuarios_Ficha)