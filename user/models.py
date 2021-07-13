"""
Implemented Profile of User models
"""
from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

from films.validators import positive_validator


class Cash(models.Model):
    pid = models.AutoField(primary_key=True)
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00,
                                 validators=[positive_validator])
    username = models.OneToOneField("auth.User", on_delete=models.CASCADE)



