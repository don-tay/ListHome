from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from landlords.models import Landlord

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }
    
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all landlords
    landlords = Landlord.objects.order_by('-hire_date')

    # Get MVP landlord
    mvp_landlords = Landlord.objects.all().filter(is_mvp=True)

    context = {
        'landlords': landlords,
        'mvp_landlords': mvp_landlords
    }

    return render(request, 'pages/about.html', context)