

"""
URL configuration for proyecto_python project.
"""
from django.contrib import admin
from django.urls import path, include

# IMPORTANTE: Necesitamos estas dos importaciones para las imágenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # App de Lógica de Negocio
    path('', include('biblioteca.urls')),
    
    # App de Usuarios y Autenticación (Requisito del profesor cumplido ✅)
    path('accounts/', include('accounts.urls')),
]

# Si estamos en modo DEBUG (desarrollo), habilitamos la ruta de archivos multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    