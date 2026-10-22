# Student Management System – React & Django

A full-stack **Student Management System** built using React and Django REST Framework to perform CRUD (Create, Read, Update, Delete) operations on student data. The application provides a simple interface to add, view, update, and delete student records.

## 🚀 Features

- **Add Student:** Register new students with their details.
- **View Students:** Display student records in a structured format.
- **Update Student:** Edit existing student information.
- **Delete Student:** Remove student records when required.
- **REST API Integration:** Connect the React frontend with the Django backend.
- **Responsive UI:** Simple and user-friendly interface.
- **Database Management:** Store and manage student information through Django models.

## 🛠️ Technologies Used

### Frontend
- React.js
- JavaScript
- HTML5
- CSS3
- Axios
- React Router
- React Toastify
- Vite

### Backend
- Python
- Django
- Django REST Framework
- Django CORS Headers

### Database
- SQLite or the database configured in the Django project.

## 📂 Project Structure

```text
React_Django/
├── Backend/
│   ├── enrollment/
│   └── test/                 # Local virtual environment (not uploaded)
│
├── Frontend/
│   └── JFS_Enrollment-main/
│       ├── public/
│       ├── src/
│       │   ├── components/
│       │   ├── pages/
│       │   └── styles/
│       ├── package.json
│       └── vite.config.js
│
├── .gitignore
└── README.md
```

*Note: The exact backend structure may vary depending on your Django configuration.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Vishal4046/React-_Django_Project.git
cd React-_Django_Project
```

### 2. Set Up the Django Backend

Open a terminal and navigate to the Django project directory containing `manage.py`.

Create and activate a virtual environment if you do not already have one:

**Windows:**

```powershell
python -m venv venv
venv\Scripts\activate
```

Install the required packages:

```bash
pip install django djangorestframework django-cors-headers
```

Run database migrations:

```bash
python manage.py migrate
```

Start the backend server:

```bash
python manage.py runserver
```

The Django backend runs at:

`http://127.0.0.1:8000/`

### 3. Set Up the React Frontend

Open another terminal:

```bash
cd Frontend/JFS_Enrollment-main
npm install
npm run dev
```

The Vite development server typically runs at:

`http://localhost:5173/`

Open the URL shown in your terminal to access the application.

## 🔄 CRUD Operations

| Operation | Description |
|---|---|
| Create | Add a new student record |
| Read | View all registered students |
| Update | Modify existing student details |
| Delete | Remove a student record |

## 👨‍🎓 Student Details

The application manages the following student information:

- Name
- Email
- Mobile Number
- Department
- Course

## 🔗 API Integration

The React frontend communicates with the Django backend using Axios HTTP requests.

Typical operations include:

- `POST` – Add a student
- `GET` – Retrieve student records
- `PUT` – Update student details
- `DELETE` – Delete a student record

The exact API endpoint paths depend on the URL configuration in the Django backend.

## 🎯 Project Objective

The objective of this project is to demonstrate full-stack web development by integrating a React frontend with a Django REST API to manage student records efficiently.

## 👨‍💻 Author

**Vishal Iragouda Patil**

- GitHub: [Vishal4046](https://github.com/Vishal4046)
- Project Repository: [React_Django_Project](https://github.com/Vishal4046/React-_Django_Project)

---

If you find this project useful, feel free to explore the code and learn from it.
