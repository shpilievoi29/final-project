# Generated by Django 3.2.4 on 2021-07-04 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('film_name', models.CharField(help_text='255 characters or fever', max_length=255, verbose_name='a name title')),
                ('film_description', models.CharField(max_length=1000, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/media/')),
                ('slug', models.SlugField(help_text='letters, hyphens, numbers and underscores', max_length=255)),
                ('category', models.ForeignKey(db_column='category', null=True, on_delete=django.db.models.deletion.CASCADE, to='films.category')),
            ],
        ),
        migrations.CreateModel(
            name='FilmSession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('time_start', models.TimeField(blank=True, db_column='start time sessions')),
                ('time_finish', models.TimeField(blank=True, db_column='finish time sessions')),
                ('hall', models.PositiveSmallIntegerField(choices=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], default=5, verbose_name='hall choices')),
                ('places', models.IntegerField(default=50)),
                ('film_name', models.ForeignKey(db_column='title', null=True, on_delete=django.db.models.deletion.CASCADE, to='films.film')),
            ],
        ),
    ]
