from django.urls import path

from .views import EntityListAPIView, CantonListAPIView, ZoneListAPIView, ProjectionListAPIView

urlpatterns = [
    path('entites/', EntityListAPIView.as_view(), name='entites'),
    path('cantons/', CantonListAPIView.as_view(), name='cantons'),
    path('zones/', ZoneListAPIView.as_view(), name='zones'),
    path('projections/', ProjectionListAPIView.as_view(), name='projections')

]
