from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import Usuario,Ficha,Proyecto,Integrantes
from usuarios.forms import UsuarioForm,UsuarioUpdateForm
from usuarios.forms import FichaForm, FichaUpdateForm
from usuarios.forms import ProyectoForm, ProyectoUpdateForm
from usuarios.forms import IntegrantesForm




from django.contrib import messages
from django.urls import reverse, resolve
from PIL import Image
from django.urls import reverse
from . import urls
from django.core.paginator import Paginator, PageNotAnInteger
    # """Esta funcion permite filtrar las urls
    # """
# def obtener_nombres_urls(modulo):
#     lista= urls.urlpatterns
#     names = list(set([url.name for url in lista if url.name is not None and url.name.startswith(modulo)]))
#     print(names)
#     return names
#     print(names)
#     return names
# # Create your views here.
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
    return render(request,"usuarios/usuarios/crear.html", context)

def usuario_listar(request, visualizar=1):
    titulo="Usuario"
    modulo="Usuarios"
    
    # urls_list=obtener_nombres_urls(modulo.lower())
    
    if visualizar==1:
        usuarios= Usuario.objects.filter(estado=visualizar)
    else:
        usuarios= Usuario.objects.all()

    paginator = Paginator(usuarios, 3) # 3 usuarios por página
    page_number = request.GET.get('page') # número de página actual
    try:
        usuarios = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, mostrar la primera página.
        usuarios = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera de rango, mostrar la última página.
        usuarios = paginator.page(paginator.num_pages)
    context={
        # "urls_list":urls_list,

        "titulo":titulo,
        "modulo":modulo,
        "usuarios":usuarios,
        "visualizar":visualizar
    }
    return render(request,"usuarios/usuarios/listar.html", context)

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
    return render(request,"usuarios/usuarios/modificar.html", context)

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
    return render(request,"usuarios/fichas/crear.html", context)

def ficha_listar(request):
    titulo="Ficha"
    modulo="Usuarios"
    fichas= Ficha.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "fichas":fichas
    }
    return render(request,"usuarios/fichas/listar.html", context)

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
    return render(request,"usuarios/fichas/modificar.html", context)

def ficha_eliminar(request,pk):
    ficha= Ficha.objects.filter(id=pk)
    ficha.update(
        estado="0"
    )
    print(ficha[0].estado)
    return redirect('fichas')
   


def proyecto_listar(request):
    titulo="Proyecto"
    modulo="Usuarios"
    proyectos= Proyecto.objects.all()
    context={
        "titulo":titulo,
        "modulo":modulo,
        "proyectos":proyectos
    }
    return render(request,"usuarios/proyectos/listar.html", context)
def proyecto_crear(request,pk=0):
    titulo="Proyectos"
    modulo="Usuarios"

    proyecto= Proyecto.objects.filter(id=pk)
    integrantes= Integrantes.objects.filter(grupo_id=pk)
    # para el form de creacion del grupo
    if request.method== 'POST' and 'form-grupo' in request.POST:
        form_proyecto= ProyectoForm(request.POST)
        if form_proyecto.is_valid():
            aux=form_proyecto.save()
            return redirect('proyectos-crear',aux.id)
        else:
            messages.danger(request, 'Error al crear el grupo   .')
        
    else:
        form_proyecto= ProyectoForm()
    # para el form de agregar aprendiz al grupo
    if request.method== 'POST' and 'form-integrante' in request.POST:
        form_integrante= IntegrantesForm(request.POST)
        if form_integrante.is_valid():
            integrante = form_integrante.save(commit=False)  # No guarda todavía el objeto en la base de datos
            integrante.grupo_id = pk  # Asigna el grupo_id al objeto integrante
            integrante.save()
            messages.success(request, 'El Aprendiz se agregó correctamente.')

            return redirect('proyectos-crear',pk)
        else:
            messages.success(request, 'Error al agregar el aprendiz.')

    else:
        form_integrante= IntegrantesForm()
    context={   
        "form_integrante":form_integrante,
        "form_proyecto":form_proyecto,
        "titulo":titulo,
        "modulo":modulo,
        "proyecto":proyecto,
        "integrantes":integrantes
    }
    return render(request,"usuarios/proyectos/crear.html", context)

def proyecto_modificar(request,pk):
    titulo="Proyectos"
    
    proyecto= Proyecto.objects.get(id=pk)
    
    if request.method== 'POST':
        form= ProyectoUpdateForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('proyectos')
    else:
        form= ProyectoUpdateForm(instance=proyecto)
    context={
        "titulo":titulo,
        "form":form
        }
    return render(request,"usuarios/proyectos/modificar.html", context)

def proyecto_eliminar(request,pk):
    proyecto= Proyecto.objects.filter(id=pk)
    proyecto.update(
        estado="0"
    )
    print(proyecto[0].estado)
    return redirect('proyectos')
   
def integrante_eliminar(request,pk):
    integrante = get_object_or_404(Integrantes, id=pk)
    id_proy=integrante.grupo.id
    integrante.delete()
    return redirect('proyectos-crear',id_proy)