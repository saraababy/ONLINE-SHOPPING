# Generated by Django 3.2.10 on 2023-09-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frondend', '0002_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='ProImages'),
        ),
    ]
