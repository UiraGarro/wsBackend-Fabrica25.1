from django.db import models

class filmes(models.Model):
    título = models.CharField(max_length=50)
    ano = models.CharField(max_length=4)
    diretor = models.CharField(max_length=50)
    genero = models.CharField(max_length=30)
    sinopse = models.TextField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.título
