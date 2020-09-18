from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['message', 'name', 'email', 'subject']
        widgets = {



            'message': forms.Textarea(attrs={"class": 'form-control', 'placeholder': 'message'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'subject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'subject'})

        }
