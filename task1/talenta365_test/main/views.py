from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CityForm, RegionForm


def index(request):
    return render(request, "main/cities_list.html")

def cities(request):
    return render(request, "main/cities_list.html")

def regions(request):
    return render(request, "main/regions_list.html")

def city_new(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main.views.cities')
    else:
        form = CityForm()
    return render(request, 'main/city_edit.html', {'form': form})

def region_new(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main.views.cities')
    else:
        form = RegionForm()
    return render(request, 'main/region_edit.html', {'form': form})
