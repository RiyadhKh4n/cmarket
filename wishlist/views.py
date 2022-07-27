from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
    
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product 
from .models import FavouritesList


@login_required
def wishlist(request):
    """
    Display the user's profile and allows user to update
    information, view order history
    as well as letting a user add to favourites
    """

    try:
        favourites = FavouritesList.objects.filter(user=request.user.id)[0]
    except IndexError:
        fave = None
    else:
        fave = favourites.product.all()

    if not fave:
        messages.info(request, 'You have not added any items to your wishlist :(')

    template = 'wishlist/wishlist.html'
    context = {
        'fave': fave,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Function based view to show products
    added to favourites by user
    """
    product = get_object_or_404(Product, pk=product_id)
    try:
        favouritesList = get_object_or_404(FavouritesList,
                                           user=request.user.id)

    except Http404:
        favouritesList = FavouritesList.objects.create(user=request.user)
    if product in favouritesList.product.all():
        messages.info(request, 'Your wishlist '
                               'contains this product already!')
    else:
        favouritesList.product.add(product)
        messages.info(
            request, f'Added {product.name[:30]} to your Wishlist.'
        )
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def delete_from_wishlist(request, product_id):
    """ Delete a product from the store """
   
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product removed from Wishlist!')
    return redirect(reverse('wishlist'))