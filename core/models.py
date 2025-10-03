from pathlib import Path

from django.db import models

APP_PATH = Path(__file__).resolve().parent
IMAGE_PATH = APP_PATH / 'static' / 'core' / 'images'

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    capa = models.ImageField(upload_to=str(IMAGE_PATH), blank=True, null=True)
    estilo = models.CharField(max_length=100, blank=True)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name="livros"
    )

    def __str__(self):
        return self.titulo


class Leitor(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    preferencia = models.CharField(max_length=200, blank=True)
    livros = models.ManyToManyField(Livro, through="Leitura", related_name="leitores")

    def __str__(self):
        return self.nome


class Leitura(models.Model):
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_leitura = models.DateField(blank=True, null=True)
    avaliacao = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.leitor.nome} leu {self.livro.titulo}"
