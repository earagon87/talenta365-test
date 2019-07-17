from django.db import models

class City(models.Model):
    STATUSES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUSES)

    class Meta:
        ordering = ('status','name')

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    cities = models.ManyToManyField(City)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
