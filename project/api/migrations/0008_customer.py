# Generated by Django 3.2.9 on 2021-11-25 06:55

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_menuitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('dob', models.DateTimeField()),
                ('mobile', phone_field.models.PhoneField(max_length=31)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]