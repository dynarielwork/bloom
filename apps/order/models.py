from django.db import models
from django.contrib.auth.models import User

from apps.store.models import Product
from apps.vendor.models import Vendor

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    ARRIVED = 'arrived'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (ARRIVED, 'Arrived')
    )

    user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    vendors = models.ManyToManyField(Vendor, related_name='orders')

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)
    used_coupon = models.CharField(max_length=50, blank=True, null=True)

    payment_intent = models.CharField(max_length=255)

    shipped_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return '%s' % self.first_name

    def get_total_quantity(self):
        return sum(int(item.quantity) for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.DO_NOTHING)
    vendor = models.ForeignKey(Vendor, related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    vendor_paid = models.BooleanField(default=False)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

    def get_total_price(self):
        return self.price * self.quantity


