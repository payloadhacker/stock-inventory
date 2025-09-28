# Stock Inventory App

A simple Django-based inventory management system where an admin can:
- Add new stock items
- Edit and delete stock
- View all stocks in a clean table
- Search for stocks by name

Normal users can only view stocks. Admin controls editing and deleting.

## Features
- Django backend
- User authentication (login/logout)
- Permissions: Only admin can add, edit, delete
- Responsive frontend (mobile-friendly with pure CSS)
- Search functionality for stock items

## Tech Stack
- Python (Django)
- SQLite (default, but can be swapped with PostgreSQL for production)
- HTML and CSS (no frontend framework, pure CSS)

## Project Structure
```
stock-inventory/
│── collection/        # Django app (views, models, templates)
│── static/            # CSS, JS, images
│── templates/         # Base templates
│── db.sqlite3         # Local DB (ignored in Git)
│── manage.py
```

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/payloadhacker/stock-inventory.git
cd stock-inventory
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create superuser (admin)
```bash
python manage.py createsuperuser
```

### 6. Run server
```bash
python manage.py runserver
```

Now open http://127.0.0.1:8000 in your browser.

## Admin Access
- Only admin users can add, edit, or delete stock.
- Normal users can view stocks but not modify them.

## Future Improvements
- API support (Django REST Framework)
- Deploy to Heroku or PythonAnywhere
- Support for multiple warehouses
- Export stock data to Excel/CSV

## License
MIT License – free to use and modify.
