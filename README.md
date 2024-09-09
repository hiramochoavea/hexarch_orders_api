# Orders API

This is a REST API for item and order management implemented in Python using the Django framework. The API follows the principles of the Hexagonal Architecture (Ports & Adapters) and allows to perform CRUD operations on items and orders, validating the existence of items when creating or modifying orders.

## Features
- **Items Management**: Create, retrieve, update, and list items.
- **Orders Management**: Create, retrieve, update, and list orders.
- **Hexagonal Architecture**: The system follows a layered architecture that separates concerns between business logic, infrastructure, and interfaces.

## Technologies Used
- Python 3.12
- Django 5.0.4
- Django Rest Framework 3.15.1
- MySQL

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hiramochoavea/hexarch_orders_api.git
   cd hexarch_orders_api
   ```

2. Build and run Docker containers:

   ```bash
   docker-compose up --build -d
   ```

6. Wait for the MySQL database and containers to initialize. Everything will be configured automatically.

7. Start making requests with Postman!

## Postman Collection

The file "OrderAPI Collection.postman_collection.json" contains basic HTTP requests to the API that you can try out.

## API Documentation

The API is designed according to the OpenAPI 3.0 specification. For more information, visit http://localhost:4450/api/schema/docs/ after setting up the project.

### Items Endpoints

#### `GET /api/items/`
Retrieve a list of items.

- **Responses**:
  - `200 OK`: A list of items.
  - `204 No Content`: No items found.
  - `404 Not Found`: Item not found.

#### `POST /api/items/`
Create a new item.

- **Request Body**: JSON object representing the item to create.
- **Responses**:
  - `201 Created`: Item successfully created.
  - `400 Bad Request`: Invalid input data.

#### `GET /api/items/{item_id}/`
Retrieve an item by its unique identifier.

- **Responses**:
  - `200 OK`: The requested item.
  - `404 Not Found`: Item not found.

#### `PUT /api/items/{item_id}/`
Update an existing item by its unique identifier.

- **Responses**:
  - `200 OK`: Item successfully updated.
  - `400 Bad Request`: Invalid input data.
  - `404 Not Found`: Item not found.

### Orders Endpoints

#### `GET /api/orders/`
Retrieve a list of orders.

- **Responses**:
  - `200 OK`: A list of orders.
  - `204 No Content`: No orders found.
  - `404 Not Found`: Order not found.

#### `POST /api/orders/`
Create a new order.

- **Request Body**: JSON object representing the order to create.
- **Responses**:
  - `201 Created`: Order successfully created.
  - `400 Bad Request`: Invalid input data.
  - `409 Conflict`: One or more items in the order not found.

#### `GET /api/orders/{order_id}/`
Retrieve an order by its unique identifier.

- **Responses**:
  - `200 OK`: The requested order.
  - `404 Not Found`: Order not found.

#### `PUT /api/orders/{order_id}/`
Update an existing order by its unique identifier.

- **Responses**:
  - `200 OK`: Order successfully updated.
  - `400 Bad Request`: Invalid input data.
  - `404 Not Found`: Order not found.