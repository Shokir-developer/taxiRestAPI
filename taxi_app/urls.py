from django.urls import path
from .views import CreateCustomerAPIView, CreateDriverAPIView, CreateOrderAPIView, \
										CreateOrderStatusAPIView, CreateAcceptOrderAPPIView,\
										driverSerializerView, createDriverSerializerView


urlpatterns = [
	path('customer/', CreateCustomerAPIView.as_view(), name='customer'),
	path('driver/', CreateDriverAPIView.as_view(), name='driver'),
	path('order/', CreateOrderAPIView.as_view(), name='order'),
	path('order_status/', CreateOrderStatusAPIView.as_view(), name='order_status'),
	path('accept_status/', CreateAcceptOrderAPPIView.as_view(), name='accept_status'),
	path('driver_serializer/', driverSerializerView, name='driver_serializer'),
	path('driver_serializer_create/', createDriverSerializerView, name='driver_serializer_create'),
]