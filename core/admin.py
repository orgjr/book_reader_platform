from typing import ClassVar

from django.contrib import admin

from .models import Author, Book, Read, Reader

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'biography', 'picture')
    search_fields = ('name',)
    fieldsets: ClassVar = (
        (None, {
            'fields': ('name', 'age', 'biography', 'picture')
            }),
        )

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'preference')
    search_fields = ('name', 'preference')
    fieldsets: ClassVar = (
        (None, {
            'fields': ('name', 'age', 'preference')
            }),
        )

@admin.register(Read)
class ReadAdmin(admin.ModelAdmin):
    list_display = ('reader', 'book', 'read_date', 'evaluation')
    search_fields = ('reader__name', 'book__title')
    fieldsets: ClassVar = (
        (None, {
            'fields': ('reader', 'book', 'read_date', 'evaluation')
            }),
        )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover', 'style', 'author')
    search_fields = ('title', 'style', 'author__name')
    fieldsets: ClassVar = (
        (None, {
            'fields': ('title', 'cover', 'style', 'author', 'description', 'file')
            }),
        )
