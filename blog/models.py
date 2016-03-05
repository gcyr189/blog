from django.db import models
from django.utils import timezone
# Create your models here.
class Fotos (models.Model):
    autor = models.ForeignKey('auth.User')
    fecha = models.DateTimeField(default=timezone.now)
    descripcion = models.TextField()
