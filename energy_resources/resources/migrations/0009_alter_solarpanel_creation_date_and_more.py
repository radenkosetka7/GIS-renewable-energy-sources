# Generated by Django 4.1.7 on 2023-04-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_alter_solarpanel_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarpanel',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='windfarm',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
