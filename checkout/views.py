from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contents import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error.request, "Your bag is empty"
        return redirect(reverse('products'))

    user_bag = bag_contents(request)
    total = user_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
        'stripe_public_key': 'pk_test_51H0qbCAyzNETnnX7lIUBptAAA6ElAnwIfIqHIdw6SxeVULCxlKSAnM9JesnorroRI3R8fqtCuANbgoa3zLbm6oMf00PxDyzu87',
    }

    return render(request, template, context)
