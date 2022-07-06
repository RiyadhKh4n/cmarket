
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KxwDcJKTNleUfw8PLnyHlnP1Qt8fCRNL2xAX3LmzrfsaSYLlRaQkDmSsXoehuGDlLodwqhd01kzxr7hBT75xGEA004QHfDlck',
        'client_secret': 'this_is_secret_key',
    }

    return render(request, template, context)