from django.urls import path  # path nos permite crear las urls que necesitemos
from . import views  # me traigo todas las vistas


app_name = "namespaceprueba"


urlpatterns = [
    path("", views.my_view, name="list_prueba"),
]
