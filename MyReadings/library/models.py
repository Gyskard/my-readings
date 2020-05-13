from django.db import models


class Author(models.Model):
    name = models.CharField(
        "author's name",
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        "book's title",
        max_length=50,
        unique=True,
    )
    has_been_read = models.BooleanField(
        "book's status",
        default=False,
    )
    author = models.ForeignKey(
        Author,
        verbose_name="book's author",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
