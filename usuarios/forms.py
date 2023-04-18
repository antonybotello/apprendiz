from django import forms

from django.forms import ModelForm, widgets
from usuarios.models import Usuario

class UsuarioForm(ModelForm):
    
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude=["estado",]
        # fields= ["nombre","apellido","documento","tipoDocumento"]
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
class UsuarioUpdateForm(ModelForm):
    
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude=["documento","rh","fecha_nacimiento"]