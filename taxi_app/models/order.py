from django.db import models
from .customer import Customer
from .drivers import Driver


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	update_at = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.customer)

class OrderStatus(models.Model):
	status = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.status

class AcceptOrder(models.Model):
	driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	upgated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.driver)

