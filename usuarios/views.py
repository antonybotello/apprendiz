from django.shortcuts import render, redirect
from usuarios.models import Usuario,Ficha
from usuarios.forms import UsuarioForm,UsuarioUpdateForm,FichaForm, FichaUpdateForm
from django.contrib import messages
from django.urls import reverse, resolve
from PIL import Image
from django.urls import reverse
from . import urls
def obtener_nombres_urls():
    lista= urls.urlpatterns
    names = list(set([url.name for url in lista if url.name is not None]))
    print(names)
    return names
# Create your views here.
def usuario_crear(request):
    titulo="Usuario"
    
    if request.method== 'POST':
        form= UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            usuario = form.save()
            if usuario.imagen:
                # Abre la imagen con Pillow
               # Abre la imagen original
                img = Image.open(usuario.imagen.path)

                # Redimensiona la imagen
                img = img.resize((500, 500))

                # Guarda la imagen redimensionada
                img.save(usuario.imagen.path)
            
            usuario.save()
            messages.success(request, 'El usuario se ha creado correctamente.')

            return redirect('usuarios')
        else:
            messages.error(request, 'Los datos del usuario tienen errores.')
    else:
        form= UsuarioForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/crear.html", context)

def usuario_listar(request, visualizar=1):
    titulo="Usuario"
    modulo="Usuarios"
    urls_list=obtener_nombres_urls()
    
    if visualizar==1:
        usuarios= Usuario.objects.filter(estado=visualizar)
    else:
        usuarios= Usuario.objects.all()

    context={
        "urls_list":urls_list,

        "titulo":titulo,
        "modulo":modulo,
        "usuarios":usuarios,
        "visualizar":visualizar
    }
    return render(request,"usuarios/listar.html", context)

def usuario_modificar(request,pk):
    titulo="Usuario"
    usuario= Usuario.objects.get(id=pk)
    
    if request.method== 'POST':
        form= UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'El formulario se ha enviado correctamente.')
            return redirect('usuarios')
    else:
        form= UsuarioUpdateForm(instance=usuario)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/modificar.html", context)

def usuario_eliminar(request,pk):
    usuario= Usuario.objects.filter(id=pk)
    
    usuario.update(
        estado="0"
    )
    return redirect('usuarios')
   
   
def ficha_crear(request):
    titulo="Ficha"
    if request.method== 'POST':
        form= FichaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fichas')
    else:
        form= FichaForm()
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"fichas/crear.html", context)

def ficha_listar(request):
    titulo="Ficha"
    modulo="Usuarios"
    fichas= Ficha.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "fichas":fichas
    }
    return render(request,"fichas/listar.html", context)

def ficha_modificar(request,pk):
    titulo="Fichas"
    
    ficha= Ficha.objects.get(id=pk)
    
    if request.method== 'POST':
        form= FichaUpdateForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return redirect('fichas')
    else:
        form= FichaUpdateForm(instance=ficha)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"fichas/modificar.html", context)

def ficha_eliminar(request,pk):
    ficha= Ficha.objects.filter(id=pk)
    ficha.update(
        estado="0"
    )
    print(ficha[0].estado)
    return redirect('fichas')
   