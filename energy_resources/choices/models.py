from django.db import models
from django.utils.translation import gettext_lazy


# Create your models here.

class Entity(models.TextChoices):
    Republika_Srpska = ('RS', gettext_lazy('Republic of Srpska'))
    Federacija = ('FBiH', gettext_lazy('Federation of Bosnia and Herzegovina'))
    Brcko = ('BD', gettext_lazy('District Brcko'))


class Canton(models.TextChoices):
    Unsko_Sanski = ('USK', gettext_lazy('Una-Sana canton'))
    Posavski = ('PK', gettext_lazy('Posavina canton'))
    Tuzlanski = ('TK', gettext_lazy('Tuzla canton'))
    Zenicko_Dobojski = ('ZDK', gettext_lazy('Zenica-Doboj canton'))
    Bosansko_Podrinjski = ('BPK', gettext_lazy('Bosnian-Podrinje canton of Goražde'))
    Srednjobosanski = ('SBK', gettext_lazy('Central Bosnian Canton'))
    Hercegovacki = ('HNK', gettext_lazy('Herzegovina-Neretva Canton'))
    Zapadnohercegovacki = ('ZHK', gettext_lazy('West Herzegovina Canton'))
    Sarajevo = ('KS', gettext_lazy('Sarajevo Canton'))
    Deset = ('K10', gettext_lazy('Canton 10'))


class Zone(models.TextChoices):
    Urbana_zona = ('U', gettext_lazy('Urban'))
    Ruralna_zona = ('R', gettext_lazy('Rural'))
