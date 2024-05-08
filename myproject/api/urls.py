from django.urls import path
from . import views

urlpatterns = [
    path('feature/', views.feature_view, name='feature'),
]
