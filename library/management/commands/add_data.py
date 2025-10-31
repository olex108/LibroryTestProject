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
        # Authors.objects.all().delete()
        # Categories.objects.all().delete()
        Books.objects.all().delete()


        # author_1 = Authors.objects.get_or_create(
        #     first_name = "Лев",
        #     lust_name = "Толстой",
        #     mid_name = "Николаевич",
        #     birthday = 1928,
        #     portrait = None
        #
        # )
        #
        # category_1 = Categories.objects.get_or_create(
        #     name = "Роман",
        #     description = "Большое повествовательное художественное произведение со сложным сюжетом",
        # )
        #
        # books = [

        # ]

        # category_1, _ = Category.objects.get_or_create(
        #     name='Смартфоны',
        #     description='Смартфон это телефон, имеющий начинку и функционал почти как у компьютера'
        # )
        # category_2, _ = Category.objects.get_or_create(
        #     name='Смарт-часы',
        #     description='Типовыми функциями смарт-часов и браслетов являются подсчет количества шагов'
        # )
        #
        # products = [
        #     {
        #         "name": 'Samsung Galaxy S25 Ultra',
        #         "description": 'Samsung Galaxy S25 Ultra - новый взгляд на будущее мобильных технологий',
        #         "price": 99990,
        #         "category": category_1,
        #     },
        #     {
        #         "name": 'Samsung Galaxy A56',
        #         "description": 'Samsung Galaxy A56 – это новый смартфон 2025 года с мощным процессором Exynos 1580',
        #         "price": 27390,
        #         "category": category_1,
        #     },
        #     {
        #         "name": 'Samsung Galaxy Watch8',
        #         "description": 'Смарт-часы Samsung Galaxy Watch 8 44mm — это именно то, что вам нужно!',
        #         "price": 20990,
        #         "category": category_2,
        #     },
        #     {
        #         "name": 'Samsung Galaxy Watch8 Classic',
        #         "description": 'Умные часы Samsung Galaxy Watch8 Classic 46mm — это не просто аксессуар, а мощный инструмент',
        #         "price": 25990,
        #         "category": category_2,
        #     },
        #
        # ]

        # for product in products:
        #     product, created = Product.objects.get_or_create(**product)
        #     if created:
        #         self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
        #     else:
        #         self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))

        # call_command("loaddata", "data_fixtures/authors_programming.json")
        # call_command("loaddata", "data_fixtures/categories_programming.json")
        call_command("loaddata", "data_fixtures/books_programming.json")
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixture"))
