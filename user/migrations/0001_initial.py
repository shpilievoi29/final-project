# Generated by Django 3.2.4 on 2021-07-02 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import films.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('wallet', models.DecimalField(decimal_places=2, default=100000.0, max_digits=10, validators=[films.validators.positive_validator])),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
