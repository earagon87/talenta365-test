from django import forms

from .models import City, Region, Status

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name', 'status')

class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = ('name', 'cities')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cities'].queryset = City.objects.exclude(status=Status.INACTIVE.value)