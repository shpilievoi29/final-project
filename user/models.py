from django.db import models

from films.validators import positive_validator


class Profile(models.Model):
    pid = models.AutoField(primary_key=True)
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=100_000.00,
                                 validators=[positive_validator])
    username = models.OneToOneField("auth.User", on_delete=models.CASCADE)
