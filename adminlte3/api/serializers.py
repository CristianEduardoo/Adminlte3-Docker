from rest_framework import serializers # Se encargan de convertir la información de los modelos a JSON
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title', 'content', 'published')
    # Los campos que voy a serializar a Json     
