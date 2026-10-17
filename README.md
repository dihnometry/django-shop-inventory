# Inventory Management System

This project is a Django-based inventory management system designed for small stores. It provides an API to manage products, categories, stock, and transactions (both purchases and sales) with authentication using JWT.

## Features

- **User Authentication:** JWT-based authentication.
- **Product Management:** CRUD operations for products, categories, and stock.
- **Transaction Management:** Manage purchases and sales with automatic stock updates.
- **RESTful API:** Well-structured API endpoints for managing the inventory.

## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and Docker Compose
- Git

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/dihnometry/django-shop-inventory.git
   cd django-shop-inventory
   ```

2. Create your environment file from the example and edit the values:
   ```bash
   cp .env.example .env
   ```
   The `.env` file defines the following variables:
   ```
   DB_NAME=inventorydb
   DB_USER=inventory_user
   DB_PASSWORD=SecretPass_1234
   DB_ROOT_PASSWORD=changeme
   SECRET_KEY='supersecretkey'
   ```
   `DB_USER` must **not** be `root`.

3. Build and start the containers (MySQL + Django):
   ```bash
   docker compose up --build
   ```
   The API will be available at `http://localhost:8000`.

4. In another terminal, apply the migrations (they are not run automatically):
   ```bash
   docker compose exec django-web python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   docker compose exec django-web python manage.py createsuperuser
   ```

6. Stop the containers:
   ```bash
   docker compose down        # keeps the database data
   docker compose down -v     # also deletes the database volume
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
