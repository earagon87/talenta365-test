from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CityForm, RegionForm
from .models import City, Region


def index(request):
    return render(request, "main/cities_list.html")

def cities(request):
    cities_list = City.objects.all()
    context = {'cities_list': cities_list}
    return render(request, "main/cities_list.html", context)

def regions(request):
    regions_list = Region.objects.all()
    context = {'regions_list': regions_list}
    return render(request, "main/regions_list.html", context)

def city_new(request):
    """
    View that handles the process of adding a new city.
    """
    error = False
    # Processing data from POST
    if request.method == "POST":
        # Building the form
        form = CityForm(request.POST)
         # Checking if the form is valid
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    '<strong>Success!</strong> A new city was created'
                )
                return redirect('cities')
            except Exception:
                error = True
        # The form is invalid
        else:
            error = True
        # Showing an error message
        if error:
            messages.error(
                request,
                u"<strong>Ouch.</strong> The city couldn't be "
                u"created. Please verify the data."
            )
    # No POST data: showing the empty form
    else:
        form = CityForm()

    # Returning   
    return render(request, 'main/city_edit.html', {'form': form})

def city_edit(request, pk):
    """
    View that handles the process of editing a city.
    """
    error = False
    # Getting city from pk
    city = get_object_or_404(City, pk=pk)
    # Processing data from POST
    if request.method == "POST":
        # Building the form using retrieved city
        form = CityForm(request.POST, instance=city)
        # Checking if the form is valid
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    '<strong>Success!</strong> City was edited'
                )
                return redirect('cities')
            except Exception:
                error = True
        # The form is invalid
        else:
            error = True
        # Showing an error message
        if error:
            messages.error(
                request,
                u"<strong>Ouch.</strong> The city couldn't be "
                u"modified. Please verify the data."
            )
    # No POST data: showing the form
    else:
        form = CityForm(instance=city)
    # Returning   
    return render(request, 'main/city_edit.html', {'form': form})

def city_delete(request, pk):
    """
    View that handles the process of deleting a city.
    """
    error = False
    try:
        City.objects.get(pk=pk).delete()
        messages.success(
            request,
            '<strong>Success!</strong> City was removed'
        )
    except Exception:
        error = True
    
    # Showing an error message
    if error:
        messages.error(
            request,
            u"<strong>Ouch.</strong> The city couldn't be "
            u"removeed. Please try again."
        )
    # Returning   
    return redirect('cities')

def region_new(request):
    """
    View that handles the process of adding a new region.
    """
    error = False
    # Processing data from POST
    if request.method == "POST":
        # Building the form
        form = RegionForm(request.POST)
        # Checking if the form is valid
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    '<strong>Success!</strong> A new region was created'
                )
                return redirect('regions')
            except Exception:
                error = True
        # The form is invalid
        else:
            error = True
        # Showing an error message
        if error:
            messages.error(
                request,
                u"<strong>Ouch.</strong> The region couldn't be "
                u"created. Please verify the data."
            )
    # No POST data: showing the empty form
    else:
        form = RegionForm()
    # Returning  
    return render(request, 'main/region_edit.html', {'form': form})

def region_edit(request, pk):
    """
    View that handles the process of editing a region.
    """
    error = False
    # Getting city from pk
    region = get_object_or_404(Region, pk=pk)
    # Processing data from POST
    if request.method == "POST":
        # Building the form using retrieved city
        form = RegionForm(request.POST, instance=region)
        # Checking if the form is valid
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    '<strong>Success!</strong> Region was edited'
                )
                return redirect('regions')
            except Exception:
                error = True
        # The form is invalid
        else:
            error = True
        # Showing an error message
        if error:
            messages.error(
                request,
                u"<strong>Ouch.</strong> The region couldn't be "
                u"modified. Please verify the data."
            )
    # No POST data: showing the form
    else:
        form = RegionForm(instance=region)
    # Returning   
    return render(request, 'main/region_edit.html', {'form': form})

def region_delete(request, pk):
    """
    View that handles the process of deleting a region.
    """
    error = False
    try:
        Region.objects.get(pk=pk).delete()
        messages.success(
            request,
            '<strong>Success!</strong> Region was removed'
        )
    except Exception:
        error = True
    
    # Showing an error message
    if error:
        messages.error(
            request,
            u"<strong>Ouch.</strong> The region couldn't be "
            u"removeed. Please try again."
        )
    # Returning   
    return redirect('regions')