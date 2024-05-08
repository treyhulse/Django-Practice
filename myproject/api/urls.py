from django.urls import path
from . import views
from .views import feature_view

urlpatterns = [
    path('', feature_view, name='api_feature'),
    ]
