from django.urls import path
from .views import WindFarmListAPIView, WindFarmUpdateDeleteAPIView, SolarPanelListAPIView, \
    SolarPanelUpdateDeleteAPIView, ImportShapeFileWindFarmAPIView, ImportShapeFileSolarPanelAPIView

urlpatterns = [
    path('wind_farms/', WindFarmListAPIView.as_view(), name='create_wind_farm'),
    path('wind_farms/<int:pk>', WindFarmUpdateDeleteAPIView.as_view(), name='wind_farm_update_delete'),
    path('solar_panels/<int:pk>', SolarPanelUpdateDeleteAPIView.as_view(), name='solar-panel-update_delete'),
    path('solar_panels/', SolarPanelListAPIView.as_view(), name='solar-panel-create'),
    path('import_shape_file/wind_farms/', ImportShapeFileWindFarmAPIView.as_view(), name='import_shape_file_wind_farm'),
    path('import_shape_file/solar_panels/', ImportShapeFileSolarPanelAPIView.as_view(),
         name='import_shape_file_solar_panel'),
]
