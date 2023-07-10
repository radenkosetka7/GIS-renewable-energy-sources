from rest_framework import serializers
from django.contrib.gis.db.backends.postgis.models import PostGISSpatialRefSys


class ModelSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)
    name = serializers.CharField(max_length=25)

    class Meta:
        fields = ('code', 'name')


class ProjectionSerializer(serializers.ModelSerializer):
    srid_name = serializers.CharField()

    class Meta:
        model = PostGISSpatialRefSys
        fields = ('srid', 'srid_name')
        read_only_fields = ('srid', 'srid_name',)
