import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

from Backend.models import Customer, Driver, Vehicle, Booking, Payment

def populate():
    print("Populating database with sample data...")

    # Clear existing data to avoid conflicts
    Customer.objects.all().delete()
    Driver.objects.all().delete()
    Vehicle.objects.all().delete()
    Booking.objects.all().delete()
    Payment.objects.all().delete()

    # 1. Add Customer
    customer = Customer.objects.create(
        customer_id=101,
        full_name="Rahul Sharma",
        email="rahul@gmail.com",
        phone="9876543210",
        address="Hyderabad",
        password="rahul123"
    )
    print(f"Created Customer: {customer}")

    # 2. Add Driver
    driver = Driver.objects.create(
        driver_id=201,
        driver_name="Ramesh Kumar",
        email="ramesh@gmail.com",
        phone="9988776655",
        license_number="DL123456789",
        experience=5,
        availability="Available"
    )
    print(f"Created Driver: {driver}")

    # 3. Add Vehicle
    vehicle = Vehicle.objects.create(
        vehicle_id=301,
        driver_name="Ramesh Kumar",
        vehicle_type="Sedan",
        vehicle_number="TS09AB1234",
        seating_capacity=4,
        model="Hyundai Verna"
    )
    print(f"Created Vehicle: {vehicle}")

    # 4. Add Ride Booking
    booking = Booking.objects.create(
        booking_id=401,
        customer_name="Rahul Sharma",
        driver_name="Ramesh Kumar",
        pickup_location="Madhapur",
        drop_location="Gachibowli",
        booking_date="2026-08-15",
        fare=350.0,
        ride_status="Accepted"
    )
    print(f"Created Ride Booking: {booking}")

    # 5. Add Payment
    payment = Payment.objects.create(
        payment_id=501,
        booking_id=401,
        customer_name="Rahul Sharma",
        amount=350.0,
        payment_method="UPI",
        payment_status="Success",
        transaction_id="TXN456789123",
        payment_date="2026-08-15"
    )
    print(f"Created Payment: {payment}")

    print("Database population complete!")

if __name__ == '__main__':
    populate()
