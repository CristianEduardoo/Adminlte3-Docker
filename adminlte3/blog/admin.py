from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post)
# Decorador para registrar el modelo Post tunneado en el sitio de administrador
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # List of fields to display in the admin change list
    list_display = ["title", "slug", "content", "published"]

    # List of fields to filter the admin change list
    list_filter = ["published"]

    # Campos de búsqueda por medio de 2 campos
    search_fields = ["title", "slug"]

    # rellena el slug en base al title
    prepopulated_fields = {"slug": ("title",)}