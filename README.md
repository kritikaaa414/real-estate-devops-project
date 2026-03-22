# 🏠 HomeHaven – Real Estate Full Stack DevOps Project

A complete Full-Stack Real Estate web application built using **React + Flask + MySQL** and deployed using **Docker & Docker Compose**.

This project demonstrates end-to-end DevOps workflow including containerization, database integration, and service orchestration.

---

## 🚀 Features

* View available properties
* Property images display
* Location and pricing details
* Backend API integration
* Database driven application
* Multi-container Docker setup

---

## 🧱 Tech Stack

### Frontend

* React (Vite)
* Axios
* CSS

### Backend

* Python Flask
* Flask-SQLAlchemy
* Flask-CORS

### Database

* MySQL 8

### DevOps

* Docker
* Docker Compose
* Nginx (for frontend serving)

---

## 🏗️ Architecture

Client (Browser)
⬇
React Frontend (Port 3000)
⬇
Flask Backend API (Port 5000)
⬇
MySQL Database (Port 3306)

---

## 📂 Project Structure

real-estate-fullstack/
│
├── frontend/ → React UI
├── backend/ → Flask API
├── docker-compose.yml → Multi-container setup
├── requirements.txt → Python dependencies
└── realestate_db.sql → Database schema & data

---

## ⚙️ How to Run Locally

### 1. Clone repo

git clone https://github.com/kritikaaa414/real-estate-devops-project.git

### 🔹 2. Run with Docker

Make sure Docker is installed on your system.

```
docker compose up --build
```

---

### 🔹 3. Access Application

* Frontend: http://localhost:3000
* Backend API: http://localhost:5000/properties

---

## ☁️ Deployment (AWS EC2)

### Steps:

1. Launch EC2 instance (Ubuntu)
2. Install Docker & Docker Compose
3. Clone repository
4. Run:

```
docker compose up --build -d
```

5. Open in browser:

```
http://<your-ec2-public-ip>:3000
```

---

## 📡 API Endpoints

### GET Properties

```
GET /properties
```

### Sample Response

```json
[
  {
    "title": "2BHK Apartment",
    "location": "Indore",
    "price": "5000",
    "image": "img1.jpg"
  }
]
```

---

## 🧪 Database Schema

| Field    | Type    |
| -------- | ------- |
| id       | Integer |
| title    | String  |
| location | String  |
| price    | String  |
| image    | String  |

---

## 🐳 Docker Services

* frontend → React App (Port 3000)
* backend → Flask API (Port 5000)
* db → MySQL (Port 3306)

---


---

## 📌 Future Improvements

* Add authentication (Login/Signup)
* Add property filters (price, location)
* Add image upload feature
* Deploy using CI/CD pipeline

 & Software Engineer
