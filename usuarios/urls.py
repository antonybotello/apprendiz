from django.urls import path

from usuarios.views import proveedor_listar, proveedor_crear

urlpatterns = [
    path('proveedores/', proveedor_listar, name="proveedores" ),
    path('proveedores/crear/', proveedor_crear, name="proveedores-crear" ),

]
