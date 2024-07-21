from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.constraints import CheckConstraint
from django.db.models import Q


class InventoryItem(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
	price_per_unit = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[MinValueValidator(0.0)]
  )
	quantity = models.PositiveSmallIntegerField(
		validators=[MinValueValidator(0)]
	)
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta():
		constraints = [
			models.CheckConstraint(
				name='quantity_value_valid',
				check=Q(quantity__gte=0),
				violation_error_message='Quantity invalid: cannot be less than 0'
			),

			models.CheckConstraint(
				name='price_value_valid',
				check=Q(price_per_unit__gte=0),
				violation_error_message='Price invalid: cannot be less than 0'
			)
		]

class Category(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	verbose_name = 'category'
	verbose_name_plural = 'categories'

	def __str__(self):
		return self.name