# 🚀 FastAPI Category & Product API

## 📌 Project Overview

This is a backend API project built using **FastAPI**.
It provides RESTful APIs to manage **Categories** and **Products** with proper database relationships.

---

## 🛠️ Tech Stack

* **FastAPI** – Backend framework
* **Python** – Programming language
* **SQLAlchemy** – ORM for database operations
* **SQLite / MySQL** – Database
* **Pydantic** – Data validation
* **Uvicorn** – ASGI server


## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd fastapi_project
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install fastapi uvicorn sqlalchemy pydantic
```

### 4️⃣ Run the server

```
python -m uvicorn main:app --reload
```

---

## 🌐 API Documentation

Once the server is running, open:

👉 http://127.0.0.1:8000/docs

FastAPI provides interactive Swagger UI for testing APIs.

---

## 📌 API Endpoints

### 🔹 Category APIs

| Method | Endpoint               | Description         |
| ------ | ---------------------- | ------------------- |
| GET    | `/api/categories`      | Get all categories  |
| POST   | `/api/categories`      | Create new category |
| GET    | `/api/categories/{id}` | Get category by ID  |

---

### 🔹 Product APIs

| Method | Endpoint             | Description        |
| ------ | -------------------- | ------------------ |
| GET    | `/api/products`      | Get all products   |
| POST   | `/api/products`      | Create new product |
| GET    | `/api/products/{id}` | Get product by ID  |

---

## 🧪 Sample Request

### Create Category

```json
{
  "name": "Electronics"
}
```

### Create Product

```json
{
  "name": "Mobile",
  "price": 20000,
  "category_id": 1
}
```

---

## 🔗 Database Relationship

* One **Category** can have multiple **Products**
* `category_id` in Product acts as a **Foreign Key**

---

## 🎯 Features

* RESTful API design
* CRUD operations
* Database integration using ORM
* Data validation with Pydantic
* Modular project structure
* Auto-generated API docs

---

## ⚠️ Common Errors & Fixes

* **Module not found** → Install dependencies
* **Validation error (422)** → Check request body
* **Internal server error (500)** → Check backend logs

---

## 🚀 Future Improvements

* Update & Delete APIs
* Authentication (JWT)
* Pagination
* Search & filtering
* Deployment (Render / AWS)

---

## 👨‍💻 Author

**Bikash Mohanty**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
