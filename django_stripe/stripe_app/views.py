from django.shortcuts import render
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from stripe_app.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


# def buy_item(request, item_id):
#     item = Item.objects.get(id=item_id)
#     DOMAIN = "http://127.0.0.1:8000"
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=[{
#             'price_data': {
#                 'currency': item.currency,
#                 'product_data': {
#                     'name': item.name,
#                 },
#                 'unit_amount': int(item.price * 100),
#             },
#             'quantity': 1,
#         }],
#         mode='payment',
#         success_url=DOMAIN + '/success/',
#         cancel_url=DOMAIN + '/cancel/',
#     )
#     return JsonResponse({'session_id': session.id})

def buy_item(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(id=item_id)
        amount = int(item.price * 100)
        currency = item.currency
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency
        )
        return JsonResponse({'client_secret': payment_intent.client_secret})


def get_item_page(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'stripe_app/item_page.html', context=context)


