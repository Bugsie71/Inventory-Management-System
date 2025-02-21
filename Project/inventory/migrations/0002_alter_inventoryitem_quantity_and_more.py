# Generated by Django 5.0.7 on 2024-07-18 15:08

import django.core.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddConstraint(
            model_name='inventoryitem',
            constraint=models.CheckConstraint(check=models.Q(('quantity__gte', 0)), name='Quantity_Value_Valid', violation_error_message='Quantity invalid: cannot be less than 0'),
        ),
    ]
