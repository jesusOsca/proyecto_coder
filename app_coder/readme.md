# Proyecto Web Django - Coderhouse

Este proyecto es una aplicación web construida con Django para gestionar el registro de profesores, estudiantes y entregables. Se implementa con el patrón MVT (Modelo-Vista-Template).

## Requisitos

- Python 3.x
- Django 3.x o superior

## Instrucciones de Instalación

1. **Clonar el repositorio**:
   - Abre una terminal y ejecuta:
     ```bash
     git clone https://github.com/tu_usuario/tu_repositorio.git
     ```
   
2. **Crear y activar un entorno virtual** (opcional, pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows

3. **Funcionalidades**

    Página de inicio:
        Ruta: /inicio/
        Muestra un enlace a las páginas de registro de profesores, estudiantes y entregables.

    Registro de Profesores:
        Ruta: /registrar-profesor/
        Formulario para registrar un profesor. Se requiere el nombre, apellido, email y profesión.
        Funcionalidad: El formulario guarda la información del profesor en la base de datos y redirige a la página de inicio al completarse.

    Registro de Estudiantes:
        Ruta: /registrar-estudiante/
        Formulario para registrar un estudiante. Se requiere el nombre, apellido y email.
        Funcionalidad: El formulario guarda la información del estudiante en la base de datos y redirige a la página de inicio al completarse.

    Registro de Entregables:
        Ruta: /registrar-entregable/
        Formulario para registrar un entregable. Se requiere el nombre del entregable, fecha de entrega y un checkbox de "entregado".
        Funcionalidad: El formulario guarda el entregable en la base de datos y redirige a la página de inicio al completarse.