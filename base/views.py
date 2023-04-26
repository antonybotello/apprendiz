from django.shortcuts import redirect, render
from usuarios.models import Usuario,Ficha
from actividades.models import Llamado
def principal(request):
    titulo="Bienvenido al Sistema Apprendiz"
    usuarios= Usuario.objects.all().count()
    fichas= Ficha.objects.all().count()
    instructores= Usuario.objects.filter(rol="I").count()
    llamados= Llamado.objects.all().count()
    

    context={
        "instructores":instructores,
        "usuarios":usuarios,
        "fichas":fichas,
        "titulo":titulo,
        "llamados":llamados
    }
    return render(request, "index.html",context)