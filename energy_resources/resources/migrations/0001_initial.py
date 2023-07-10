# Generated by Django 4.1.7 on 2023-03-20 13:31

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WindFarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=50, null=True)),
                ('manufactured', models.CharField(blank=True, max_length=50, null=True)),
                ('note', models.CharField(blank=True, max_length=150, null=True)),
                ('entity', models.CharField(choices=[('RS', 'Republika Srpska'), ('FBiH', 'Federacija Bosne i Hercegovine'), ('BD', 'Brčko Distrikt')], max_length=4)),
                ('canton', models.CharField(choices=[('USK', 'Unsko-sanski kanton'), ('PK', 'Posavski kanton'), ('TK', 'Tuzlanski kanton'), ('ZDK', 'Zeničko-dobojski kanton'), ('BPK', 'Bosansko-podrinjski kanton Goražde'), ('SBK', 'Srednjobosanski kanton'), ('HNK', 'Hercegovačko-neretvanski kanton'), ('ZHK', 'Zapadnohercegovački kanton'), ('KS', 'Kanton Sarajevo'), ('K10', 'Kanton 10')], max_length=3)),
                ('city', models.CharField(max_length=50)),
                ('zone', models.CharField(blank=True, choices=[('U', 'Urbana'), ('R', 'Ruralna')], max_length=1, null=True)),
                ('elevation', models.DecimalField(decimal_places=5, max_digits=9)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('wind_direction', models.CharField(blank=True, max_length=50, null=True)),
                ('power_energy', models.DecimalField(decimal_places=5, max_digits=9)),
                ('document', models.FileField(blank=True, null=True, upload_to='wind_farm/')),
                ('last_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SolarPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=50, null=True)),
                ('manufactured', models.CharField(blank=True, max_length=50, null=True)),
                ('note', models.CharField(blank=True, max_length=150, null=True)),
                ('entity', models.CharField(choices=[('RS', 'Republika Srpska'), ('FBiH', 'Federacija Bosne i Hercegovine'), ('BD', 'Brčko Distrikt')], max_length=4)),
                ('canton', models.CharField(choices=[('USK', 'Unsko-sanski kanton'), ('PK', 'Posavski kanton'), ('TK', 'Tuzlanski kanton'), ('ZDK', 'Zeničko-dobojski kanton'), ('BPK', 'Bosansko-podrinjski kanton Goražde'), ('SBK', 'Srednjobosanski kanton'), ('HNK', 'Hercegovačko-neretvanski kanton'), ('ZHK', 'Zapadnohercegovački kanton'), ('KS', 'Kanton Sarajevo'), ('K10', 'Kanton 10')], max_length=3)),
                ('city', models.CharField(max_length=50)),
                ('zone', models.CharField(blank=True, choices=[('U', 'Urbana'), ('R', 'Ruralna')], max_length=1, null=True)),
                ('elevation', models.DecimalField(decimal_places=5, max_digits=9)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('power_field', models.DecimalField(decimal_places=5, max_digits=9)),
                ('panel_degree', models.DecimalField(blank=True, decimal_places=5, max_digits=9, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='solar_panel/')),
                ('last_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]