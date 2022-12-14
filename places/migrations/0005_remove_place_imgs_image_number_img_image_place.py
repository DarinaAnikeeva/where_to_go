# Generated by Django 4.1.2 on 2022-11-05 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_place_imgs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='imgs',
        ),
        migrations.AddField(
            model_name='image',
            name='number_img',
            field=models.ImageField(blank=True, default=1, upload_to=''),
        ),
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.place'),
        ),
    ]
