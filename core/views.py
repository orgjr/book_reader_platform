from django.shortcuts import render

# Create your views here.

def index(request):
    title = "Month's top three"
    return render(request, 'core/index.html', {
        'title': title
    })


def read(request):
    return render(request, 'core/index.html', {
        'page': 'read'
    })


def book(request):
    return render(request, 'core/index.html', {
        'page': 'book'
    })


def author(request):
    return render(request, 'core/index.html', {
        'page': 'author'
    })


def reader(request):
    return render(request, 'core/index.html', {
        'page': 'reader'
    })
