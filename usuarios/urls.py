from django.urls import path

from usuarios.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar
from usuarios.views import ficha_listar, ficha_crear, ficha_modificar, ficha_eliminar
from usuarios.views import proyecto_listar, proyecto_crear, proyecto_modificar, proyecto_eliminar
from usuarios.views import integrante_eliminar




urlpatterns = [
    path('usuario/<int:visualizar>/', usuario_listar, name="usuarios" ),
    path('usuario/', usuario_listar, name="usuarios" ),

    path('usuario/crear/', usuario_crear, name="usuarios-crear" ),
    path('usuario/modificar/<int:pk>/', usuario_modificar, name="usuarios-modificar" ),
    path('usuario/eliminar/<int:pk>/', usuario_eliminar, name="usuarios-eliminar" ),
    
    path('ficha/', ficha_listar, name="fichas" ),
    path('ficha/crear/', ficha_crear, name="fichas-crear" ),
    path('ficha/modificar/<int:pk>/', ficha_modificar, name="fichas-modificar" ),
    path('ficha/eliminar/<int:pk>/', ficha_eliminar, name="fichas-eliminar" ),

    path('proyecto/', proyecto_listar, name="proyectos" ),

    path('proyecto/crear/', proyecto_crear, name="proyectos-crear" ),
    path('proyecto/gestionar/<int:pk>/', proyecto_crear, name="proyectos-crear" ),

    path('proyecto/modificar/<int:pk>/', proyecto_modificar, name="proyectos-modificar" ),
    path('proyecto/eliminar/<int:pk>/', proyecto_eliminar, name="proyectos-eliminar" ),

    path('proyecto/integrante/eliminar/<int:pk>/', integrante_eliminar, name="integrante-eliminar" ),
]
