from django.db import models
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Driver, Vehicle, Booking, Payment

# --- Serializers ---

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


# --- Customer APIs ---

@api_view(['POST'])
def add_customer(request):
    data = request.data.copy()
    if 'customer_id' not in data or not data['customer_id']:
        max_id = Customer.objects.aggregate(models.Max('customer_id'))['customer_id__max']
        data['customer_id'] = max_id + 1 if max_id else 101
    
    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CustomerSerializer(customer, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
    customer.delete()
    return Response({'message': 'Customer deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def customer_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        customer = Customer.objects.get(email=email, password=password)
        serializer = CustomerSerializer(customer)
        return Response({'status': 'success', 'user': serializer.data})
    except Customer.DoesNotExist:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)


# --- Driver APIs ---

@api_view(['POST'])
def add_driver(request):
    data = request.data.copy()
    if 'driver_id' not in data or not data['driver_id']:
        max_id = Driver.objects.aggregate(models.Max('driver_id'))['driver_id__max']
        data['driver_id'] = max_id + 1 if max_id else 201
    
    serializer = DriverSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_drivers(request):
    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_driver(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = DriverSerializer(driver, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_driver(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)
    driver.delete()
    return Response({'message': 'Driver deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def driver_login(request):
    email = request.data.get('email')
    try:
        driver = Driver.objects.get(email=email)
        serializer = DriverSerializer(driver)
        return Response({'status': 'success', 'user': serializer.data})
    except Driver.DoesNotExist:
        return Response({'error': 'Invalid driver email'}, status=status.HTTP_400_BAD_REQUEST)


# --- Vehicle APIs ---

@api_view(['POST'])
def add_vehicle(request):
    data = request.data.copy()
    if 'vehicle_id' not in data or not data['vehicle_id']:
        max_id = Vehicle.objects.aggregate(models.Max('vehicle_id'))['vehicle_id__max']
        data['vehicle_id'] = max_id + 1 if max_id else 301
    
    serializer = VehicleSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_vehicles(request):
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_vehicle(request, pk):
    try:
        vehicle = Vehicle.objects.get(pk=pk)
    except Vehicle.DoesNotExist:
        return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_vehicle(request, pk):
    try:
        vehicle = Vehicle.objects.get(pk=pk)
    except Vehicle.DoesNotExist:
        return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)
    vehicle.delete()
    return Response({'message': 'Vehicle deleted successfully'}, status=status.HTTP_200_OK)


# --- Booking APIs ---

@api_view(['POST'])
def add_booking(request):
    data = request.data.copy()
    if 'booking_id' not in data or not data['booking_id']:
        max_id = Booking.objects.aggregate(models.Max('booking_id'))['booking_id__max']
        data['booking_id'] = max_id + 1 if max_id else 401
    
    serializer = BookingSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_booking(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BookingSerializer(booking, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_booking(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)
    booking.delete()
    return Response({'message': 'Booking deleted successfully'}, status=status.HTTP_200_OK)


# --- Payment APIs ---

@api_view(['POST'])
def add_payment(request):
    data = request.data.copy()
    if 'payment_id' not in data or not data['payment_id']:
        max_id = Payment.objects.aggregate(models.Max('payment_id'))['payment_id__max']
        data['payment_id'] = max_id + 1 if max_id else 501
    
    serializer = PaymentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_payments(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_payment(request, pk):
    try:
        payment = Payment.objects.get(pk=pk)
    except Payment.DoesNotExist:
        return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PaymentSerializer(payment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_payment(request, pk):
    try:
        payment = Payment.objects.get(pk=pk)
    except Payment.DoesNotExist:
        return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
    payment.delete()
    return Response({'message': 'Payment deleted successfully'}, status=status.HTTP_200_OK)
