from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product


@login_required
def wishlist(request):
    """
    A view to show the user wishlist.
    """
    user = request.user
    wishlist = user.wishlist.all()

    context = {
        'wishlist_item': wishlist
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_remove_wishlist(request, product_id):
    """
    A view to add or remove a product from the wishlist.
    Code edited from: https://www.youtube.com/@veryacademy
    """
    product = get_object_or_404(Product, pk=product_id)

    if product.wishlist.filter(id=request.user.id).exists():
        product.wishlist.remove(request.user)
        messages.success(
            request, f'Removed {product.name} from your WishList!')
    else:
        product.wishlist.add(request.user)
        messages.success(request, f'Added {product.name} to your WishList!')

    return redirect(reverse('product_detail', args=[product.id]))
