# Generated by Django 3.2.9 on 2021-11-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_restaurantlist_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlist',
            name='closing_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='restaurantlist',
            name='opening_time',
            field=models.TimeField(null=True),
        ),
    ]