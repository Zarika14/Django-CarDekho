# Generated by Django 5.0.4 on 2024-04-09 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarDekho', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carlist',
            old_name='status',
            new_name='active',
        ),
    ]
