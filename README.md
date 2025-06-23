# 📞 REST API Contact App

A Django REST Framework-based API for managing contact records. This project enables users to create, retrieve, update, and delete contact information in a clean and structured way using JWT authentication.

## 🚀 Features

- Secure Contact CRUD Operations
- User-specific contact management
- Token-based access control
- Clean, RESTful API design

---

## 🛠️ Tech Stack

- Python 3.11+
- Django 5.0+
- Django REST Framework
- Simple JWT

---

## 📸 Screenshots

- DRF page


---

## 📦 Installation Guide

Follow the steps below to run this project locally:

## ⚙️ Setup Instructions

### 🔧 Step-by-step

1. **Clone the repository**
   ```bash
   git clone https://github.com/rahat-abir/REST_API_contact_app.git
   cd REST_API_contact_app
2. **(Optional) Create and activate a virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate
3. **Install dependencies**
   ```bash
   pip install django
4. **Apply database migrations**
   ```bash
   python manage.py migrate
5. **Run the development server**
   ```bash
   python manage.py runserver
6. **Visit in browser**
   ```bash
   http://127.0.0.1:8000/api/

## 📬 API Endpoints

| Method | Endpoint                 | Description             |
|--------|--------------------------|-------------------------|
| POST   | `/api/register/`         | Register a new user     |
| POST   | `/api/token/`            | Login and get tokens    |
| GET    | `/api/contacts/`         | List all contacts       |
| POST   | `/api/contacts/`         | Create a new contact    |
| GET    | `/api/contacts/{id}/`    | Retrieve single contact |
| PUT    | `/api/contacts/{id}/`    | Update contact          |
| DELETE | `/api/contacts/{id}/`    | Delete contact          |

## ⚙️ Project Structure

REST_API_contact_app/
├── api/ # Contact app

│   ├── views.py

│   ├── models.py

│   ├── serializers.py

│   └── urls.py

├── contactapp/     # Main Django project

│   └── settings.py

├── db.sqlite3

├── manage.py

├── requirements.txt

└── .env



