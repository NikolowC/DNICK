from django.shortcuts import render, redirect
from food_shop.models import FoodProduct
from food_shop.forms import FoodProductForm


def index(request):
    food_products = FoodProduct.objects.all()
    return render(request, "index.html", context={"products": food_products})


def outofstock(request):
    if request.method == "POST":
        form = FoodProductForm(request.POST, request.FILES)
        if form.is_valid():
            food_product = form.save(commit=False)
            food_product.save()
            return redirect("outofstock")
    else:
        form = FoodProductForm()
    food_products = FoodProduct.objects.filter(quantity=0, category__is_acitve=True)
    return render(request, "outofstock.html", {"form": form, "products": food_products})


# Create your views here.
