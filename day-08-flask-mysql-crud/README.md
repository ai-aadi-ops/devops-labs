# Day 08 - Flask + MySQL CRUD using Docker Compose

## Project Overview

This project demonstrates a multi-container application using Docker Compose.

The application is built with Flask and MySQL and provides complete CRUD functionality.

## Technologies Used

- Python 3.12
- Flask
- MySQL 8.4
- Docker
- Docker Compose

## Features

- Add Employee
- View Employees
- Edit Employee
- Delete Employee
- Automatic MySQL table creation
- Persistent MySQL storage using Docker Volume

## Project Structure

```text
day-08-flask-mysql-crud/
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── templates/
    ├── index.html
    └── edit.html
```

## Run

```bash
docker compose up --build
```

## Access

Application:

```
http://<VM_EXTERNAL_IP>:5000
```

## Database

- Host: mysql
- Database: employee_db

## CRUD Operations

- Create Employee
- Read Employee
- Update Employee
- Delete Employee

## Learning Outcomes

- Docker Compose
- Flask
- MySQL Integration
- CRUD Operations
- Docker Networking
- Docker Volumes
