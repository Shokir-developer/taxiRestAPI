from rest_framework.views import APIView
from rest_framework.response import Response
from .models.customer import Customer
from .models.drivers import Driver
from .models.order import Order, OrderStatus, AcceptOrder
from .serializers import DriverSerializers
from rest_framework.decorators import api_view

@api_view(['GET'])
def driverSerializerView(request):
	items = Driver.objects.all()
	serializer = DriverSerializers(items, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def createDriverSerializerView(request):
	serializer = DriverSerializers(data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


class CreateDriverAPIView(APIView):
	def post(self, request):
		data = request.data
		name = data['name']
		surname = data['surname']
		car = data['car']
		phone_number = data['phone_number']

		driver = Driver.objects.create(name=name, surname=surname, car=car, phone_number=phone_number)
		return Response('Driver is successfully created!')


class CreateCustomerAPIView(APIView):
	def post(self, request):
		data = request.data
		name = data['name']
		surname = data['surname']
		phone_number = data['phone_number']

		customer = Customer.objects.create(name=name, surname=surname, phone_number=phone_number)
		return Response('Customer is successfully created!')

class CreateOrderAPIView(APIView):
	def post(self, request):
		data = request.data
		customer = data['customer']
		get_customer = Customer.objects.get(id=customer)
		order = Order.objects.create(customer=get_customer)
		return Response('Order is successfully created!')

class CreateOrderStatusAPIView(APIView):
	def post(self, request):
		data = request.data
		status = data['status']

		order_status = OrderStatus.objects.create(status=status)
		return Response('Status of order is successfully created!')


class CreateAcceptOrderAPPIView(APIView):
	def post(self, request):
		data = request.data
		driver = data['driver']
		customer = data['customer']
		status  = data['status']

		get_driver = Driver.objects.get(id=driver)
		get_customer = Customer.objects.get(id=customer)
		get_status = OrderStatus.objects.get(id=driver)

		accept_order = AcceptOrder.objects.create(driver=get_driver, customer=get_customer,  status=get_status)
		return Response('Order is successfully accepted!')