# Generated by Django 3.2.4 on 2021-07-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_hall_hall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='hall',
            field=models.CharField(max_length=100, unique=True, verbose_name='hall'),
        ),
    ]
