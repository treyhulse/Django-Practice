from django.urls import path
from . import views
from .views import sales_performance

urlpatterns = [
    path('', sales_performance, name='sales_performance'),
]
