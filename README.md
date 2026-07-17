CabFlow - Premium Taxi Booking Application
CabFlow is a full-stack, high-fidelity taxi booking and ride-hailing application. It connects customers with professional drivers, enables vehicle tracking, processes mock digital payments, and features comprehensive administrative dashboards.

📸 Application Screenshots
Landing Page (Home)
Screenshot 2026-07-17 154000
Login Page
Screenshot 2026-07-17 154349
Ride Booking Page
Screenshot 2026-07-17 154043
Live GPS Tracking & Driver Details!
Uploading Screenshot 2026-07-17 154043.png…

Screenshot 2026-07-17 154157 Screenshot 2026-07-17 154116
Technology Stack
Frontend: HTML5, CSS3 (Vanilla design system with glassmorphic dark/light mode styling), JavaScript (ES6+), Fetch API.
Backend: Django REST Framework (DRF), Python 3.10.
Database: SQLite3.
APIs: 20 Function-Based REST API endpoints + 2 Login Auth helpers.
Directory Structure
TaxiBookingApplication/
├── Backend/
│   ├── db.py                 # SQLite-mapped Django Model definitions
│   ├── models.py             # App models exporter for migrations
│   ├── views.py              # Function-Based REST API endpoints (20 CRUD APIs)
│   ├── urls.py               # API routing config
│   ├── settings.py           # Django configurations (SQLite, CORS, REST Framework)
│   ├── apps.py               # Django app configuration
│   ├── wsgi.py / asgi.py     # Production server gateways
│   └── migrations/           # Auto-generated database migration scripts
├── Frontend/
│   ├── index.html            # Landing / Home Page
│   ├── login.html            # Role-based sign-in form (Customer / Driver / Admin)
│   ├── register.html         # Customer Registration form
│   ├── booking.html          # Interactive ride booking interface
│   ├── drivers.html          # Driver registration and profile panel
│   ├── payments.html         # Transaction checkout page
│   ├── ride_history.html     # User trip ledger and action panel
│   ├── customer_dashboard.html # Passenger dashboard
│   ├── driver_dashboard.html   # Driver assignment tracker
│   ├── admin_dashboard.html    # Consolidated administrative CRUD dashboard
│   ├── style.css             # Glassmorphism visual stylesheet (dark/light theme support)
│   ├── script.js             # API Fetch library, session tracker & theme toggle
│   └── images/               # City landmark & hero images
├── screenshots/              # README documentation screenshots
├── db.sqlite3                # Persistent database file
├── populate_db.py            # SQLite sample testing data populator
└── manage.py                 # Django command-line execution manager
🗄️ Database Schemas (SQLite)
1. Customer Table
Column	Type	Constraint
customer_id	Integer	Primary Key
full_name	String	Required
email	String	Unique
phone	String	Required
address	String	Required
password	String	Required
2. Driver Table
Column	Type	Constraint
driver_id	Integer	Primary Key
driver_name	String	Required
email	String	Unique
phone	String	Required
license_number	String	Required
experience	Integer	Required
availability	String	Available / Busy / Offline
3. Vehicle Table
Column	Type	Constraint
vehicle_id	Integer	Primary Key
driver_name	String	Required
vehicle_type	String	Sedan / Hatchback / SUV / Auto / Bike / Luxury
vehicle_number	String	Required
seating_capacity	Integer	Required
model	String	Required
4. Booking Table
Column	Type	Constraint
booking_id	Integer	Primary Key
customer_name	String	Required
driver_name	String	Optional
pickup_location	String	Required
drop_location	String	Required
booking_date	Date	Required
fare	Float	Required
ride_status	String	Requested / Accepted / In Progress / Completed / Cancelled
5. Payment Table
Column	Type	Constraint
payment_id	Integer	Primary Key
booking_id	Integer	Required
customer_name	String	Required
amount	Float	Required
payment_method	String	UPI / Credit Card / Debit Card / Wallet / Cash
payment_status	String	Success / Pending / Failed
transaction_id	String	Unique
payment_date	Date	Required
🗄️ SQLite Database Screenshots
Customer Table (DB Browser for SQLite)
SQLite - Customer Table

Booking Table (DB Browser for SQLite)
SQLite - Booking Table

Payment Table (DB Browser for SQLite)
SQLite - Payment Table

🔌 REST API Documentation (22 Endpoints)
Module	Method	Endpoint	Description
Customer	POST	/customers/add/	Register/create a new customer profile.
GET	/customers/	List all registered customers.
PUT	/customers/update/<id>/	Edit customer information.
DELETE	/customers/delete/<id>/	Delete customer account.
POST	/customers/login/	Verify customer credentials.
Driver	POST	/drivers/add/	Create driver details.
GET	/drivers/	Retrieve driver availability network.
PUT	/drivers/update/<id>/	Update driver (status, experience, etc.).
DELETE	/drivers/delete/<id>/	Delete driver from network.
POST	/drivers/login/	Log in driver using registered email.
Vehicle	POST	/vehicles/add/	Insert vehicle records.
GET	/vehicles/	List vehicle configurations.
PUT	/vehicles/update/<id>/	Edit vehicle features/capacity.
DELETE	/vehicles/delete/<id>/	Remove vehicle details.
Booking	POST	/bookings/add/	Create a new ride reservation.
GET	/bookings/	Fetch platform reservation logs.
PUT	/bookings/update/<id>/	Transition trip statuses.
DELETE	/bookings/delete/<id>/	Delete booking records.
Payment	POST	/payments/add/	Register payment transactions.
GET	/payments/	Fetch invoice records.
PUT	/payments/update/<id>/	Update transaction records.
DELETE	/payments/delete/<id>/	Delete invoice records.
📮 Postman API Testing Screenshots
GET - Fetch All Customers
Endpoint: GET http://localhost:8000/customers/ Screenshot 2026-07-17 155041

POST - Create New Booking
Endpoint: POST http://localhost:8000/bookings/add/ Screenshot 2026-07-17 155041

PUT - Update Driver Availability
Endpoint: PUT http://localhost:8000/drivers/update/201/ Screenshot 2026-07-17 155041

DELETE - Remove Payment Record
Endpoint: DELETE http://localhost:8000/payments/delete/401/ Screenshot 2026-07-17 155041

🔐 Testing Credentials
Use the following pre-loaded credentials to verify app features:

Role	Email	Password
Customer	rahul@gmail.com	rahul123
Driver	ramesh@gmail.com	(email-only login)
Admin	admin@cabflow.com	admin123
⚙️ Setup & Execution
1. Prerequisites
Make sure Python 3.10+ is installed on your local machine.

2. Install Dependencies
pip install django djangorestframework django-cors-headers
3. Backend Setup
Open terminal inside the workspace directory.
Initialize Django migrations and build the database tables:
python manage.py makemigrations Backend
python manage.py migrate
Load the sample database seeder data:
python populate_db.py
Start the API server:
python manage.py runserver 0.0.0.0:8000
4. Frontend Execution
Open the file Frontend/index.html in any web browser (Safari, Chrome, Edge, Firefox).
Or run a simple HTTP server inside the Frontend directory:
npx http-server ./Frontend
✨ Key Features
Feature	Description
🌗 Dark / Light Theme Toggle	One-click theme switcher in the navigation bar persists preference across sessions.
📍 Live GPS Tracking Map	Animated SVG route map with moving taxi icon, pickup/drop pins, and real-time tracking badge.
🚗 Driver & Vehicle Details	After booking, see assigned driver name, experience, rating, vehicle model, type, and plate number.
🗺️ Popular Routes	Pre-configured route cards on landing page that auto-fill the booking form with pickup/drop locations.
🔐 Role-Based Access Control	Customer, Driver, and Admin roles with enforced page-level access guards and redirect logic.
💳 Secure Payments	Multiple payment methods (UPI, Credit Card, Debit Card, Wallet, Cash) with transaction tracking.
📊 Admin Dashboard	Full CRUD management of Customers, Drivers, Vehicles, Bookings, and Payments with statistics.
🏙️ City Landmark Images	Real images of Hyderabad landmarks (Charminar, Hussain Sagar, Cyber Towers, Golconda Fort).
📱 Responsive Design	Glassmorphic design system with smooth animations, micro-interactions, and mobile-friendly layout.
