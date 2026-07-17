# CabFlow - Premium Taxi Booking Application

CabFlow is a full-stack, high-fidelity taxi booking and ride-hailing application. It connects customers with professional drivers, enables vehicle tracking, processes mock digital payments, and features comprehensive administrative dashboards.

---

## 📸 Application Screenshots

### Landing Page (Home)
<img width="928" height="451" alt="Screenshot 2026-07-17 154000" src="https://github.com/user-attachments/assets/fd59d44b-d484-4647-a920-0b4347bac237" />



### Login Page
<img width="893" height="416" alt="Screenshot 2026-07-17 154349" src="https://github.com/user-attachments/assets/9d5ececc-dd17-42d4-bdbf-6695f37529c1" />



### Ride Booking Page
<img width="683" height="408" alt="Screenshot 2026-07-17 154043" src="https://github.com/user-attachments/assets/e63e5ec6-7eba-43b6-b185-6556f8486a29" />



### Live GPS Tracking & Driver Details!
[Uploading Screenshot 2026-07-17 154043.png…]()

<img width="713" height="395" alt="Screenshot 2026-07-17 154157" src="https://github.com/user-attachments/assets/f901887f-c174-45ea-a52a-890e633dafd5" />
<img width="625" height="408" alt="Screenshot 2026-07-17 154116" src="https://github.com/user-attachments/assets/8c1a0985-89b0-46e5-b06a-2c457bac4279" />

---

## Technology Stack

- **Frontend**: HTML5, CSS3 (Vanilla design system with glassmorphic dark/light mode styling), JavaScript (ES6+), Fetch API.
- **Backend**: Django REST Framework (DRF), Python 3.10.
- **Database**: SQLite3.
- **APIs**: 20 Function-Based REST API endpoints + 2 Login Auth helpers.

---

## Directory Structure

```
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
```

---

## 🗄️ Database Schemas (SQLite)

### 1. Customer Table
| Column | Type | Constraint |
| :--- | :--- | :--- |
| `customer_id` | Integer | Primary Key |
| `full_name` | String | Required |
| `email` | String | Unique |
| `phone` | String | Required |
| `address` | String | Required |
| `password` | String | Required |

### 2. Driver Table
| Column | Type | Constraint |
| :--- | :--- | :--- |
| `driver_id` | Integer | Primary Key |
| `driver_name` | String | Required |
| `email` | String | Unique |
| `phone` | String | Required |
| `license_number` | String | Required |
| `experience` | Integer | Required |
| `availability` | String | Available / Busy / Offline |

### 3. Vehicle Table
| Column | Type | Constraint |
| :--- | :--- | :--- |
| `vehicle_id` | Integer | Primary Key |
| `driver_name` | String | Required |
| `vehicle_type` | String | Sedan / Hatchback / SUV / Auto / Bike / Luxury |
| `vehicle_number` | String | Required |
| `seating_capacity` | Integer | Required |
| `model` | String | Required |

### 4. Booking Table
| Column | Type | Constraint |
| :--- | :--- | :--- |
| `booking_id` | Integer | Primary Key |
| `customer_name` | String | Required |
| `driver_name` | String | Optional |
| `pickup_location` | String | Required |
| `drop_location` | String | Required |
| `booking_date` | Date | Required |
| `fare` | Float | Required |
| `ride_status` | String | Requested / Accepted / In Progress / Completed / Cancelled |

### 5. Payment Table
| Column | Type | Constraint |
| :--- | :--- | :--- |
| `payment_id` | Integer | Primary Key |
| `booking_id` | Integer | Required |
| `customer_name` | String | Required |
| `amount` | Float | Required |
| `payment_method` | String | UPI / Credit Card / Debit Card / Wallet / Cash |
| `payment_status` | String | Success / Pending / Failed |
| `transaction_id` | String | Unique |
| `payment_date` | Date | Required |

---

## 🗄️ SQLite Database Screenshots

### Customer Table (DB Browser for SQLite)
![SQLite - Customer Table](screenshots/sqlite_customers.png)

### Booking Table (DB Browser for SQLite)
![SQLite - Booking Table](screenshots/sqlite_bookings.png)

### Payment Table (DB Browser for SQLite)
![SQLite - Payment Table](screenshots/sqlite_payments.png)

---

## 🔌 REST API Documentation (22 Endpoints)

| Module | Method | Endpoint | Description |
| :--- | :---: | :--- | :--- |
| **Customer** | POST | `/customers/add/` | Register/create a new customer profile. |
| | GET | `/customers/` | List all registered customers. |
| | PUT | `/customers/update/<id>/` | Edit customer information. |
| | DELETE | `/customers/delete/<id>/` | Delete customer account. |
| | POST | `/customers/login/` | Verify customer credentials. |
| **Driver** | POST | `/drivers/add/` | Create driver details. |
| | GET | `/drivers/` | Retrieve driver availability network. |
| | PUT | `/drivers/update/<id>/` | Update driver (status, experience, etc.). |
| | DELETE | `/drivers/delete/<id>/` | Delete driver from network. |
| | POST | `/drivers/login/` | Log in driver using registered email. |
| **Vehicle** | POST | `/vehicles/add/` | Insert vehicle records. |
| | GET | `/vehicles/` | List vehicle configurations. |
| | PUT | `/vehicles/update/<id>/` | Edit vehicle features/capacity. |
| | DELETE | `/vehicles/delete/<id>/` | Remove vehicle details. |
| **Booking** | POST | `/bookings/add/` | Create a new ride reservation. |
| | GET | `/bookings/` | Fetch platform reservation logs. |
| | PUT | `/bookings/update/<id>/` | Transition trip statuses. |
| | DELETE | `/bookings/delete/<id>/` | Delete booking records. |
| **Payment** | POST | `/payments/add/` | Register payment transactions. |
| | GET | `/payments/` | Fetch invoice records. |
| | PUT | `/payments/update/<id>/` | Update transaction records. |
| | DELETE | `/payments/delete/<id>/` | Delete invoice records. |

---

## 📮 Postman API Testing Screenshots

### GET - Fetch All Customers
**Endpoint**: `GET http://localhost:8000/customers/`
<img width="890" height="488" alt="Screenshot 2026-07-17 155041" src="https://github.com/user-attachments/assets/d99c21a4-90a7-4dd7-b1e4-eb2dd9af5ebb" />



### POST - Create New Booking
**Endpoint**: `POST http://localhost:8000/bookings/add/`
<img width="890" height="488" alt="Screenshot 2026-07-17 155041" src="https://github.com/user-attachments/assets/981878cd-2c69-48ce-8693-496bb655eb61" />



### PUT - Update Driver Availability
**Endpoint**: `PUT http://localhost:8000/drivers/update/201/`
<img width="890" height="488" alt="Screenshot 2026-07-17 155041" src="https://github.com/user-attachments/assets/669c3de0-c29c-44d9-91b4-f059472efa54" />


### DELETE - Remove Payment Record
**Endpoint**: `DELETE http://localhost:8000/payments/delete/401/`
<img width="890" height="488" alt="Screenshot 2026-07-17 155041" src="https://github.com/user-attachments/assets/753aa94c-52f5-49cd-95de-2d712de6e97c" />


---

## 🔐 Testing Credentials

Use the following pre-loaded credentials to verify app features:

| Role | Email | Password |
| :--- | :--- | :--- |
| **Customer** | `rahul@gmail.com` | `rahul123` |
| **Driver** | `ramesh@gmail.com` | *(email-only login)* |
| **Admin** | `admin@cabflow.com` | `admin123` |

---

## ⚙️ Setup & Execution

### 1. Prerequisites
Make sure Python 3.10+ is installed on your local machine.

### 2. Install Dependencies
```bash
pip install django djangorestframework django-cors-headers
```

### 3. Backend Setup
1. Open terminal inside the workspace directory.
2. Initialize Django migrations and build the database tables:
   ```bash
   python manage.py makemigrations Backend
   python manage.py migrate
   ```
3. Load the sample database seeder data:
   ```bash
   python populate_db.py
   ```
4. Start the API server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

### 4. Frontend Execution
1. Open the file `Frontend/index.html` in any web browser (Safari, Chrome, Edge, Firefox).
2. Or run a simple HTTP server inside the `Frontend` directory:
   ```bash
   npx http-server ./Frontend
   ```

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 🌗 **Dark / Light Theme Toggle** | One-click theme switcher in the navigation bar persists preference across sessions. |
| 📍 **Live GPS Tracking Map** | Animated SVG route map with moving taxi icon, pickup/drop pins, and real-time tracking badge. |
| 🚗 **Driver & Vehicle Details** | After booking, see assigned driver name, experience, rating, vehicle model, type, and plate number. |
| 🗺️ **Popular Routes** | Pre-configured route cards on landing page that auto-fill the booking form with pickup/drop locations. |
| 🔐 **Role-Based Access Control** | Customer, Driver, and Admin roles with enforced page-level access guards and redirect logic. |
| 💳 **Secure Payments** | Multiple payment methods (UPI, Credit Card, Debit Card, Wallet, Cash) with transaction tracking. |
| 📊 **Admin Dashboard** | Full CRUD management of Customers, Drivers, Vehicles, Bookings, and Payments with statistics. |
| 🏙️ **City Landmark Images** | Real images of Hyderabad landmarks (Charminar, Hussain Sagar, Cyber Towers, Golconda Fort). |
| 📱 **Responsive Design** | Glassmorphic design system with smooth animations, micro-interactions, and mobile-friendly layout. |

---
