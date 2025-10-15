from django.core.validators import MaxLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(blank=True, null=True)
    biography = models.TextField(blank=True, validators=[MaxLengthValidator(600)])
    picture = models.ImageField(upload_to="images/authors/", blank=True, null=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=35)
    description = models.TextField(blank=True, validators=[MaxLengthValidator(600)])
    style = models.CharField(max_length=100, blank=True)
    cover = models.ImageField(upload_to="images/covers/", blank=True, null=True)
    file = models.FileField(upload_to="docs/", blank=True, null=True)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.title


class Reader(AbstractUser):
    name = models.CharField(max_length=200)
    age = models.IntegerField(blank=True, null=True)
    preference = models.CharField(max_length=200, blank=True)
    books = models.ManyToManyField(Book, through="Read", related_name="readers")

    class Meta:
        verbose_name = "Leitor"
        verbose_name_plural = "Leitores"

    def __str__(self):
        return self.name


class Read(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    read_date = models.DateField(blank=True, null=True)
    evaluation = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.reader.name
