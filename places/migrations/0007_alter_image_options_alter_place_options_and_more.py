# Generated by Django 4.1.2 on 2022-11-09 07:49

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_image_number_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number_img']},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
