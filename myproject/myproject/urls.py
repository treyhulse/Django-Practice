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
from django.contrib.auth import views as auth_views
from django.urls import include, path
from myapp.views import home, form, database, display_database, display_parts
from api.views import api_view, orders_view, inventory_view
from metrics.views import sales_performance
from django.conf import settings
from django.conf.urls.static import static

#URL Patterns Here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Set the home view as the index page
    path('form/', form, name='form'),
    path('database/', display_database, name='database'),  # URL for the database page
    path('api/', include('api.urls')),
    path('metrics/', include('metrics.urls')),
    path('sales_performance/', sales_performance, name='sales_performance'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('parts/', display_parts, name='display-parts'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)