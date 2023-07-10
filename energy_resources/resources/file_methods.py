from zipfile import ZipFile
import os.path
from django.conf import settings
from django.utils.translation import gettext_lazy

from .exceptions import InvalidShapeFileError


def validate_required_shapefile_components(shapefile_list):
    required_extensions = ['.shx', '.dbf', '.shp']
    imported_extensions = []
    for file in shapefile_list:
        name, extension = os.path.splitext(file)
        imported_extensions.append(extension)
    if set(required_extensions).issubset(set(imported_extensions)):
        return True
    return False


def unzip_archive(shapefile, wind_farm_folder):
    with ZipFile(shapefile, 'r') as zipFarm:
        if not validate_required_shapefile_components(zipFarm.namelist()):
            raise InvalidShapeFileError(gettext_lazy("Shapefile does not contain required components."))

        folder_name = os.path.splitext(os.path.basename(shapefile.name))[0]
        zipFarm.extractall(f'{settings.MEDIA_ROOT}/{wind_farm_folder}/{folder_name}/')
        return folder_name


def find_shapefile(folder_name, wind_farm_folder):
    try:
        for file_name in os.listdir(f'{settings.MEDIA_ROOT}/{wind_farm_folder}/{folder_name}'):
            if os.path.splitext(file_name)[1] == '.shp':
                shapefile_path = f'{settings.MEDIA_ROOT}/{wind_farm_folder}/{folder_name}/{file_name}'
                return shapefile_path
    except:
        InvalidShapeFileError(gettext_lazy("It is impossible to find shapefile (.shp)."))
