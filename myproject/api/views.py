from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Product
from django.db.models import Q

# Create your views here.

# API Page View
@login_required
def api_view(request):
    return render(request, 'api.html')

# Orders View
@login_required
def orders_view(request):
    # Code to interact with Amazon SP-API and fetch data
    # Store the fetched data into your database
    orders = Order.objects.all()  # Assuming you have an Order model
    return render(request, 'api/orders.html', {'orders': orders})

# Inventory View
@login_required
def inventory_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'api/inventory.html', {'page_obj': page_obj})
