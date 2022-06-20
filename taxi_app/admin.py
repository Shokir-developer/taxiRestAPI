from django.contrib import admin

from .models.customer import Customer
from .models.drivers import Driver
from .models.order import Order, OrderStatus, AcceptOrder

admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(AcceptOrder)
