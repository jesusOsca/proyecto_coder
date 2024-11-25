from django.shortcuts import render, redirect
from .forms import ProfesorForm, EstudianteForm, EntregableForm

# Vista para el inicio
def inicio(request):
    return render(request, 'app_coder/inicio.html')

# Vista para registrar un profesor
def registrar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige al inicio después de guardar
    else:
        form = ProfesorForm()
    return render(request, 'app_coder/registrar_profesor.html', {'form': form})

# Vista para registrar un estudiante
def registrar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EstudianteForm()
    return render(request, 'app_coder/registrar_estudiante.html', {'form': form})

# Vista para registrar un entregable
def registrar_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EntregableForm()
    return render(request, 'app_coder/registrar_entregable.html', {'form': form})
