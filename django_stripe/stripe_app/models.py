from django.db import models

class Item(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f} {1}".format(self.price / 100, self.get_currency_display())

class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id}'

class PaymentModifier(models.Model):
    ORDER_TYPE_CHOICES = (
        ('D', 'Discount'),
        ('T', 'Tax'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    modifier_type = models.CharField(max_length=1, choices=ORDER_TYPE_CHOICES)

    def __str__(self):
        return f'{self.get_modifier_type_display()}: {self.amount}'
