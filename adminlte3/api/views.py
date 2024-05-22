# Nos olvidamos del render y usamos un viewsets y permissions
from rest_framework import viewsets, permissions
from blog.models import Post # Importamos el modelo
from .serializers import PostSerializer # Importamos el serializador

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # queryset => es convención. Le decimos que nos traiga todos los posts
    serializer_class = PostSerializer  # Le decimos que serializador va a usar
    permission_classes = [permissions.AllowAny] # Le decimos que permisos tiene el usuario para acceder a los datos 
