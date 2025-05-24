from django.shortcuts import render, redirect
from hot_ballon.models import *
from .forms import FlightForm


def index(request):
    ballons = HotBallon.objects.all()
    return render(request, "index.html", context={"ballons": ballons})


# Create your views here.


def flights(request):
    if request.method == "POST":
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            ballons = form.save(commit=False)
            ballons.save()
            return redirect("flights")
    else:
        form = FlightForm()
    flights = Flight.objects.all()
    return render(request, "flights.html", {"form": form, "flights": flights})
