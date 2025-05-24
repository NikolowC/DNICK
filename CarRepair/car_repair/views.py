from django.shortcuts import render, redirect
from car_repair.forms import RepairForm
from car_repair.models import Repair


def index(request):
    return render(request, "index.html")


def repairs(request):
    if request.method == "POST":
        form = RepairForm(request.POST, request.FILES)
        if form.is_valid():
            repairs = form.save(commit=False)
            repairs.user = request.user
            repairs.save()
            return redirect("repairs")
    else:
        form = RepairForm()
    repairs = Repair.objects.filter(user=request.user, car__car_type="Седан")
    return render(request, "repairs.html", {"form": form, "repairs": repairs})


# Create your views here.
