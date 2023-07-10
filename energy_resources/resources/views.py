import zipfile

import rest_framework.exceptions
from django.contrib.gis.db.backends.postgis.models import PostGISSpatialRefSys
from .exceptions import InvalidShapeFileError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework_gis.filters import InBBoxFilter
from .import_shapefile import import_shapefile
from .serializer import WindFarmSerializer, SolarPanelSerializer, ShapeFileWindFarmSerializer, \
    ShapeFileSolarPanelSerializer
from .models import *
from .file_methods import unzip_archive, find_shapefile
from .constans import WIND_FARM_FOLDER, SOLAR_PANELS_FOLDER, MAPPING_WIND_FARMS, MAPPING_SOLAR_PANEL


# Create your views here.


class WindFarmListAPIView(ListCreateAPIView):
    queryset = WindFarm.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = WindFarmSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, InBBoxFilter]
    bbox_filter_field = 'geometry'
    filterset_fields = ['entity', 'canton', 'zone']
    search_fields = ['city']

    def perform_create(self, serializer):
        serializer.save(last_user=self.request.user)


class WindFarmUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = WindFarm.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = WindFarmSerializer

    def perform_update(self, serializer):
        serializer.save(last_user=self.request.user)


class SolarPanelListAPIView(ListCreateAPIView):
    queryset = SolarPanel.objects.all()
    serializer_class = SolarPanelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [SearchFilter, DjangoFilterBackend, InBBoxFilter]
    bbox_filter_field = 'geometry'
    filterset_fields = ['entity', 'canton', 'zone']
    search_fields = ['city']

    def perform_create(self, serializer):
        serializer.save(last_user=self.request.user)


class SolarPanelUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SolarPanel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = SolarPanelSerializer

    def perform_update(self, serializer):
        serializer.save(last_user=self.request.user)


class ImportShapeFileWindFarmAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            if not 'shapefile' in request.FILES:
                return Response(data={'detail': 'Import shapefile is required'})
            else:
                shapefile = request.FILES['shapefile']
                if not zipfile.is_zipfile(shapefile):
                    raise InvalidShapeFileError('Uploaded file is not zip')

            srid = request.POST.get('srid')
            if not srid:
                return Response(data={'detail': 'Import SRID is required'})

            source_srid = PostGISSpatialRefSys.objects.get(srid=srid)
            folder_name = unzip_archive(shapefile, WIND_FARM_FOLDER)
            shapefile_path = find_shapefile(folder_name, WIND_FARM_FOLDER)
            import_shapefile(shapefile_path, self.request.user, MAPPING_WIND_FARMS, WindFarm, source_srid, WindFarmSerializer)
            return Response(status=status.HTTP_201_CREATED)
        except InvalidShapeFileError as e:
            return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except rest_framework.exceptions.ValidationError as e:
            return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class ImportShapeFileSolarPanelAPIView(CreateAPIView):
    queryset = SolarPanel.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ShapeFileSolarPanelSerializer

    def post(self, request):
        try:
            if not 'shapefile' in request.FILES:
                return Response(data={'detail': 'Import shapefile is required'})
            else:
                shapefile = request.FILES['shapefile']
                if not zipfile.is_zipfile(shapefile):
                    raise InvalidShapeFileError('Uploaded file is not zip')

            srid = request.POST.get('srid')
            if not srid:
                return Response(data={'detail': 'Import SRID is required'})

            source_srid = PostGISSpatialRefSys.objects.get(srid=srid)
            folder_name = unzip_archive(shapefile, SOLAR_PANELS_FOLDER)
            shapefile_path = find_shapefile(folder_name, SOLAR_PANELS_FOLDER)
            import_shapefile(shapefile_path, self.request.user, MAPPING_SOLAR_PANEL, SolarPanel, source_srid, SolarPanelSerializer)
            return Response(status=status.HTTP_201_CREATED)

        except InvalidShapeFileError as e:
            return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except rest_framework.exceptions.ValidationError as e:
            return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
