# Generated by Django 3.2.9 on 2021-12-03 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_restmenuitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlist',
            name='menu_list',
        ),
    ]
