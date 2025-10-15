from typing import ClassVar

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Author, Book, Reader

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "biography", "picture")
    search_fields = ("name",)
    fieldsets: ClassVar = ((None, {"fields": ("name", "age", "biography", "picture")}),)


@admin.register(Reader)
class ReaderAdmin(UserAdmin):
    list_display = ("username", "name", "email", "age", "preference")
    search_fields = ("username", "name", "email", "preference")
    fieldsets: ClassVar = (
        *UserAdmin.fieldsets,
        (None, {"fields": ("name", "age", "preference")}),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "cover", "style", "author")
    search_fields = ("title", "style", "author__name")
    fieldsets: ClassVar = (
        (
            None,
            {"fields": ("title", "cover", "style", "author", "description", "file")},
        ),
    )
