from django.db import models


class Categories(models.Model):

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
    portrait = models.ImageField(upload_to="portraits/", verbose_name="Author portrait", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.lust_name}"

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"
        ordering = ['lust_name']


class Books(models.Model):

    title = models.CharField(max_length=150, verbose_name="Book name")
    category_pk = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Book category")
    author_pk = models.ManyToManyField(Authors, verbose_name="Book authors")
    publication_year = models.IntegerField(verbose_name="Publication year", null=True)
    description = models.TextField(verbose_name="Book description")

    review = models.TextField(verbose_name="Book review", null=True, blank=True)
    recommend = models.BooleanField(verbose_name="Recommend", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"
        ordering = ['title']
        permissions = (
            ("can_review_book", "Can review book"),
            ("can_recommend_book", "Can recommend book"),
        )
