from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, InventoryItem
from django.core.validators import MinValueValidator

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class InventoryItemForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
	price_per_unit = forms.DecimalField(
		max_digits=10,
		decimal_places=2,
		validators=[MinValueValidator(0.0)],
		label="Price Per Unit"
	)
	class Meta:
		model = InventoryItem
		fields = ['name', 'category', 'quantity', 'price_per_unit']

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']