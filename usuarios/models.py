from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Usuario(models.Model):
    primer_nombre= models.CharField(max_length=45,verbose_name="Primer Nombre")
    segundo_nombre= models.CharField(max_length=45,verbose_name="Segundo Nombre")
    
    primer_apellido= models.CharField(max_length=45,verbose_name="Primer Apellido")
    segundo_apellido= models.CharField(max_length=45,verbose_name="Segundo Apellido")
    
    fecha_nacimiento= models.DateField(verbose_name="Fecha de Nacimiento", help_text="MM/DD/AAAA")
    
    class RH(models.TextChoices):
        OP='OP',_("O+")
        ON='ON',_("O-")
        AP='AP',_("A+")
        AN='AN',_("A-")
        BP='BP',_("B+")
        BN='BN',_("B-")
        ABP='ABP',_("AB+")
        ABN='ABN',_("AB-")
        
    rh= models.CharField(max_length=3,choices=RH.choices,verbose_name="Factor RH")
    class Rol(models.TextChoices):
        INSTRUCTOR='I',_("Instructor")
        APRENDIZ='A',_("Aprendiz")
        JEFE_AREA='JA',_("Jefe de Area")
    rol=models.CharField(max_length=2,choices=Rol.choices,verbose_name="Rol")
    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento=models.CharField(max_length=2,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    
    documento= models.CharField(max_length=10,verbose_name="Documento")
    
    correo_personal= models.CharField(max_length=50,verbose_name="Correo Personal")
    correo_ins= models.CharField(max_length=50,verbose_name="Correo Institucional")
    telefono_contacto=models.CharField(max_length=10,verbose_name="Teléfono de Contacto")
    telefono_personal=models.CharField(max_length=10,verbose_name="Teléfono de Personal")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
        CONDICIONADO='2',_("Condicionado")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
        
    def clean(self):
        self.primer_nombre= self.primer_nombre.title()
        self.segundo_nombre= self.segundo_nombre.title()
        
        self.primer_apellido= self.primer_apellido.title()
        self.segundo_apellido= self.segundo_apellido.title()
        self.correo_personal= self.correo_personal.lower()
        self.correo_ins= self.correo_ins.lower()
        
                
    def __str__(self):
        return "%s %s"%(self.primer_nombre,self.primer_apellido)
    
    class Meta:
        verbose_name_plural = "Usuarios"
        
class Ficha(models.Model):
    numero_ficha=models.CharField(max_length=7,verbose_name="Primer Nombre")
    fecha_ingreso= models.DateField(verbose_name="Fecha de Ingreso", help_text="MM/DD/AAAA")
    fecha_productiva= models.DateField(verbose_name="Fecha de Etapa Productiva", help_text="MM/DD/AAAA")
    fecha_final= models.DateField(verbose_name="Fecha de Salida", help_text="MM/DD/AAAA")

class Usuarios_Ficha(models.Model):
    ficha=models.ForeignKey(Ficha, on_delete=models.CASCADE,verbose_name="Ficha")
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE,verbose_name="Usuario")

    
    

