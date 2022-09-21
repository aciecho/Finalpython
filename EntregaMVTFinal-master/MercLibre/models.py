from django.db import models

# Create your models here.
class Posteo (models.Model):
    fechaPosteo = models.DateField()
    tituloPosteo = models.CharField(max_length=60)

    def __str__(self):
        txt = "{0} - {1}"
        return txt.format (self.tituloPosteo, self.fechaPosteo)

class Vendedor (models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    contacto = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Contacto: {self.contacto}'

class Comprador(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    contacto = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Contacto: {self.contacto}'