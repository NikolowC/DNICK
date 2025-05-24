from django.shortcuts import render, redirect
from cake_shop.forms import CakeForm
from cake_shop.models import Cake


def index(request):
    cakes = Cake.objects.all()
    return render(request, "index.html", context={"cakes": cakes})


def add_cake(request):
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.save()
            return redirect("cakes")
    else:
        form = CakeForm()
    cakes = Cake.objects.all()
    return render(request, "add_cake.html", {"form": form, "cakes": cakes})


# Create your views here.
