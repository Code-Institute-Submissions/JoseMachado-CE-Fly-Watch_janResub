from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product

# Create your views here.

"""Function to view bag"""
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


"""Function to add products to bag"""
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id] = quantity
        messages.success(
            request, f"Updated {product.name} quantity to {bag[item_id]}"
        )
    else:
        bag[item_id] = quantity
        messages.success(request, f"Added {product.name} to your bag")

    request.session["bag"] = bag
    return redirect(redirect_url)


"""Function to update the bag"""
def adjust_bag(request, item_id):
    """ Make the quantity of certain product correct """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}'
        )
    else:
        bag.pop(item_id)
        messages.success(
            request, f'Removed {product.name} watch from your bag'
        )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


"""Function to remove products from the bag"""
def remove_item_from_bag(request, item_id):
    """ Make the quantity of certain product correct """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(
            request, f'Removed {product.name} watch from your bag'
        )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
        messages.error(request, f'It was not possible to remove item: {e}')
