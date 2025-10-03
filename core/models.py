from django.core.validators import MaxLengthValidator
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    biography = models.TextField(blank=True, validators=[MaxLengthValidator(200)])
    picture = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )
    title = models.CharField(max_length=35)
    description = models.TextField(blank=True, validators=[MaxLengthValidator(200)])
    style = models.CharField(max_length=100, blank=True)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='docs/', blank=True, null=True)

    def __str__(self):
        return self.title


class Reader(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    preference = models.CharField(max_length=200, blank=True)
    books = models.ManyToManyField(Book, through="Read", related_name="readers")

    def __str__(self):
        return self.name


class Read(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    read_date = models.DateField(blank=True, null=True)
    evaluation = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.reader.name
