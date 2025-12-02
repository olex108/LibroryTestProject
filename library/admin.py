from django.contrib import admin
from .models import (
                     Authors,
                     Categories,
                     Books,
                     )


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "lust_name", "birthday")
    list_filter = ("lust_name",)
    search_fields = ("lust_name",)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("author_pk", "category_pk")
    search_fields = ("title", )
