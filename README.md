# 🛡️ Mini Project — JWT Authentication API with Django Rest Framework

A secure and extendable backend API for user registration, authentication (JWT), and CRUD operations on personal notes. Built with Django Rest Framework and Simple JWT.

---

## 🚀 Features

- ✅ **User Registration** (`/api/register/`)
- 🔐 **JWT Authentication** (`/api/token/`, `/api/token/refresh/`)
- 📝 **CRUD for Notes** linked to the authenticated user (`/api/notes/`)
- 🏷️ **Tags Support** via Many-to-Many relation
- 🔎 **Filtering** by tags and creation date
- 🔒 **Permissions**: Only the author can update/delete their own notes

---

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT (`djangorestframework-simplejwt`)
- django-filter
