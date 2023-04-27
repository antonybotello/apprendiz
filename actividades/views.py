from django.shortcuts import render
from actividades.models import Llamado
from actividades.forms import LlamadoForm
# Create your views here.

   
def llamado_crear(request):
    titulo="Llamado"
    if request.method== 'POST':
        form= LlamadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('llamados')
    else:
        form= LlamadoForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/llamados/crear.html", context)

def llamado_listar(request):
    titulo="Llamado"
    modulo="Usuarios"
    llamados= Llamado.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "llamados":llamados
    }
    return render(request,"usuarios/llamados/listar.html", context)

def llamado_eliminar(request,pk):
    llamado= Llamado.objects.filter(id=pk)
    llamado.update(
        estado="0"
    )
    print(llamado[0].estado)
    return redirect('llamados')
   