from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ProductSearch, ProductsForm
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


def product_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductsForm()
        return render(request, 'create.html' , context={
            'form' : form
        })
    elif request.method == 'POST':
        form = ProductsForm(data = request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                category= form.cleaned_data['category'],
                balance= form.cleaned_data['balance'],
                price= form.cleaned_data['price']
            )
            return redirect('product_view', pk = product.pk)
        else:
            return render(request, 'create.html', context={'form':form})