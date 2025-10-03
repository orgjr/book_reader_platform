from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author', views.author, name='author'),
    path('book', views.book, name='book'),
    path('reader', views.reader, name='reader'),
    path('read', views.read, name='read'),
]
