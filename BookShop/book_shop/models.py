from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Book(models.Model):
    TYPE_CHOICES = [("S", "Soft"), ("H", "Hard")]
    CATEGORY_CHOICES = [
        ("R", "Romance"),
        ("T", "Thriller"),
        ("B", "Biography"),
        ("C", "Classic"),
        ("D", "Drama"),
        ("H", "History"),
    ]
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="book_images/", null=True, blank=True)
    isbn = models.CharField(max_length=100, null=True, blank=True)
    year_release = models.DateField(null=True, blank=True)
    publisher_house = models.ForeignKey(
        "PublisherHouse", on_delete=models.CASCADE, null=True, blank=True
    )
    number_of_pages = models.IntegerField(null=True, blank=True)
    book_dimensions = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    type_book = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        null=True,
        blank=True
    )

    category_book = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title} - {self.publisher_house} - {self.category_book}'


class PublisherHouse(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    year_of_establishment = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    website = models.URLField()

    def __str__(self):
        return self.name
