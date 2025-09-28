# Inventory Management System API

- A Backend API built with FastAPI + SQLAlchemy + PostgreSQL for managing products in a warehouse.

## Features

### Product Management (CRUD)

- Create/Add New Products
- Get All Products or fetch by ID
- Update Product details
- Delete Products

### Invetory Logic

- Increment Stock (ensures only positive values)
- Decrement Stock (ensures no negative stock, error if insufficient)

### Low Stock Monitoring

- Tracking stocks which are below a threshold

### Error Handeling

- Proper HTTP status codes and clear error messages (400 for Bad Requests, 404 for missing products, etc)

## Tech Stack

- Language: Python
- Framework: FastAPI
- ORM: SQLAlchemy
- Database: PostgreSQL
- Data Validation: Pydantic
- Testing: pytest

## Setup Instructions

1. Clone the Repo

    ```bash
    git clone https://github.com/An-Array/
    cd 
    ```

2. Create Virtual Environment

    ```cmd
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install Dependencies

    ```cmd
    pip install -r requirements.txt
    ```

4. Configure Environment Variables

    - Create a .env file in the Project root

    ```.env
    database_hostname=localhost
    database_port=5432
    database_username=postgres
    database_password=postgres
    database_name=inventory_db
    ```

5. Run Server

    ```bash
    uvicorn app.main:app --reload
    ```

    - API will be available at - ```https://127.0.0.1:8000``` and  ```https://localhost:8000```

## API Endpoints

### Product Management

- ```POST /products```        -> Create/Add a Product
- ```GET /products```         -> Create/Add a Product
- ```GET /products/{id}```    -> Create/Add a Product
- ```PATCH /products/{id}```  -> Create/Add a Product
- ```DELETE /products/{id}``` -> Create/Add a Product

### Inventory Management

- ```PATCH /products/increment/{id}```  -> Add Stocks
- ```PATCH /products/decrement/{id}```  -> Remove Stocks

### Monitoring Threshold

- ```GET /products/below_requirement``` -> Products with stock <= Threshold

## Design Choice and Assumptions

- Stock Updates:
  - Stock must be updated via ```increment``` / ```decrement``` endpoints to ensure validation rules.
  - However, ```PATCH /products/{id}``` still allows updating ```stock_quantity``` directly
- Low Stock Logic:
  - A product is considered "below requirement" when ```stock_quantity <= low_stock_threshold```
- Concurreny
  - Uses ```with_for_update``` in transactions to avoid race conditions on stock updates.

## Future Enhancements (If Required)

- Add USER AUTENTICATION (Role-Based: Admin, Staff)
- Add pagination & search for product listings
- Add audit logs for all stock changes