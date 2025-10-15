from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .models import Book

# Create your views here.


def index(request):
    the_title = "Month's top three..."
    top_books = Book.objects.filter(id__in=[1, 2, 3])
    return render(
        request,
        "core/index.html",
        {"page": "index", "the_title": the_title, "top_books": top_books},
    )


def read(request):
    return render(request, "core/index.html", {"page": "read"})


def book(request):
    return render(request, "core/index.html", {"page": "book"})


def author(request):
    return render(request, "core/index.html", {"page": "author"})


def reader_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("reader")
        else:
            return render(
                request,
                "core/index.html",
                {"page": "reader_login", "error": "Usuário ou senha incorretos."},
            )
    return render(request, "core/index.html", {"page": "reader_login"})


def reader(request):
    if not request.user.is_authenticated:
        return render(request, "core/index.html", {"page": "reader_login"})

    return render(request, "core/index.html", {"page": "reader"})
