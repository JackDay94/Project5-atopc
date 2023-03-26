from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    A view that renders the bag contents page.
    From CI Boutique Ado walkthrough.
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    A view to add a quantity of the specified product to the shopping bag.
    From CI Boutique Ado walkthrough.
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}'
            )
    else:
        bag[item_id] = quantity
        if quantity > 1:
            messages.success(
                request, f'Added {quantity} {product.name} to your bag'
            )
        else:
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    A view to adjust the quantity of the specified product to
    the specified amount.
    From CI Boutique Ado walkthrough.
    """

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
        messages.success(request, f'Removed {product.name} from your bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
