from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from warehouses.forms import StorageLocationForm
from warehouses.models import StorageLocation


@login_required()
def address_create(request):
    if request.method == 'POST':
        new_address_form = StorageLocationForm(request.POST)

        if new_address_form.is_valid():
            new_address_form.save()
            return redirect('warehouses:address_list')

    else:
        new_address_form = StorageLocationForm()

    return render(request, 'address/address_form.html', {'new_address': new_address_form})


@login_required()
def address_list(request):
    address = StorageLocation.objects.order_by('address')
    context = {
        'address_list': address
        }

    return render(request, 'address/address_list.html', context=context)