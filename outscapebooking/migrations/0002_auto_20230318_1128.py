# Generated by Django 3.2.18 on 2023-03-18 11:28

import django.core.validators
from django.db import migrations, models
import outscapebooking.models


class Migration(migrations.Migration):

    dependencies = [
        ('outscapebooking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookdate',
            field=models.DateField(help_text='[It is not possible to book the current day]', validators=[outscapebooking.models.Booking.validate_bookdate], verbose_name='The booking date*'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='comment',
            field=models.TextField(blank=True, max_length=300, verbose_name='Your comment'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Your email address*'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(max_length=80, verbose_name='Your first name*'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='last_name',
            field=models.CharField(max_length=80, verbose_name='Your last name*'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='mobile',
            field=models.CharField(help_text='[Indicate your country code]', max_length=14, verbose_name='Your phone number*'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='players',
            field=models.PositiveIntegerField(help_text="[You can't reserve for more than 10 players]", validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Number of players*'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='tickets',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Number of public transport tickets'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='timeslot',
            field=models.CharField(choices=[('10:00-13:00', '10:00-13:00'), ('11:00-14:00', '11:00-14:00'), ('12:00-15:00', '12:00-15:00'), ('13:00-16:00', '13:00-16:00'), ('14:00-17:00', '14:00-17:00'), ('15:00-18:00', '15:00-18:00'), ('16:00-19:00', '16:00-19:00')], help_text='[The game lasts for the duration of the slot]', max_length=40, verbose_name='Choose your time slot*'),
        ),
    ]