from django import forms

# OBLIGATORIO, si queremos que se registre en la DB de la tabla de usuario de auth
from django.contrib.auth.models import User

# Para dar de alta un usuario
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import escape  # Para escapar codigo malisioso


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario',max_length=30, required=True)
    email = forms.EmailField(label='Correo electrónico',max_length=30, help_text="Required. Inform a valid email address.")
    password1 = forms.CharField(label='Contaseña',max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña',max_length=30, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"].strip()  
        return escape(username)  

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        return escape(email)

    def clean_password1(self):
        password = self.cleaned_data["password1"]
        return escape(password)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    class Meta:
        # Modelo al que está asociado el formulario
        model = User
        
        # Campos que se deben incluir en el formulario
        fields = ["username", "email", "password1"]
        
        # Define las etiquetas para los campos del formulario
        labels = {
            "username": "Nombre de usuario",
            "email": "Correo electrónico",
            "password1": "Contraseña",
        }