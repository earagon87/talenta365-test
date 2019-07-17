from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("cities/", views.cities, name="cities"),
    path("regions/", views.regions, name="regions"),
    path('city/new', views.city_new, name='city_new'),
    path('region/new', views.region_new, name='region_new'),

]