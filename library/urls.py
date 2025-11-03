from django.urls import path
from . import views


app_name = 'library'


urlpatterns = [
    path("main/", views.main, name="main"),
    path("categories/", views.categories, name="categories"),
    path("authors/", views.authors, name="authors"),
    path("books_list/", views.books_list, name="books_list"),
    path("book_details/<int:book_id>", views.book_details, name="book_details"),
]
