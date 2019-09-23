from django.shortcuts import render, get_object_or_404

from webapp.models import Product
from webapp.models import STATUS_CHOICES

def products_index_view(request, *args, **kwargs):
    products = Product.objects.all().order_by('category', 'name')
    return render(request, 'index.html', context={
        'products' : products
    })


def products_find_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })