# Generated by Django 3.2.10 on 2023-09-12 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_auto_20230912_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdb',
            old_name='Image3',
            new_name='Image',
        ),
    ]
