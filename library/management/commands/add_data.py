from django.core.management import call_command
from django.core.management.base import BaseCommand

from library.models import Categories, Authors, Books


class Command(BaseCommand):
    help = "Add data to the database"

    def handle(self, *args, **kwargs) -> None:
        """
        Method to delete and add products and categories to the database
        """

        # Удаляем существующие записи
        Authors.objects.all().delete()
        Categories.objects.all().delete()
        Books.objects.all().delete()

        call_command("loaddata", "data_fixtures/authors_programming.json")
        call_command("loaddata", "data_fixtures/categories_programming.json")
        call_command("loaddata", "data_fixtures/books_programming.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
