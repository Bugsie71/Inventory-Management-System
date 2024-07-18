
from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, Inventory, Finance, AddItem, EditItem, DeleteItem, AddCategory, EditCategory, DeleteCategory, ManageCategory
from django.contrib.auth import views as authViews

urlpatterns = [
  path('', Index.as_view(), name='index'),
	path('signup/', SignUpView.as_view(), name='signup'),
	path('login/', authViews.LoginView.as_view(template_name='inventory/login.html'), name='login'),
	path('logout/', authViews.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
	path('inventory/', Inventory.as_view(), name='inventory'),
	path('dashboard/', Dashboard.as_view(), name='dashboard'),
	path('finance/', Finance.as_view(), name='finance'),
	path('inventory/add/', AddItem.as_view(), name='add-item'),
	path('inventory/delete/<int:pk>/', DeleteItem.as_view(), name='delete-item'),
	path('inventory/edit/<int:pk>/', EditItem.as_view(), name='edit-item'),
	path('manage-category/', ManageCategory.as_view(), name='manage-category'),
	path('manage-category/add/', AddCategory.as_view(), name='add-category'),
	path('manage-category/edit/<int:pk>/', EditCategory.as_view(), name='edit-category'),
	path('manage-category/delete/<int:pk>/', DeleteCategory.as_view(), name='delete-category'),
]
