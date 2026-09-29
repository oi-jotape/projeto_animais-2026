from django.contrib import admin
from .models import Animal, VolunteerOpportunity, VolunteerSubscription, AdoptionRequest

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'created_at')

@admin.register(VolunteerOpportunity)
class VolunteerOpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'schedule', 'created_at')

@admin.register(VolunteerSubscription)
class VolunteerSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'opportunity', 'created_at')
    list_filter = ('opportunity',)

@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal', 'status', 'created_at')
    list_filter = ('status', 'animal')
    search_fields = ('name', 'email')
