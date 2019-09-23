from django.shortcuts import render, get_object_or_404

from webapp.forms import ProductSearch
from webapp.models import Product
from webapp.models import STATUS_CHOICES

def products_index_view(request, *args, **kwargs):
    if request.method == 'GET':
        products = Product.objects.all().order_by('category', 'name')
        form = ProductSearch()
        return render(request, 'index.html', context={
            'products' : products,
            'form' : form
        })
    elif (request.method == 'POST'):
        searched = request.POST.get('searched_value')
        form = ProductSearch()
        products = Product.objects.all().filter(name__icontains=searched).order_by('category', 'name')
        return render(request, 'index.html', context={
            'products': products ,
            'form': form
        })


def products_find_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })