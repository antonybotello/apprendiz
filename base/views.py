from django.shortcuts import redirect, render
from usuarios.models import Usuario,Ficha
from actividades.models import Llamado
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@login_required
def principal(request):
    titulo="Bienvenido al Sistema Apprendiz"
    usuarios= Usuario.objects.all().count()
    fichas= Ficha.objects.all().count()
    instructores= Usuario.objects.filter(rol=Usuario.Rol.INSTRUCTOR).count()
    llamados= Llamado.objects.all().count()
    

    context={
        "instructores":instructores,
        "usuarios":usuarios,
        "fichas":fichas,
        "titulo":titulo,
        "llamados":llamados
    }
    return render(request, "index.html",context)

def logout_user(request):
    logout(request)
    return redirect('inicio')

