from django.contrib import admin
from .models import Signature, UserSignature

# Register your models here.

# Decoradores para manejar mejor la UI del Admin en la web
@admin.register(Signature)
class SignatureAdmin(admin.ModelAdmin):
    list_display = ["nombre", "referencia", "creditos"]
    list_filter = ["referencia"]


@admin.register(UserSignature)
class UserSignatureAdmin(admin.ModelAdmin):
    list_display = ["user", "signature", "score"]
    list_filter = ["user"]
