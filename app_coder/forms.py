from django import forms
from .models import Profesor, Estudiante, Entregable

# Formulario para registrar un profesor
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']

# Formulario para registrar un estudiante
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

# Formulario para registrar un entregable
class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_de_entrega', 'entregado']