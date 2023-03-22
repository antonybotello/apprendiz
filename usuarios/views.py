from django.shortcuts import render, redirect
from usuarios.models import Proveedor
from usuarios.forms import ProveedorForm
# Create your views here.
def proveedor_crear(request):
    titulo="Crear Proveedor"
    if request.method== 'POST':
        form= ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    else:
        form= ProveedorForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/crear.html", context)

def proveedor_listar(request):
    proveedores= Proveedor.objects.all()
    context={
        "proveedores":proveedores
    }
    return render(request,"usuarios/listar.html", context)

def proveedor_modificar(request):
    context={}
    return render(request,"usuarios/modificar.html", context)

def proveedor_eliminar(request):
    context={}
    return render(request,"usuarios/eliminar.html", context)