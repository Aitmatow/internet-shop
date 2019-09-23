from django.shortcuts import render

from webapp.models import Product
from webapp.models import STATUS_CHOICES

def products_index_view(request, *args, **kwargs):
    products = Product.objects.all()
    return render(request, 'index.html', context={
        'products' : products
    })
