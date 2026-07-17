from django.urls import path
from . import views

urlpatterns = [
    # Customer URLs
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/', views.get_customers, name='get_customers'),
    path('customers/update/<int:pk>/', views.update_customer, name='update_customer'),
    path('customers/delete/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('customers/login/', views.customer_login, name='customer_login'),

    # Driver URLs
    path('drivers/add/', views.add_driver, name='add_driver'),
    path('drivers/', views.get_drivers, name='get_drivers'),
    path('drivers/update/<int:pk>/', views.update_driver, name='update_driver'),
    path('drivers/delete/<int:pk>/', views.delete_driver, name='delete_driver'),
    path('drivers/login/', views.driver_login, name='driver_login'),

    # Vehicle URLs
    path('vehicles/add/', views.add_vehicle, name='add_vehicle'),
    path('vehicles/', views.get_vehicles, name='get_vehicles'),
    path('vehicles/update/<int:pk>/', views.update_vehicle, name='update_vehicle'),
    path('vehicles/delete/<int:pk>/', views.delete_vehicle, name='delete_vehicle'),

    # Booking URLs
    path('bookings/add/', views.add_booking, name='add_booking'),
    path('bookings/', views.get_bookings, name='get_bookings'),
    path('bookings/update/<int:pk>/', views.update_booking, name='update_booking'),
    path('bookings/delete/<int:pk>/', views.delete_booking, name='delete_booking'),

    # Payment URLs
    path('payments/add/', views.add_payment, name='add_payment'),
    path('payments/', views.get_payments, name='get_payments'),
    path('payments/update/<int:pk>/', views.update_payment, name='update_payment'),
    path('payments/delete/<int:pk>/', views.delete_payment, name='delete_payment'),
]
