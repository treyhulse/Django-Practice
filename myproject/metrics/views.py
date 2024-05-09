from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Sale

# Create your views here.
@login_required
def sales_performance(request):
    sales = Sale.objects.all()
    return render(request, 'metrics.html', {'sales': sales})
