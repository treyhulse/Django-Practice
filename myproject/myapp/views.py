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
            return redirect('form')  # Redirect to a new URL if you want
    else:
        form = GondolaShelvingForm()
    return render(request, 'form.html', {'form': form})

def display_database(request):
    # Fetch all entries from GondolaShelving model
    entries = GondolaShelving.objects.all()
    return render(request, 'database.html', {'entries': entries})