from django.urls import path

from actividades.views import llamado_listar, llamado_crear, usuario_modificar, usuario_eliminar



urlpatterns = [
    
    path('llamado/', llamado_listar, name="llamados" ),

    path('llamado/crear/', llamado_crear, name="llamados-crear" ),
    path('llamado/modificar/<int:pk>/', llamado_modificar, name="llamados-modificar" ),
    path('llamado/eliminar/<int:pk>/', llamado_eliminar, name="llamados-eliminar" ),
    

]
