from django.contrib import admin
from .models import (Authors, Category,
                     Book,
                     # BookParameters
                     )

@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "mid_name", "lust_name")
    list_filter = ("lust_name",)
    search_fields = ("lust_name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("author", "category")
    search_fields = ("name", )
