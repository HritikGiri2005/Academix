# Academix — Student–Teacher Portal

**Academix** is a Django-based Student–Teacher Portal designed to provide a centralized platform for managing interactions and academic activities between students and teachers.

The project demonstrates the development of a role-based educational web application using **Python and Django**, with server-side rendering, database integration, templates, static assets, and structured Django application architecture.

---

## 📌 Overview

Academix provides a foundation for an academic management portal where different users can interact with the system based on their role.

The project focuses on building practical Django functionality around:

* Student management
* Teacher management
* User authentication
* Academic information
* Database-driven functionality
* Django templates
* Static file management
* Role-oriented application workflows

---

## ✨ Key Features

### 👨‍🎓 Student Portal

Students can access their academic information through the portal and interact with functionality provided by the application.

Potential student workflows include:

* Student profile management
* Academic information
* Access to teacher-provided content
* Student-specific dashboard functionality

### 👨‍🏫 Teacher Portal

Teachers have access to functionality designed for managing student-related academic activities.

Features include:

* Teacher profile management
* Student-related information
* Academic content management
* Teacher-specific workflows

### 🔐 Authentication & User Management

The application is designed around different user types and provides the foundation for role-based access.

Key concepts include:

* User authentication
* Login/logout workflows
* User-specific access
* Student and teacher roles

---

## 🛠️ Technology Stack

### Backend

* **Python**
* **Django**

### Frontend

* **HTML**
* **CSS**
* **Django Templates**

### Database

* Django ORM
* SQLite / relational database configuration

### Development Tools

* Git
* GitHub
* Visual Studio Code

---

## 🏗️ Project Architecture

The application follows the standard Django architecture:

```text
Academix
│
├── manage.py
│
├── Academix/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── testapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── template/
│   └── testapp/
│
└── static/
```

---

## 🔄 Application Flow

The general application flow is:

```text
                    Academix
                       │
             ┌─────────┴─────────┐
             │                   │
          Student              Teacher
             │                   │
             └─────────┬─────────┘
                       │
                  Django Views
                       │
                  Django ORM
                       │
                    Database
```

---

## 📚 Django Concepts Demonstrated

This project provides practical experience with several important Django concepts:

* Django project structure
* Django applications
* URL routing
* Views
* Templates
* Static files
* Models
* Django ORM
* Database operations
* Forms
* Authentication
* User roles
* Django migrations
* Admin interface
* Request/response handling

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3.x
* pip
* Git

Verify Python:

```bash
python --version
```

Verify pip:

```bash
pip --version
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/HritikGiri2005/Academix.git
```

### 2. Navigate to the project

```bash
cd Academix
```

### 3. Create a virtual environment

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install Django:

```bash
pip install django
```

---

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal.

---

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🗄️ Database

Academix uses Django's ORM for database interaction.

The application follows the standard Django database workflow:

```text
Django Models
      ↓
Django ORM
      ↓
Database
      ↓
Query Results
      ↓
Django Views
      ↓
Templates
```

This approach keeps database operations integrated with the Django application layer.

---

## 🎯 Learning Objectives

The project was developed to gain practical experience in building a database-driven web application using Django.

Key learning areas include:

* Building a complete Django application
* Structuring Django projects
* Working with models and databases
* Implementing user-based workflows
* Connecting views with templates
* Managing static resources
* Understanding Django's request/response lifecycle
* Building applications around different user roles

---

## 🔮 Future Enhancements

Possible improvements for Academix include:

* Student attendance management
* Assignment management
* Examination and quiz modules
* Marks and grade management
* Teacher dashboard
* Student dashboard
* Course/subject management
* Notifications
* Search and filtering
* Django REST Framework APIs
* PostgreSQL integration
* Role-based permissions
* Production deployment
* Automated testing

---

## 📸 Screenshots

Screenshots can be added here to showcase the main interfaces.

Example:

```text
docs/
├── login.png
├── student-dashboard.png
├── teacher-dashboard.png
└── profile.png
```

Then display them in the README:

```markdown
![Login](docs/login.png)
![Student Dashboard](docs/student-dashboard.png)
![Teacher Dashboard](docs/teacher-dashboard.png)
```

---

## 💡 Project Highlights

* Built using **Python and Django**
* Student–Teacher oriented application
* Database-driven architecture
* Django ORM integration
* Server-side rendered templates
* Structured Django project architecture
* Authentication and user-oriented workflows
* Practical implementation of Django fundamentals

---

## 👨‍💻 Author

**Hritik Giri**

Aspiring Python Backend Developer

### Technical Focus

```text
Python
Django
Django REST Framework
SQL
REST APIs
Backend Development
```

GitHub:
https://github.com/HritikGiri2005

---

## ⭐ Conclusion

Academix is a practical Django project demonstrating how a **Student–Teacher Portal** can be structured using Python and Django.

The project serves as a foundation for expanding into a complete educational management platform with additional modules such as attendance, assignments, examinations, grades, notifications, and REST APIs.
