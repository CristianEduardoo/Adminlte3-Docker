from django.shortcuts import render
from django.http import Http404
from django.contrib import messages

# descorador para validar si el usuario esta autenticado
from django.contrib.auth.decorators import login_required

# Importamos los modelos o formularios
from .models import Post
from .forms import PostForm


# recibe un parametro de tipo (request)
# devuelve un objeto de tipo (response)
def post_list(request):
    # query_result = Post.objects.filter(published = False)  # filtra por no publicados
    query_result = Post.objects.all()  # en medio una query
    return render(request, "post/list.html", {"clave": query_result})


# render('objeto request', 'url a donde debe enviar, 'CONTEXTO,  lo que quiero que manipule el template')
# {'indice' : valor}
# con el 'indice, manipulamos el HTML'


def post_detail(request, id):
    try:
        # busca el registro cuyo ID es igual al pasado por URL
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        # Si no existe ese ID lanza la excepcion DoesNotExist y capturada con un try-except
        raise Http404("La publicación no existe")

    return render(request, "post/detail.html", {"my_post": post})


# descorador para validar si el usuario esta autenticado
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST) 
        if form.is_valid(): # valida  los campos del formulario, que no esten vacion, etc
            # cd = form.cleaned_data # obtenenos solo los required
            # print(cd)

            # Guarda el nuevo registro en BD
            new_post = form.save()

            messages.success(request, "Publicacion creada con éxito!")
            # Redirecciona a
            return render(request, "post/create_post.html", {"new_post": new_post})
    else:
        form = PostForm()  # PostForm(vacio), simplemente muestra el formulario

    return render(request, "post/create_post.html", {"registrar_post": form})
    # renderizado al template
    # pasamos el contexto {}

""" 
Aveces también necesitas realizar validaciones adicionales
como verificar la disponibilidad de recursos externos, la lógica de negocio más compleja, etc.
acceder a otros datos de la solicitud o realizar validaciones basadas en el contexto de la aplicación.
"""
