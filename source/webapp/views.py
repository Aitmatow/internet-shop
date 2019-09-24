from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ProductSearch, ProductsForm
from webapp.models import Product, STATUS_CHOICES


def products_index_view(request, *args, **kwargs):
    if request.method == 'GET':
        products = Product.objects.all().order_by('category')
        form = ProductSearch()
        return render(request, 'index.html', context={
            'products' : products,
            'form' : form,
            'category' : STATUS_CHOICES,
            'is_category' : False,
        })
    elif (request.method == 'POST'):
        searched = request.POST.get('searched_value')
        form = ProductSearch()
        products = Product.objects.all().filter(name__icontains=searched).order_by('category')
        return render(request, 'index.html', context={
            'products': products ,
            'form': form,
            'category': STATUS_CHOICES,
            'is_category' : False,
        })

def products_category_view(request, category):
    for i in STATUS_CHOICES:
        if category == i[0]:
            cur_category = i[1]
    products = Product.objects.all().filter(category=category).order_by('name')
    form = ProductSearch()
    return render(request, 'index.html', context={
        'products' : products,
        'form' : form,
        'category': STATUS_CHOICES,
        'is_category' : True,
        'cur_category' : cur_category
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


def products_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductsForm(data={
            'name' : product.name,
            'description' : product.description,
            'category' : product.category,
            'balance' : product.balance,
            'price' : product.price,
        })
        return render(request, 'update.html' , context={
            'form' : form,
            'product':product
        })
    elif request.method == 'POST':
        form = ProductsForm(data = request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.balance = form.cleaned_data['balance']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('product_view', pk = product.pk)
        else:
            return render(request, 'update.html', context={'form':form,
            'product':product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('index')