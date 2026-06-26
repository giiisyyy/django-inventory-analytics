# B2B Inventory & Stock Analytics Platform 📦📈

An enterprise-grade web application built with Python and Django designed to streamline warehouse logistics, track stock variations in real-time, and provide instant data analytics for decision-making.

## 🚀 Key Features

- Django ORM Architecture: Implements relational database modeling utilizing Django's Object-Relational Mapping.
- Real-Time Threshold Analytics: Background evaluation logic to instantly flag products dropping below critical stock safety metrics.
- Secure Model Validations: Enforces strict field constraints, including unique SKU generation and precise decimal price scaling.
- Built-in Enterprise Administration Dashboard: Fully integrated with Django's native authentication for secure database management.

## 🛠️ Tech Stack

- Backend Framework: Django 4.x / 5.x
- Language: Python 3.x
- Database: SQLite (Development)

## 📦 Installation & Setup

1. Clona el repositorio ([ver en GitHub](https://github.com/giiisyyy/django-inventory-analytics)):

```bash
git clone https://github.com/giiisyyy/django-inventory-analytics.git
```

2. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies and run migrations:

```bash
pip install django
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser to access the admin dashboard:

```bash
python manage.py createsuperuser
```

5. Start the server:

```bash
python manage.py runserver
```
