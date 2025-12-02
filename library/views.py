from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseForbidden

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Categories, Authors, Books

from .forms import AuthorsForm, BooksForm, CategoriesForm


class ReviewBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Books, pk=pk)

        if not request.user.has_perm("library.can_review_book"):
            return HttpResponseForbidden("You don't have permission to review books.")
        else:
            book.review = request.POST.get('review')
            book.save()

        return redirect("library:book_detail", pk=pk)


class RecommendBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Books, pk=pk)

        if not request.user.has_perm("library.can_recommend_book"):
            return HttpResponseForbidden("You don't have permission to recommend books.")

        book.recommend = True
        book.save()

        return redirect("library:book_detail", pk=pk)


class BooksListView(ListView):
    model = Books
    template_name = "library/book/books_list.html"
    context_object_name = "books"


class BookCreateView(CreateView):
    model = Books
    form_class = BooksForm
    template_name = "library/book/book_form.html"
    success_url = reverse_lazy("library:books_list")


class BookDetailView(DetailView):
    model = Books
    template_name = "library/book/book_detail.html"
    context_object_name = "book"


class BookUpdateView(UpdateView):
    model = Books
    form_class = BooksForm
    template_name = "library/book/book_form.html"
    success_url = reverse_lazy("library:books_list")


class BookDeleteView(DeleteView):
    model = Books
    template_name = "library/book/book_confirm_delete.html"
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
