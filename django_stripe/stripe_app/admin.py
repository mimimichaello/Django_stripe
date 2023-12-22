from django.contrib import admin
from stripe_app.models import Item, PaymentModifier, Order

admin.site.register(Item)
admin.site.register(PaymentModifier)
admin.site.register(Order)
