from django import forms
from .models import VolunteerSubscription, AdoptionRequest

class VolunteerSubscriptionForm(forms.ModelForm):
    class Meta:
        model = VolunteerSubscription
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu melhor e-mail'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 99999-9999'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Conte um pouco sobre por que quer ser voluntário (Opcional)'}),
        }

class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['name', 'email', 'phone', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu melhor e-mail'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 99999-9999'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Por que sua casa é o melhor lugar para ele?'}),
        }
