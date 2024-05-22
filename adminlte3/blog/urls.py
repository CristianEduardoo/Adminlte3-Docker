from django.urls import path  # path nos permite crear las urls que necesitemos
from . import views  # me traigo todas las vistas

# Un namespace manejar los enlaces, botones, etc en el template de forma facil
# Todas las URLs definidas en este archivo urls.py pertenecen al espacio de nombres 'namespaceblog'.
app_name = "namespaceblog"


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:id>/", views.post_detail, name="post_detail"),  # <int:id> una url dinámica con el ID de cada post
    path("registro-post/", views.create_post, name="post-register"),
]


# path("la ruta-url, en la barra de navegacion", views.post_list, name="post_list")
# views.post_list  es una funcion que se encuentra en views.py
# name='post_list' le doy el nombre a la url en caso cambie el nombre de la vista... es como un namespaces
