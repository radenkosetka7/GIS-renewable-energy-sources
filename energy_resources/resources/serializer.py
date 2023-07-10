from django.utils.translation import gettext_lazy
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import SolarPanel
from .models import WindFarm


def validate_canton(value=None, entity=None, instance=None):
    err_msg1 = gettext_lazy("Field canton is mandatory for the entity Federation of Bosnia and Herzegovina.")
    err_msg2 = gettext_lazy("Field canton can not be selected for Republic of Serbs or District Brcko.")
    err_msg3 = gettext_lazy("It is not possible to change entity field, canton field is already selected.")
    if entity and entity == 'FBiH' and not value:
        raise serializers.ValidationError(err_msg1)
    elif entity and entity in ['RS', 'BD'] and value:
        raise serializers.ValidationError(err_msg2)
    elif value and instance and not entity and instance.entity != 'FBiH':
        raise serializers.ValidationError(err_msg2)
    elif entity and entity in ['RS', 'BD'] and instance and value is not None and instance.canton:
        raise serializers.ValidationError(err_msg3)
    elif entity and entity in ['RS', 'BD'] and instance and value is None and instance.canton:
        return value

    return value


class WindFarmSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WindFarm
        geo_field = "geometry"
        fields = ('id', 'owner', 'manufactured', 'note', 'entity', 'canton', 'city', 'zone', 'elevation',
                  'wind_direction', 'power_energy', 'document')

    def validate(self, data):
        data = super().validate(data)
        validate_canton(data.get('canton'), data.get('entity'), self.instance)
        return data


class SolarPanelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SolarPanel
        geo_field = "geometry"
        fields = ('id', 'owner', 'manufactured', 'note', 'entity', 'canton', 'city', 'zone', 'elevation',
                  'panel_degree', 'power_field', 'document')

    def validate(self, data):
        data = super().validate(data)
        validate_canton(data.get('canton'), data.get('entity'), self.instance)
        return data


class ShapeFileSerializer(serializers.ModelSerializer):
    shapefile = serializers.FileField()
    srid = serializers.IntegerField()


class ShapeFileWindFarmSerializer(ShapeFileSerializer):
    class Meta:
        model = WindFarm
        fields = ('shapefile', 'srid')


class ShapeFileSolarPanelSerializer(ShapeFileSerializer):
    class Meta:
        model = SolarPanel
        fields = ('shapefile', 'srid')
