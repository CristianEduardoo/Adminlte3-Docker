from django.shortcuts import render, redirect

# descorador para validar si el usuario esta autenticado
from django.contrib.auth.decorators import login_required

# OBLIGATORIO, si queremos que se registre en la DB de la tabla de usuario de auth
from django.contrib.auth.models import User
from django.utils.html import escape  # Función escape para escapar codigo malisioso


# Importamos los modelos o formulario
from .forms import SignUpForm
from .models import UserSignature


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Limpia y valida la entrada del usuario
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            # Escapa los datos antes de procesarlos
            username = escape(username)
            email = escape(email)
            password = escape(password)

            # Crea un nuevo usuario con los datos limpios y validados
            user = User.objects.create_user(username, email, password)
            user.save()

            return redirect("login") # login => de mi accounts de mi urls de mi proyecto
            # que se encuentra en mi lista de apps INSTALLED_APPS en settings de mi proyecto
            # return redirect(request, "registration/login.html")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def user_data_and_notes(request):
    # Obtener el usuario actualmente autenticado
    user = request.user

    # Obtener los datos y las notas del usuario actual
    user_data_and_notes = UserSignature.objects.filter(user=user)

    # Renderizar la plantilla con los datos y las notas del usuario
    return render(request, "usuario/udnotes.html", {"udnotes": user_data_and_notes})
