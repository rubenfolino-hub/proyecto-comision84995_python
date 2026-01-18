

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
    path('', include('biblioteca.urls')),
]

# ESTO ES LA CLAVE: 
# Si estamos en modo DEBUG (desarrollo), habilitamos la ruta de archivos multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)