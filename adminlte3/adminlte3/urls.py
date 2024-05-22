from django.contrib import admin
from django.urls import path, include # include para incluir otras url de otras aplicaciones ejm: 'blog'
from django.conf import settings
from django.conf.urls.static import static

""" PARA ACCEDER A LOS ESQUEMAS CREADOS archivo.yml desde la web, tenemos que establecer las url's """
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView)


# Tambien conocidos como EndPoints => Hablando de documentación de Apis
urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # URL de Autenticacion y Autorización de Django
    path('api/v1/', include("api.urls", namespace ="api")), # Registramos las Urls de nuestra API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # url_name='schema' => el name coincide con el name de SpectacularAPIView.as_view()
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("", include("blog.urls", namespace="blog")),
    path("usuarios/", include("usuarios.urls", namespace="usuarios")),
    path("prueba-adminlte3/", include("prueba.urls", namespace="prueba")),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
