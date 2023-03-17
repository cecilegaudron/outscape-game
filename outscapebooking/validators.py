from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now
from datetime import date


def validate_bookdate(value):
        # Validate the booking if the booked date is before today
        # https://stackoverflow.com/questions/66882721/how-to-add-todays-date-to-django-templates
        # https://stackoverflow.com/questions/50439356/django-date-validation-help-needed
        # https://docs.djangoproject.com/en/4.1/ref/validators/
        # Help in Slack
        today = now().date()
        if value <= today:
            raise ValidationError("The date cannot be in the past!")
