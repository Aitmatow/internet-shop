from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class ProductSearch(forms.Form):
    searched_value = forms.CharField(max_length=200, required=True, label='Поиск ')

