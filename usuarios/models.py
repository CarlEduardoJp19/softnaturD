from django.db import models

# Create your models here.
class usuario(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('cliente', 'Cliente'),
    )

    nombre = models.CharField(max_length=150)
    clave = models.CharField(max_length=90)
    email = models.EmailField(max_length=60, unique=True)
    numTelefono = models.CharField(max_length=10)
    rol = models.CharField(max_length=20, choices=ROLES, default='cliente')  # 👈 Solo admin y cliente

    def __str__(self):
        return self.nombre