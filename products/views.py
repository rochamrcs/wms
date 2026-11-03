from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product


@login_required()
def product_create(request):
    if request.method == 'POST':
        new_product_form = ProductForm(request.POST)

        if new_product_form.is_valid():
            new_product_form.save()
            return redirect('products:product_list')
    else:
        new_product_form = ProductForm()

    return render(request, 'products/product_form.html', {
        'new_product': new_product_form,
    })


@login_required()
def product_list(request):
    products = Product.objects.order_by('code')
    context = {
        'product_list': products
        }

    return render(request, 'products/product_list.html', context=context)