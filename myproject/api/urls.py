from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_view, name='api'),
    path('orders/', views.orders_view, name='orders'),
    path('inventory/', views.inventory_view, name='inventory'),
]
