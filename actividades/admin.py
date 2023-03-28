from django.contrib import admin
from actividades.models import Tipo_Llamado,Llamado
# Register your models here.

admin.site.register(Llamado)
admin.site.register(Tipo_Llamado)