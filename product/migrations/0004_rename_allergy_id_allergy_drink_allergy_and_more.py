# Generated by Django 4.0.1 on 2022-01-07 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_image_drink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allergy_drink',
            old_name='allergy_id',
            new_name='allergy',
        ),
        migrations.RenameField(
            model_name='allergy_drink',
            old_name='drink_id',
            new_name='drink',
        ),
    ]
