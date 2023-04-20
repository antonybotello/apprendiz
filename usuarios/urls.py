from django.urls import path

from usuarios.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar
from usuarios.views import ficha_listar, ficha_crear, ficha_modificar, ficha_eliminar


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

]
