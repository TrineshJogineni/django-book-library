from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_year', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Clean Code'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Robert C. Martin'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Technical'}),
            'published_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2008'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'e.g. 599.00'}),
        }