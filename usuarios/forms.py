
from django.forms import ModelForm, widgets
from usuarios.models import Usuario,Ficha

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
        
class FichaForm(ModelForm):
    
    class Meta:
        model = Ficha
        fields = "__all__"
        exclude=["estado",]
        widgets={
            'fecha_ingreso': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'fecha_productiva': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d'),
            'fecha_final': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
            
        }

class FichaUpdateForm(ModelForm):
    
    class Meta:
        model = Ficha
        fields = "__all__"
        exclude=["numero","estado"]