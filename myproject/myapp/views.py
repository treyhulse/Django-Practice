from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GondolaShelvingForm
from .models import GondolaShelving
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    context = {'message': "This is a dynamic message."}
    return render(request, 'index.html', context)

@login_required
def database(request):
    return render(request, 'database.html')

@login_required
def form(request):
    if request.method == 'POST':
        form = GondolaShelvingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form')  # Adjust the redirect as necessary
    else:
        form = GondolaShelvingForm()
    return render(request, 'form.html', {'form': form})

@login_required
def display_database(request):
    sort_by = request.GET.get('sort', 'date_added')  # Default sorting by date added
    order = request.GET.get('order', 'desc')
    if order == 'desc':
        sort_by = '-' + sort_by

    entries = GondolaShelving.objects.all().order_by(sort_by)
    return render(request, 'database.html', {'entries': entries})

@login_required
def display_parts(request):
    query = request.GET.get('q', '')  # Get the search term from the URL
    filter_by = request.GET.get('filter', '')  # Get the filter option from the URL

    # Basic QuerySet filtering based on search and additional filtering
    shelvings = GondolaShelving.objects.all()
    if query:
        shelvings = shelvings.filter(
            Q(configuration__icontains=query) | 
            Q(color__icontains=query) | 
            Q(height__icontains=query)
        )
    if filter_by:
        shelvings = shelvings.filter(configuration=filter_by)

    # Paginator setup
    paginator = Paginator(shelvings, 10)  # Show 10 shelvings per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'parts.html', {'page_obj': page_obj, 'query': query, 'filter_by': filter_by})
