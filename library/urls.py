from django.urls import path
from . import views


app_name = 'library'


urlpatterns = [
    path("books/", views.BooksListView.as_view(), name="books_list"),
    path("books/new/", views.BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/update/<int:pk>/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/delete/<int:pk>/", views.BookDeleteView.as_view(), name="book_delete"),

    path("main/", views.main, name="main"),
    path("categories/", views.categories, name="categories"),
    path("authors/", views.authors, name="authors"),
    # path("books_list/", views.books_list, name="books_list"),
    # path("book_details/<int:book_id>", views.book_details, name="book_details"),
]
