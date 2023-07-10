from django.contrib.gis.db import models
from users.models import UserData

from choices.models import Entity, Canton, Zone


class Resource(models.Model):
    class Meta:
        abstract = True

    owner = models.CharField(blank=True, null=True, max_length=50)
    manufactured = models.CharField(blank=True, null=True, max_length=50)
    note = models.CharField(blank=True, null=True, max_length=150)
    entity = models.CharField(choices=Entity.choices, max_length=4)
    canton = models.CharField(choices=Canton.choices, null=True, blank=True, max_length=4)
    city = models.CharField(max_length=50)
    zone = models.CharField(choices=Zone.choices, blank=True, null=True, max_length=1)
    elevation = models.DecimalField(max_digits=9, decimal_places=5)
    geometry = models.PointField(srid=4326, dim=2)

    last_user = models.ForeignKey(UserData, blank=True, null=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)


class SolarPanel(Resource):
    power_field = models.DecimalField(max_digits=9, decimal_places=5)
    panel_degree = models.DecimalField(max_digits=9, decimal_places=5, blank=True, null=True)
    document = models.FileField(blank=True, null=True, upload_to="solar_panel/")


class WindFarm(Resource):
    wind_direction = models.CharField(blank=True, null=True, max_length=50)
    power_energy = models.DecimalField(max_digits=9, decimal_places=5)
    document = models.FileField(blank=True, null=True, upload_to="wind_farm/")
