from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GondolaShelvingForm
from .models import GondolaShelving

# Create your views here.

def home(request):
    context = {'message': "This is a dynamic message."}
    return render(request, 'index.html', context)

def database(request):
    return render(request, 'database.html')

def form(request):
    if request.method == 'POST':
        form = GondolaShelvingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form')  # Adjust the redirect as necessary
    else:
        form = GondolaShelvingForm()
    return render(request, 'form.html', {'form': form})

def display_database(request):
    sort_by = request.GET.get('sort', 'date_added')  # Default sorting by date added
    order = request.GET.get('order', 'desc')
    if order == 'desc':
        sort_by = '-' + sort_by

    entries = GondolaShelving.objects.all().order_by(sort_by)
    return render(request, 'database.html', {'entries': entries})