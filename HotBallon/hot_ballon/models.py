from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Flight(models.Model):
    code = models.CharField(max_length=50, null=True, blank=True)
    airport_start = models.CharField(max_length=50, null=True, blank=True)
    airport_end = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="flights/", null=True, blank=True)
    ballon = models.ForeignKey(
        "HotBallon", on_delete=models.CASCADE, null=True, blank=True
    )
    pilot = models.ForeignKey("Pilot", on_delete=models.CASCADE, null=True, blank=True)
    airline = models.ForeignKey(
        "Airline", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.code} | From: {self.airport_start} To: {self.airport_end}"


class Pilot(models.Model):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    flying_hours = models.IntegerField(null=True, blank=True)
    act = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname}  {self.lastname}"


class HotBallon(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    limit_passengers = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} | Manufacturer: {self.manufacturer}"


class Airline(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    year_of_establishment = models.IntegerField(null=True, blank=True)
    is_in_Europe = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PilotAirline(models.Model):
    pilot = models.ForeignKey("Pilot", on_delete=models.CASCADE, null=True, blank=True)
    airline = models.ForeignKey(
        "Airline", on_delete=models.CASCADE, null=True, blank=True
    )
