from django.core.exceptions import ValidationError


def positive_validator(value):
    if value < 0.00:
        raise ValidationError("Should be positive or zero")

    return value
