from django.db import models

class usuario (models.Model):
    nombre = models.CharField(max_length=150)
    clave = models.CharField(max_length=90)
    email = models.EmailField(max_length=60, unique=True)
    numTelefono = models.CharField(max_length=10)

