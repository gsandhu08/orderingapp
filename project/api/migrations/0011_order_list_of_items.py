# Generated by Django 3.2.9 on 2021-11-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='list_of_items',
            field=models.TextField(default=None, null=True),
        ),
    ]