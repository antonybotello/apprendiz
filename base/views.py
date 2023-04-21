from django.shortcuts import redirect, render
from usuarios.models import Usuario,Ficha
def principal(request):
    titulo="Bienvenido al Sitema Apprendiz"
    usuarios= Usuario.objects.all().count()
    fichas= Ficha.objects.all().count()
    instructores= Usuario.objects.filter(rol="I").count()

    

    context={
        "instructores":instructores,
        "usuarios":usuarios,
        "fichas":fichas,
        "titulo":titulo
    }
    return render(request, "index.html",context)