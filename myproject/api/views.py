from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Product

# Create your views here.
def feature_view(request):
    product_list = Product.objects.all().prefetch_related('inventory')
    paginator = Paginator(product_list, 10)  # Show 10 products per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'api.html', {'page_obj': page_obj})