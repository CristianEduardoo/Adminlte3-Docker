from django.db import models

# Create your models here.

# table post con sus campos title, slug, body
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.TextField()
    published = models.BooleanField(default=False)

    # para tener una mejor visualizacion en la interfaz del admin
    # es opcional, ya que se mejora en el admin.py
    def __str__(self):
        return self.title

    # devuelve el nombre como su representación de cadena