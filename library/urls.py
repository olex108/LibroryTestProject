from django.urls import path
from . import views


app_name = 'library'


urlpatterns = [
    path("books/", views.BooksListView.as_view(), name="books_list"),
    path("books/new/", views.BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/update/<int:pk>/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/delete/<int:pk>/", views.BookDeleteView.as_view(), name="book_delete"),

    path("authors/", views.AuthorsListView.as_view(), name="authors_list"),
    path("authors/new/", views.AuthorCreateView.as_view(), name="author_create"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author_detail"),

    path("categories/", views.CategoriesListView.as_view(), name="categories_list"),
    path("categories/new/", views.CategoryCreateView.as_view(), name="category_create"),

    path("main/", views.main, name="main"),


    # path("books_list/", views.books_list, name="books_list"),
    # path("book_details/<int:book_id>", views.book_details, name="book_details"),
]
