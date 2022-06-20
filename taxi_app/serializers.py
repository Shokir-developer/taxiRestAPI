from rest_framework import serializers
from .models.drivers import Driver

class DriverSerializers(serializers.ModelSerializer):
	class Meta:
		model = Driver
		fields = "__all__"