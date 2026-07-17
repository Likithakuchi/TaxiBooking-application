from django.db import models

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    password = models.CharField(max_length=255)

    class Meta:
        app_label = 'Backend'
        db_table = 'customers'

    def __str__(self):
        return self.full_name


class Driver(models.Model):
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
        ('Offline', 'Offline'),
    ]

    driver_id = models.IntegerField(primary_key=True)
    driver_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    license_number = models.CharField(max_length=100)
    experience = models.IntegerField()
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='Available')

    class Meta:
        app_label = 'Backend'
        db_table = 'drivers'

    def __str__(self):
        return self.driver_name


class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Auto', 'Auto'),
        ('Bike', 'Bike'),
        ('Luxury', 'Luxury'),
    ]

    vehicle_id = models.IntegerField(primary_key=True)
    driver_name = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    vehicle_number = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    model = models.CharField(max_length=100)

    class Meta:
        app_label = 'Backend'
        db_table = 'vehicles'

    def __str__(self):
        return f"{self.model} ({self.vehicle_number})"


class Booking(models.Model):
    RIDE_STATUS_CHOICES = [
        ('Requested', 'Requested'),
        ('Accepted', 'Accepted'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    booking_id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    driver_name = models.CharField(max_length=255, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)
    booking_date = models.DateField()
    fare = models.FloatField()
    ride_status = models.CharField(max_length=20, choices=RIDE_STATUS_CHOICES, default='Requested')

    class Meta:
        app_label = 'Backend'
        db_table = 'bookings'

    def __str__(self):
        return f"Booking {self.booking_id} by {self.customer_name}"


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('UPI', 'UPI'),
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Wallet', 'Wallet'),
        ('Cash', 'Cash'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('Success', 'Success'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    ]

    payment_id = models.IntegerField(primary_key=True)
    booking_id = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateField()

    class Meta:
        app_label = 'Backend'
        db_table = 'payments'

    def __str__(self):
        return f"Payment {self.payment_id} - {self.payment_status}"
