# Generated by Django 4.1.7 on 2023-03-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_canton_entity_zone_alter_solarpanel_canton_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarpanel',
            name='canton',
            field=models.CharField(blank=True, choices=[('USK', 'Unsko-sanski kanton'), ('PK', 'Posavski kanton'), ('TK', 'Tuzlanski kanton'), ('ZDK', 'Zeničko-dobojski kanton'), ('BPK', 'Bosansko-podrinjski kanton Goražde'), ('SBK', 'Srednjobosanski kanton'), ('HNK', 'Hercegovačko-neretvanski kanton'), ('ZHK', 'Zapadnohercegovački kanton'), ('KS', 'Kanton Sarajevo'), ('K10', 'Kanton 10')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republika Srpska'), ('FBiH', 'Federacija Bosne i Hercegovine'), ('BD', 'Brčko Distrikt')], max_length=25),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='zone',
            field=models.CharField(blank=True, choices=[('U', 'Urbana'), ('R', 'Ruralna')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='windfarm',
            name='canton',
            field=models.CharField(blank=True, choices=[('USK', 'Unsko-sanski kanton'), ('PK', 'Posavski kanton'), ('TK', 'Tuzlanski kanton'), ('ZDK', 'Zeničko-dobojski kanton'), ('BPK', 'Bosansko-podrinjski kanton Goražde'), ('SBK', 'Srednjobosanski kanton'), ('HNK', 'Hercegovačko-neretvanski kanton'), ('ZHK', 'Zapadnohercegovački kanton'), ('KS', 'Kanton Sarajevo'), ('K10', 'Kanton 10')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='windfarm',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republika Srpska'), ('FBiH', 'Federacija Bosne i Hercegovine'), ('BD', 'Brčko Distrikt')], max_length=25),
        ),
        migrations.AlterField(
            model_name='windfarm',
            name='zone',
            field=models.CharField(blank=True, choices=[('U', 'Urbana'), ('R', 'Ruralna')], max_length=25, null=True),
        ),
        migrations.DeleteModel(
            name='Canton',
        ),
        migrations.DeleteModel(
            name='Entity',
        ),
        migrations.DeleteModel(
            name='Zone',
        ),
    ]