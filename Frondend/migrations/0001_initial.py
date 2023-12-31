# Generated by Django 3.2.10 on 2023-09-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(blank=True, max_length=20, null=True)),
                ('FullName', models.CharField(blank=True, max_length=20, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('ContactNumber', models.IntegerField(blank=True, null=True)),
                ('Password', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
