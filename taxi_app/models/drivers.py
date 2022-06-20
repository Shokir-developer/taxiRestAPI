from django.db import models

class Driver(models.Model):
	name = models.CharField(max_length=10, null=True)
	surname = models.CharField(max_length=100, null=True)
	car = models.CharField(max_length=8, null=True)
	phone_number = models.CharField(max_length=9, null=True)

	def __str__(self):
		return self.name + ' ' + self.surname