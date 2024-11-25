from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profesor, Estudiante, Entregable

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)
