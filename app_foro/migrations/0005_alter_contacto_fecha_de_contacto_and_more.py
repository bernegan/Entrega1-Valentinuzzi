# Generated by Django 4.0.4 on 2022-05-31 23:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foro', '0004_alter_contacto_fecha_de_contacto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='fecha_de_contacto',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 20, 51, 6, 49295)),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_de_publicacion',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 20, 51, 6, 8258)),
        ),
    ]
