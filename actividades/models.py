from django.db import models
from usuarios.models import Usuario
class Tipo_Llamado(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    norma= models.CharField(max_length=45,verbose_name="Norma")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
     

# Create your models here.
class Llamado(models.Model):
    fecha_ingreso= models.DateField(auto_now=True, verbose_name="Fecha", help_text="MM/DD/AAAA")
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name="Usuario")
    tipo_llamado=models.ForeignKey(Tipo_Llamado, on_delete=models.CASCADE,verbose_name="Tipo de Llamado")
    descripcion=models.CharField(max_length=45,verbose_name="Descripción")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
     
