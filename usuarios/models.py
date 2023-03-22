from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Proveedor(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    apellido= models.CharField(max_length=45,verbose_name="Apellido")
    class TipoDocumento(models.TextChoices):
        CC='1',_("Cédula de Ciudadanía")
        TI='2',_("Tarjeta de Identidad")
        CE='3',_("Cédula de Extranjería")
    tipoDocumento= models.CharField(max_length=1,choices=TipoDocumento.choices, 
    verbose_name="Tipo de Documento")
    documento= models.CharField(max_length=45,verbose_name="Documento")
    def clean(self):
        self.nombre= self.nombre.title()
    def __str__(self):
        return "%s %s"%(self.nombre,self.apellido)
    
    class Meta:
        verbose_name_plural = "Proveedores"
        

    
    

