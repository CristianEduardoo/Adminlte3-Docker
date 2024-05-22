from django import forms

# si queremos que se registre en la DB, debemos inportar como en admin.py
from .models import Post
from django.utils.html import escape  # para escapar codigo malisioso


# class PostForm (forms.Form): => de formulario regular a PERSISTENTE
class PostForm(forms.ModelForm):
    title = forms.CharField(label="Título para la publicación", max_length=250)
    content = forms.CharField(label="Contenido", widget=forms.Textarea)
    published = forms.BooleanField(label="¿Publicar?", required=False)  # No es obligatorio

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        return escape(title)

    def clean_content(self):
        content = self.cleaned_data["content"].strip()
        return escape(content)

    # Esto define una clase interna Meta que proporciona metadatos adicionales sobre el formulario.
    class Meta:
        # El modelo en el que se basará el formulario, en este caso, Post.
        model = Post
        # Campos del modelo Post deben incluirse en el formulario.
        fields = ["title", "content", "published"]


""" puedes personalizar los mensajes de error para cada campo. """
