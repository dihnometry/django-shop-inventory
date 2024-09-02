# Inventory Management System

This project is a Django-based inventory management system designed for small stores. It provides an API to manage products, categories, stock, and transactions (both purchases and sales) with authentication using JWT.

## Features

- **User Authentication:** JWT-based authentication.
- **Product Management:** CRUD operations for products, categories, and stock.
- **Transaction Management:** Manage purchases and sales with automatic stock updates.
- **RESTful API:** Well-structured API endpoints for managing the inventory.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- MySQL

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dihnometry/django-shop-inventory.git
   cd django-shop-inventory
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the MySQL database and configure the database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': 'your_port',
       }
   }
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the server:
   ```bash
   python manage.py runserver
   ```

### API Endpoints

The following are the key endpoints provided by the API:

- **/api/users/**: Register a new user (no authentication required).
- **/api/token/**: Obtain JWT token (login).
- **/api/token/refresh/**: Refresh JWT token.
- **/api/products/**: CRUD operations on products.
- **/api/categories/**: CRUD operations on product categories.
- **/api/stock/**: CRUD operations on stock products.
- **/api/transactions/**: Manage purchases and sales transactions.

### Usage

- To interact with the API, you can use tools like `curl`, `Postman`, or any HTTP client.
- Make sure to include the JWT token in the `Authorization` header for endpoints that require authentication.
