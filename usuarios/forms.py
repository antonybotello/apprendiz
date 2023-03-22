from django import forms

from usuarios.models import Proveedor

class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        fields = "__all__"
        # fields= ["nombre","apellido","documento","tipoDocumento"]
