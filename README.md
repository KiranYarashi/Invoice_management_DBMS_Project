# Invoice Management System

This is a Django-based Invoice Management System that allows users to manage invoices, customers, and items. The system provides functionalities to add, edit, and delete invoices, customers, and items.

---
---


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/invoice_management_system.git
    cd invoice_management_system
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure the database settings in `dbms/settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'invoice_manage',
            'USER': 'userName',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` to manage users and other models.
- Access the main application at `http://127.0.0.1:8000/` to manage invoices, customers, and items.

## URL Configuration

The URL configuration is defined in [`dbms/urls.py`](dbms/urls.py). The main URLs include:
- `/admin/` - Admin panel
- `/` - Login view
- `/invoice-list/` - List of invoices
- `/invoice-list/add-invoice/` - Add a new invoice
- `/edit-invoice/<int:invoice_id>/` - Edit an invoice
- `/delete-invoice/<int:invoice_id>/` - Delete an invoice
- `/customer-details/<int:cust_id>/` - Customer details
- `/invoice-items/<int:invoice_id>/` - Invoice items
- `/add-customer/` - Add a new customer
- `/edit-item/<int:id>/` - Edit an item
- `/delete-item/<int:id>/` - Delete an item
- `/add-item/<int:id>/` - Add a new item
- `/pay-id/<int:pay>/` - Payment

