from django import forms
from django.forms import fields, widgets
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']
        labels = {'title': 'Enter your title', 
                    'text': 'Enter your text'}