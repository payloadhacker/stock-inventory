from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('stocks/', views.list_stock, name='list_stock'),
    path('edit/<int:pk>/', views.edit_stock, name='edit_stock'),
    path('delete/<int:pk>/', views.delete_stock, name='delete_stock'),
]
