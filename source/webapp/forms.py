from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES, DEFAULT_STATUS
from webapp.models import Product


class ProductSearch(forms.Form):
    searched_value = forms.CharField(max_length=200, required=True, label='Поиск ')

class ProductsForm(forms.Form):
    name = forms.CharField(required=True, label='Наименование товара')
    description = forms.CharField(required=False,max_length=2000, label='Описание', widget=widgets.Textarea)
    category = forms.ChoiceField(required=False,label='Категория', choices=STATUS_CHOICES)
    balance = forms.IntegerField(label='Остаток', min_value=0)
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')
