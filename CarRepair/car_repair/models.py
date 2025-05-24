from django.db import models
from django.contrib.auth.models import User


class Repair(models.Model):
    code = models.CharField(max_length=50, null=True, blank=True)
    date_reported = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="repairs/", null=True, blank=True)
    workshop = models.ForeignKey(
        "Workshop", on_delete=models.CASCADE, null=True, blank=True
    )
    car = models.ForeignKey("Car", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.code} | {self.description} | {self.date_reported}"


class Car(models.Model):
    car_type = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, null=True, blank=True
    )
    speed_limit = models.PositiveBigIntegerField(null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.car_type} | {self.manufacturer}"


class Workshop(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    year_of_establishment = models.IntegerField(null=True, blank=True)
    repair_oldtimers = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    CEO_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.country}"


class WorkshopManufacturer(models.Model):
    workshop = models.ForeignKey(
        "Workshop", on_delete=models.CASCADE, null=True, blank=True
    )
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, null=True, blank=True
    )


# Create your models here.
