from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Categories, Authors, Books

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BooksListView(ListView):
    model = Books
    template_name = "library/books_list.html"
    context_object_name = "books"


class BookCreateView(CreateView):
    model = Books
    fields = ["title", "category_pk", "author_pk", "publication_year", "description"]
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:books_list")



class BookDetailView(DetailView):
    model = Books
    template_name = "library/book_detail.html"
    context_object_name = "book"


class BookUpdateView(UpdateView):
    model = Books
    fields = ["title", "category_pk", "author_pk", "publication_year", "description"]
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:books_list")


class BookDeleteView(DeleteView):
    model = Books
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("library:books_list")



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
#
# def books_list(request):
#     books = Books.objects.all()
#     context = {
#         "books": books,
#     }
#     return render(request, "library/books_list.html", context)
#
# def book_details(request, book_id):
#     book = Books.objects.get(id=book_id)
#     context = {
#         "book": book,
#     }
#     return render(request, "library/book_detail.html", context)
