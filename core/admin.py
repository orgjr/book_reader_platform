from typing import ClassVar

from django.contrib import admin

from .models import Autor, Leitor, Leitura, Livro

# Register your models here.


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade')
    search_fields = ('nome',)
    fieldsets: ClassVar = (
        (None, {
            'fields': ('nome', 'idade',)
            }),
        )

@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'preferencia')
    search_fields = ('nome', 'preferencia', 'livros')
    fieldsets: ClassVar = (
        (None, {
            'fields': ('nome', 'idade', 'preferencia')
            }),
        )

@admin.register(Leitura)
class LeituraAdmin(admin.ModelAdmin):
    list_display = ('leitor', 'livro', 'data_leitura', 'avaliacao')
    search_fields = ('leitor', 'livro', 'data_leitura', 'avaliacao')
    fieldsets: ClassVar = (
        (None, {
            'fields': ('leitor', 'livro', 'data_leitura', 'avaliacao')
            }),
        )

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'capa', 'estilo', 'autor')
    search_fields = ('titulo', 'capa', 'estilo', 'autor')
    fieldsets: ClassVar = (
        (None, {
            'fields': ('titulo', 'capa', 'estilo', 'autor')
            }),
        )
