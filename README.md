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

git clone https://github.com/vidhi4104/real-estate-fullstack.git

### 2. Go inside project

cd real-estate-fullstack

### 3. Run docker

docker compose up --build

### 4. Open in browser

http://localhost:3000

---

## 📡 API Endpoint

http://localhost:5000/api/properties

---

## 🎯 DevOps Concepts Used

* Containerization
* Multi-service architecture
* Service networking
* Persistent database setup
* Environment isolation
* Build automation

---



Aspiring DevOps & Software Engineer
