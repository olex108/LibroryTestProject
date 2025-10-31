from django.shortcuts import render

from .models import Categories, Authors, Books


def main(request):
    return render(request, 'library/main.html')


def categories(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'library/categories.html', context)


def authors(request):
    authors = Authors.objects.all()
    context = {
        "authors": authors,
    }
    return render(request, "library/example_authors.html", context)

def books_list(request):
    books = Books.objects.all()
    context = {
        "books": books,
    }
    return render(request, "library/books_list.html", context)

def book_details(request, book_id):
    book = Books.objects.get(id=book_id)
    context = {
        "book": book,
    }
    return render(request, "library/book_details.html", context)
