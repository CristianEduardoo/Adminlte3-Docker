from django.db import models
from django.contrib.auth.models import User  # ==>> from auth_user


# Create your models here.

class Signature(models.Model):
    nombre = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre

    # Lo terminamos de configurar en admin.py con decoradores


class UserSignature(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signature = models.ForeignKey(Signature, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "signature"], name="unique_user_signature"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.signature.nombre}"
