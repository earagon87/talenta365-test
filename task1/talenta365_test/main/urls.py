from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("cities/", views.cities, name="cities"),
    path("regions/", views.regions, name="regions"),
    path('city/new', views.city_new, name='city_new'),
    path('city/<int:pk>/edit/', views.city_edit, name='city_edit'),
    path('city/<int:pk>/delete/', views.city_delete, name='city_delete'),
    path('region/new', views.region_new, name='region_new'),
    path('region/<int:pk>/edit/', views.region_edit, name='region_edit'),
    path('region/<int:pk>/delete/', views.region_delete, name='region_delete'),

]