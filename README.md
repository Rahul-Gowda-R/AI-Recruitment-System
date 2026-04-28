# 🚀 AI-Powered Recruitment System

## 📌 Overview

The **AI-Powered Recruitment System** is a full-stack web application designed to automate and enhance the hiring process. It combines **Artificial Intelligence, Natural Language Processing (NLP), and Web Development** to evaluate resumes, conduct skill-based assessments, and monitor candidate behavior during interviews.

This system helps recruiters make smarter decisions by analyzing resumes, scoring candidates using ATS logic, and ensuring fairness through anti-cheating mechanisms.

---

## 🔥 Key Features

### 🔐 User Authentication

* Secure registration and login system
* Password hashing using Flask-Bcrypt
* Session-based authentication

### 📄 Resume Analysis (ATS Scoring)

* Extracts text from resumes (PDF/Image)
* Uses NLP techniques (TF-IDF + Cosine Similarity)
* Calculates ATS score based on job description
* Keyword matching + semantic similarity

### 🧪 Skill-Based Testing System

* Dynamic question generation based on difficulty
* Stores user responses in database
* Tracks performance

### 🚨 Anti-Cheating Detection

* Detects tab switching during tests
* Logs suspicious activity in database
* Auto-submit after multiple violations

### 🎥 Live Interview Monitoring

* Real-time video capture using OpenCV
* Face tracking and monitoring
* Simulates real interview environment

### 💼 Job Matching System

* Suggests jobs based on role and location
* Filters opportunities dynamically

---

## 🛠️ Tech Stack

### 💻 Frontend

* HTML
* CSS
* JavaScript

### ⚙️ Backend

* Python (Flask)

### 🧠 AI / ML

* Natural Language Processing (NLTK)
* TF-IDF Vectorization
* Cosine Similarity (Scikit-learn)

### 🗄️ Database

* MySQL

### 📦 Other Libraries

* OpenCV (Computer Vision)
* Flask-Bcrypt (Authentication Security)
* PDF/Text Processing Libraries

---

## 🗂️ Project Structure

```
RecruitAi/
│── app.py
│── index.py
│── resume_parser.py
│── templates/
│── static/
│── uploads/
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/AI-Recruitment-System.git
cd AI-Recruitment-System
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MySQL

* Create a database:

```sql
CREATE DATABASE recruitai;
```

* Update database config in `app.py`:

```python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "recruitai"
}
```

### 5️⃣ Run the application

```bash
python app.py
```

### 6️⃣ Open in browser

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots (Add your images here)

```
/screenshots/login.png
/screenshots/ats-score.png
/screenshots/skill-test.png
/screenshots/dashboard.png
```

---

## 🧠 How It Works

1. User registers and logs in
2. Uploads resume + enters job description
3. System extracts and preprocesses text
4. ATS score is calculated using NLP
5. User takes skill-based test
6. System tracks behavior and prevents cheating
7. Results are stored in MySQL database

---

## 🚀 Future Enhancements

* 📊 User dashboard with analytics
* 📈 Resume score history tracking
* 🌐 Deployment on cloud (AWS/Render)
* 🤖 AI interview assistant (voice-based)
* 📱 Mobile-friendly UI

---

## 👨‍💻 Author

**Rahul Gowda R**

* Engineering Student | AI & Web Developer
* Passionate about building real-world tech solutions

---

## 🌟 Acknowledgement

This project demonstrates the integration of **AI + Full Stack Development + Database Systems** to solve real-world recruitment challenges.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it

---

> “Focused effort with clarity leads to powerful results.”
