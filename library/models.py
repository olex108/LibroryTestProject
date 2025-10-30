from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name="Category name")
    description = models.TextField(verbose_name="Category description", null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ['name']


class Authors(models.Model):

    first_name = models.CharField(max_length=100, verbose_name="Author name")
    lust_name = models.CharField(max_length=100, verbose_name="Author surname")
    mid_name = models.CharField(max_length=100, verbose_name="Author middle name", null=True)
    birthday = models.IntegerField(verbose_name="Birthday year", null=True)
    portrait = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.lust_name}"

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"
        ordering = ['lust_name']


class Book(models.Model):

    name = models.CharField(max_length=150, verbose_name="Book name")
    # category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="books"),
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name="books")
    description = models.TextField(verbose_name="Book description")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"
        ordering = ['name']

#
# class BookParameters(models.Model):
#
#     book = models.OneToOneField(Book, on_delete=models.CASCADE)
#     pages = models.IntegerField(verbose_name="Pages num")
#     heroes = models.TextField(verbose_name="Main heroes")
#
#     def __str__(self):
#         return f"{self.book}"
#
#     class Meta:
#         verbose_name = "book"
#         verbose_name_plural = "books"
#         ordering = ['book']
