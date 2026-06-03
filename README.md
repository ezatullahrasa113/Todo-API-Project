Todo API
![Swagger](docs\swagger.png)
A Todo API built with Django REST Framework (DRF).
Features
User Registration
JWT Authentication
Access Token & Refresh Token
Logout with Refresh Token Blacklisting
CRUD Operations for Todos
Search
Filtering
Ordering
Pagination
Swagger Documentation
Owner Permissions
Technologies
Django
Django REST Framework
Simple JWT
Django Filter
DRF Spectacular
Installation
Clone the repository:
git clone <repository-url> cd todo-api 
Create virtual environment:
python -m venv venv 
Activate virtual environment:
Windows:
venv\Scripts\activate 
Install dependencies:
pip install -r requirements.txt 
Run migrations:
python manage.py migrate 
Create superuser:
python manage.py createsuperuser 
Run server:
python manage.py runserver 
API Documentation
Swagger UI:
http://127.0.0.1:8000/api/docs/ 
Authentication
Get JWT tokens:
POST /api/token/ 
Refresh token:
POST /api/token/refresh/ 
Logout:
POST /api/logout/ 
Author
Ezatullah Rasa