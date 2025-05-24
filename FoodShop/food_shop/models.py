from django.db import models
from django.contrib.auth.models import User


class FoodProduct(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=True, blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="food_products/", null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.category}"


class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_acitve = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    adress = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Sale(models.Model):
    date_sold = models.DateField(null=True, blank=True)
    client = models.ForeignKey(
        "Client", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.date_sold} | {self.client}"


class SoldProduct(models.Model):
    product = models.ForeignKey(
        "FoodProduct", on_delete=models.CASCADE, null=True, blank=True
    )
    sale = models.ForeignKey("Sale", on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)


# Create your models here.
