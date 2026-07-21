# 🔐 Day 10 - Flask Authentication with MySQL, Docker & Nginx

> A production-style authentication system built using **Flask**, **MySQL**, **Docker**, and **Nginx Reverse Proxy**.

---

## 🚀 Tech Stack

- 🐍 Python 3.12
- 🌐 Flask
- 🗄️ MySQL 8.4
- 🐳 Docker
- 📦 Docker Compose
- 🌍 Nginx Reverse Proxy
- 🎨 HTML5
- 🎯 CSS3

---

## 📂 Project Structure

```text
day-10-authentication/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
│
├── nginx/
│   └── default.conf
│
├── templates/
│   ├── login.html
│   ├── index.html
│   └── edit.html
│
├── static/
│   └── style.css
│
└── screenshots/
    ├── login-page.png
    ├── dashboard.png
    └── employee-crud.png
```

---

# ✨ Features

- ✅ User Authentication
- ✅ Login System
- ✅ Session-Based Authentication
- ✅ Default Admin User
- ✅ Employee CRUD Operations
- ✅ MySQL Integration
- ✅ Dockerized Deployment
- ✅ Docker Compose Support
- ✅ Nginx Reverse Proxy
- ✅ Responsive UI
- ✅ Automatic Database Initialization

---

## 👤 Default Login Credentials

| Username | Password |
|----------|----------|
| **admin** | **admin123** |

---

## 🗄️ Database Schema

### Users Table

| Column | Type |
|--------|------|
| id | INT |
| username | VARCHAR(100) |
| password | VARCHAR(100) |

### Employees Table

| Column | Type |
|--------|------|
| id | INT |
| name | VARCHAR(100) |
| email | VARCHAR(100) |
| salary | INT |

---

# 🏗️ Architecture

```text
             Browser
                │
                ▼
      Nginx Reverse Proxy
                │
                ▼
        Flask Application
                │
                ▼
          MySQL Database
```

---

# 🐳 Docker Containers

| Container | Purpose |
|-----------|----------|
| flask-app | Flask Backend |
| mysql-db | MySQL Database |
| nginx | Reverse Proxy |

---

# ▶️ Getting Started

## Clone Repository

```bash
git clone https://github.com/<your-username>/devops-labs.git

cd day-10-authentication
```

---

## Build & Run

```bash
docker compose up --build -d
```

---

## Verify Running Containers

```bash
docker ps
```

---

## Stop Containers

```bash
docker compose down
```

---

# 🌐 Access Application

Open your browser and visit:

```text
http://<YOUR_PUBLIC_IP>
```

Example:

```text
http://34.xxx.xxx.xxx
```

---

# 📸 Screenshots

## 🔑 Login Page

```
screenshots/login-page.png
```

---

## 📊 Dashboard

```
screenshots/dashboard.png
```

---

## 👨‍💼 Employee Management

```
screenshots/employee-crud.png
```

---

# 📚 Learning Outcomes

During this project I learned:

- Flask Authentication
- Session Management
- MySQL Integration
- Docker Networking
- Docker Compose
- Nginx Reverse Proxy
- Database Initialization
- CRUD Operations
- Production-Level Debugging
- Container Troubleshooting

---

# 🐞 Challenges Solved

- ✅ Fixed 502 Bad Gateway
- ✅ Solved IndentationError
- ✅ Fixed "MySQL server has gone away"
- ✅ Resolved Docker Networking Issues
- ✅ Corrected Flask Startup Errors
- ✅ Successfully Implemented Authentication

---

# 🔮 Future Improvements

- 🔐 Password Hashing using bcrypt
- 👤 User Registration
- 🚪 Logout Feature
- 👥 Role-Based Authentication
- 📧 Forgot Password
- 📱 Mobile Responsive UI
- 📊 Admin Dashboard
- 📝 Audit Logs

---

# 🛠️ Useful Commands

```bash
# Build Containers
docker compose up --build -d

# Stop Containers
docker compose down

# Running Containers
docker ps

# Flask Logs
docker logs flask-app

# MySQL Logs
docker logs mysql-db

# Nginx Logs
docker logs nginx
```

---

# 🎯 Project Highlights

- 🔐 Secure Login System
- 🗄️ MySQL Database Integration
- 🐳 Fully Dockerized Application
- 🌍 Nginx Reverse Proxy
- 📦 Docker Compose Architecture
- 👨‍💼 Employee CRUD
- 🎨 Modern Responsive UI
- 🚀 Production-Style Deployment

---

# ⭐ Conclusion

This project demonstrates how to build and deploy a **containerized authentication system** using **Flask**, **MySQL**, **Docker**, **Docker Compose**, and **Nginx**. It provides practical experience in authentication, reverse proxy configuration, database integration, container orchestration, and real-world debugging.

---

## 👨‍💻 Author

**Aaditya Acharya**

**DevOps Engineer | Python | Docker | Flask | MySQL | Nginx | Linux | CI/CD | Cloud | Kubernetes (Learning)**

⭐ If you found this project useful, don't forget to star the repository!
