# Generated by Django 3.2.10 on 2023-09-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_auto_20230912_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImages'),
        ),
        migrations.AddField(
            model_name='productdb',
            name='Image1',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImages'),
        ),
        migrations.AddField(
            model_name='productdb',
            name='Image2',
            field=models.ImageField(blank=True, null=True, upload_to='ProductImages'),
        ),
    ]