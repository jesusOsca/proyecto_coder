from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_coder.urls')),  # Incluye las rutas de app_coder
]
