from django.db import models
from enum import Enum

class Status(Enum):
    ACTIVE = 'A'
    INACTIVE = 'I'

class City(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=[(status.value, status.name) for status in Status])

    class Meta:
        ordering = ('status','name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Remove region assocciations when status is changed to Inactive
        if self.pk and self.status == Status.INACTIVE.value:
            self.region_set.clear()
        super().save(*args, **kwargs)

class Region(models.Model):
    name = models.CharField(max_length=100)
    cities = models.ManyToManyField(City, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
