from django.shortcuts import render
from .models import Animal, VolunteerOpportunity

def index(request):
    animals = Animal.objects.all().order_by('-created_at')
    opportunities = VolunteerOpportunity.objects.all().order_by('-created_at')
    
    context = {
        'animals': animals,
        'opportunities': opportunities,
    }
    return render(request, 'core/index.html', context)
