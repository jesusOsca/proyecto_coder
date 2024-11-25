from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta para el inicio
    path('registrar_profesor/', views.registrar_profesor, name='registrar_profesor'),
    path('registrar_estudiante/', views.registrar_estudiante, name='registrar_estudiante'),
    path('registrar_entregable/', views.registrar_entregable, name='registrar_entregable'),
]
