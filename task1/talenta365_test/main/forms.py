from django import forms

from .models import City, Region

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name', 'status')

class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = ('name', 'cities')