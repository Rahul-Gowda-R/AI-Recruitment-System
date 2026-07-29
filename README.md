# 🚀 RecruitAI – Intelligent Recruitment Platform

RecruitAI is a full-stack recruitment platform that simplifies and enhances the hiring process using **Artificial Intelligence**, **Natural Language Processing (NLP)**, and **Computer Vision**. Built with **Flask**, **MySQL**, **OpenCV**, and **Scikit-learn**, it enables recruiters to screen resumes, conduct online assessments, monitor interviews, and identify the most suitable candidates efficiently.

---

# ✨ Features

### 📄 AI-Assisted Resume Screening

* ATS-based resume evaluation
* PDF resume parsing
* TF-IDF and Cosine Similarity scoring
* Keyword matching against job descriptions
* Resume ranking based on relevance

### 🧪 Online Skill Assessment

* Interactive aptitude and technical tests
* Candidate response tracking
* Performance evaluation
* Automated result processing

### 🎥 Interview Monitoring

* Live webcam integration
* Face monitoring using OpenCV
* Browser tab-switch detection
* Suspicious activity logging
* Helps maintain assessment integrity

### 💼 Job Recommendation

* Job matching based on skills
* Location-based opportunity filtering
* Personalized recommendations

### 🔐 Authentication

* Secure registration and login
* Password hashing with Flask-Bcrypt
* Session management

---

# 🛠️ Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Backend Development  |
| Flask        | Web Framework        |
| MySQL        | Database             |
| HTML5        | Frontend             |
| CSS3         | Styling              |
| JavaScript   | Client-side Logic    |
| OpenCV       | Interview Monitoring |
| Scikit-learn | ATS Resume Scoring   |
| NLTK         | Text Preprocessing   |
| PyMuPDF      | Resume Parsing       |
| Flask-Bcrypt | Authentication       |

---

# 📂 Project Structure

```text
RecruitAI/
│
├── app.py                  # Main Flask application
├── index.py                # Resume processing logic
├── resume_parser.py        # PDF text extraction
├── requirements.txt
│
├── templates/
│   ├── auth.html
│   ├── ats.html
│   ├── interview.html
│   ├── resume.html
│   ├── test.html
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

# 🚀 Key Modules

### 📑 ATS Resume Analysis

The system extracts text from uploaded resumes and compares it with a job description using:

* Text preprocessing (NLTK)
* TF-IDF Vectorization
* Cosine Similarity
* Keyword Matching

A weighted ATS score is then generated to rank candidates.

---

### 🧪 Skill Assessment

Candidates complete online assessments while the system records responses and calculates performance scores.

---

### 🎥 Interview Monitoring

OpenCV captures webcam input during interviews to support basic monitoring, while browser tab-switch detection helps discourage dishonest behavior.

---

### 🔐 Authentication

Recruiters and candidates can securely register and log in using encrypted passwords managed with Flask-Bcrypt.

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Rahul-Gowda-R/AI-Recruitment-System.git
cd AI-Recruitment-System
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL

Create a database:

```sql
CREATE DATABASE recruitai;
```

Update the MySQL credentials in `app.py`:

```python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_PASSWORD",
    "database": "recruitai"
}
```

### Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:8000
```

---

# 🧠 System Workflow

```text
Candidate Registration
          │
          ▼
Resume Upload
          │
          ▼
Resume Parsing
          │
          ▼
ATS Score Calculation
          │
          ▼
Online Skill Test
          │
          ▼
Interview Monitoring
          │
          ▼
Candidate Evaluation
          │
          ▼
Recruitment Decision
```

---

# 📸 Screenshots

Add screenshots inside a `screenshots/` directory.

Example:

```markdown
![Login](screenshots/login.png)

![ATS Dashboard](screenshots/ats.png)

![Skill Test](screenshots/test.png)

![Interview](screenshots/interview.png)
```

---

# 🚀 Future Enhancements

* AI-generated interview questions
* Resume improvement suggestions
* LLM-powered candidate summaries
* Video interview transcription
* Emotion and sentiment analysis
* Recruiter analytics dashboard
* Email notifications
* Multi-role recruiter support
* Cloud deployment
* Advanced candidate ranking

---

# 📚 Learning Outcomes

* Full-stack web development using Flask
* Resume parsing and document processing
* NLP for ATS resume matching
* Computer vision with OpenCV
* Authentication and session management
* Database integration with MySQL
* AI-assisted recruitment workflows

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 👨‍💻 Author

**Rahul Gowda R**

* GitHub: https://github.com/Rahul-Gowda-R
* LinkedIn: https://www.linkedin.com/in/rahulgowdar/

---

# 📄 License

This project is intended for educational and research purposes.

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub and sharing your feedback!
