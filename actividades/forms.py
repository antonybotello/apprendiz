from django.forms import ModelForm, widgets
from actividades.models import Llamado
class LlamadoForm(ModelForm):
    
    class Meta:
        model = Llamado
        fields = "__all__"
        exclude=["estado",]
    def __init__(self, *args, **kwargs):
        super(IntegrantesForm, self).__init__(*args, **kwargs)
        self.fields["aprendiz"].queryset = Usuario.objects.filter(estado=Usuario.Estado.ACTIVO,rol=Usuario.Rol.APRENDIZ)

        