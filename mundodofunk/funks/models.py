from django.db import models

# Create your models here.
from django.db import models

class Funk(models.Model):
    nome = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    duracao = models.TimeField()
    descricao = models.TextField()
    data = models.DateField()
    logo = models.URLField()

    def __str__(self):
            return self.title
