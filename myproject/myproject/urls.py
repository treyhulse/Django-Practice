"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from myapp.views import home, form, database, display_database 
from api.views import feature_view

#URL Patterns Here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Set the home view as the index page
    path('form/', form, name='form'),
    path('database/', display_database, name='database'),  # URL for the database page
    path('api/', include('api.urls')),
    ]
