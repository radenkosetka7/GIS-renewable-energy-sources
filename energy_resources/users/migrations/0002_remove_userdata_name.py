# Generated by Django 4.1.7 on 2023-03-13 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='name',
        ),
    ]
