from django.db.models.functions import Concat
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.gis.db.backends.postgis.models import PostGISSpatialRefSys
from .serializer import ModelSerializer,ProjectionSerializer
from .models import Entity, Canton, Zone
from django.db.models import Value,CharField

# Create your views here.

class ModelListAPIView(ListAPIView):
    serializer_class = (ModelSerializer)
    permission_classes = (AllowAny,)


class EntityListAPIView(ModelListAPIView):
    queryset = [{"code": item[0], "name": item[1]} for item in Entity.choices]


class CantonListAPIView(ModelListAPIView):
    queryset = [{"code": item[0], "name": item[1]} for item in Canton.choices]


class ZoneListAPIView(ModelListAPIView):
    queryset = [{"code": item[0], "name": item[1]} for item in Zone.choices]


class ProjectionListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PostGISSpatialRefSys.objects.annotate(
        srid_name=Concat('auth_name',Value(':'), 'auth_srid', output_field=CharField())
    )
    serializer_class = ProjectionSerializer
    filter_backends=[SearchFilter,]
    search_fields = ['srid_name',]
