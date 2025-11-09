from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Categories, Authors, Books

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import AuthorsForm, BooksForm, CategoriesForm


class BooksListView(ListView):
    model = Books
    template_name = "library/books_list.html"
    context_object_name = "books"


class BookCreateView(CreateView):
    model = Books
    form_class = BooksForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:books_list")


class BookDetailView(DetailView):
    model = Books
    template_name = "library/book_detail.html"
    context_object_name = "book"


class BookUpdateView(UpdateView):
    model = Books
    form_class = BooksForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:books_list")


class BookDeleteView(DeleteView):
    model = Books
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("library:books_list")


class AuthorsListView(ListView):
    model = Authors
    template_name = "library/authors_list.html"
    context_object_name = "authors"


class AuthorCreateView(CreateView):
    model = Authors
    form_class = AuthorsForm
    template_name = "library/author_form.html"
    success_url = reverse_lazy("library:authors_list")

class AuthorUpdateView(UpdateView):
    model = Authors
    form_class = AuthorsForm
    template_name = "library/author_form.html"
    success_url = reverse_lazy("library:authors_list")


class AuthorDetailView(DetailView):
    model = Authors
    template_name = "library/author_detail.html"
    context_object_name = "author"


class CategoriesListView(ListView):
    model = Categories
    template_name = "library/categories_list.html"
    context_object_name = "categories"


class CategoryCreateView(CreateView):
    model = Categories
    form_class = CategoriesForm
    template_name = "library/category_form.html"
    success_url = reverse_lazy("library:categories_list")


def main(request):
    return render(request, 'library/main.html')
