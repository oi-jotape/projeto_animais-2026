from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Animal, VolunteerOpportunity, AdoptionRequest, VolunteerSubscription
from .forms import VolunteerSubscriptionForm, AdoptionRequestForm

def index(request):
    animals = Animal.objects.all().order_by('-created_at')
    opportunities = VolunteerOpportunity.objects.all().order_by('-created_at')
    
    context = {
        'animals': animals,
        'opportunities': opportunities,
    }
    return render(request, 'core/index.html', context)

def volunteer_subscribe(request, pk):
    opportunity = get_object_or_404(VolunteerOpportunity, pk=pk)
    if request.method == 'POST':
        form = VolunteerSubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.opportunity = opportunity
            subscription.save()
            messages.success(request, f'Sua inscrição para a vaga "{opportunity.title}" foi realizada com sucesso! Entraremos em contato.')
            return redirect('core:index')
    else:
        form = VolunteerSubscriptionForm()

    context = {
        'opportunity': opportunity,
        'form': form,
    }
    return render(request, 'core/subscribe.html', context)

def animal_adopt(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption = form.save(commit=False)
            adoption.animal = animal
            adoption.save()
            messages.success(request, f'Seu pedido de adoção para {animal.name} foi enviado! Nossa equipe analisará e entrará em contato.')
            return redirect('core:index')
    else:
        form = AdoptionRequestForm()
    context = {
        'animal': animal,
        'form': form,
    }
    return render(request, 'core/adopt.html', context)

@login_required
def dashboard(request):
    adoptions = AdoptionRequest.objects.all().order_by('-created_at')
    volunteers = VolunteerSubscription.objects.all().order_by('-created_at')
    
    context = {
        'adoptions': adoptions,
        'volunteers': volunteers,
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def update_adoption_status(request, pk, status):
    adoption = get_object_or_404(AdoptionRequest, pk=pk)
    if status in ['Aprovado', 'Rejeitado', 'Pendente']:
        adoption.status = status
        adoption.save()
        messages.success(request, f'Status do pedido de adoção de {adoption.name} atualizado para {status}.')
    return redirect('core:dashboard')

@login_required
def update_volunteer_status(request, pk, status):
    subscription = get_object_or_404(VolunteerSubscription, pk=pk)
    if status in ['Aprovado', 'Rejeitado', 'Pendente']:
        subscription.status = status
        subscription.save()
        messages.success(request, f'Status da inscrição de voluntário de {subscription.name} atualizado para {status}.')
    return redirect('core:dashboard')
