#  Ecommerce API with JWT Authentication

A production-ready backend API built using **FastAPI**, **PostgreSQL**, and **JWT Authentication**.
This project demonstrates real-world backend engineering concepts including authentication, database integration, and deployment.

---

##  Live API

👉 https://your-app.onrender.com

👉 API Docs (Swagger):
https://your-app.onrender.com/docs

---

##  Features

* 🔐 User Authentication (JWT-based)
* 👤 User Signup & Login
* 📦 Product Listing API (Protected Route)
* 🧠 Dependency Injection (FastAPI)
* 🗄️ PostgreSQL Database Integration
* ⚡ FastAPI Auto Docs (/docs)
* ☁️ Deployed on Render

---

##  Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Auth:** JWT (JSON Web Tokens)
* **Validation:** Pydantic
* **Deployment:** Render
* **Environment:** Python Virtual Environment

---

## 📁 Project Structure

```
ecommerce-api/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│
│   ├── models/
│   │   ├── product.py
│   │   └── user.py
│
│   ├── routes/
│   │   ├── product_routes.py
│   │   └── auth_routes.py
│
│   ├── schemas/
│   │   ├── product_schema.py
│   │   └── auth_schema.py
│
│   ├── utils/
│   │   ├── auth.py
│   │   ├── jwt.py
│   │   └── security.py
│
├── scripts/
│   └── load_data.py
│
├── data/
│   └── dataset.csv
│
├── requirements.txt
├── Procfile
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ecommerce-api.git
cd ecommerce-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost/ecommerce
SECRET_KEY=your_secret_key
```

---

### 5️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

---

## 🔐 Authentication Flow

1. **Signup**

```http
POST /auth/signup
```

2. **Login**

```http
POST /auth/login
```

👉 Returns JWT token

3. **Authorize**

* Click 🔐 Authorize in `/docs`
* Enter:

```
Bearer <your_token>
```

4. **Access Protected Routes**

```http
GET /products/
```

---

## 📊 Sample API Endpoints

| Method | Endpoint     | Description              |
| ------ | ------------ | ------------------------ |
| POST   | /auth/signup | Register user            |
| POST   | /auth/login  | Login & get token        |
| GET    | /products/   | Get products (Protected) |
| GET    | /            | Health check             |

---

##  Key Learnings

* Building REST APIs using FastAPI
* Implementing JWT Authentication
* Structuring scalable backend projects
* Integrating PostgreSQL with SQLAlchemy
* Deploying backend to cloud (Render)
* Debugging real-world deployment issues

---

##  Future Improvements

*  Add Cart & Orders API
*  Pagination & Filtering improvements
*  Search functionality
*  Unit & Integration Testing
*  Dockerization

---

##  Contribution

Feel free to fork and improve the project!

---


##  If you like this project

Give it a ⭐ on GitHub — it helps a lot!
