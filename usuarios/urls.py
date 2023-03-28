from django.urls import path

from usuarios.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar

urlpatterns = [
    path('usuarios/', usuario_listar, name="usuarios" ),
    path('usuarios/crear/', usuario_crear, name="usuarios-crear" ),
    path('usuarios/modificar/<int:pk>/', usuario_modificar, name="usuarios-modificar" ),
    path('usuarios/eliminar/<int:pk>/', usuario_eliminar, name="usuarios-eliminar" ),
    
    

]
