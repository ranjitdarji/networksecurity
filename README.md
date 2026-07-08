# 🛡️ Network Security - Phishing Website Detection System

A Machine Learning based web application that detects whether a website is **Safe** or **Phishing** using a trained classification model.

The project provides a modern Streamlit dashboard for prediction and a FastAPI backend for model inference.

---

# 📌 Features

- 📂 Upload CSV Dataset
- 🤖 Machine Learning Prediction
- ⚡ FastAPI Backend
- 🎨 Interactive Streamlit Dashboard
- 📊 Prediction Analytics
- 🥧 Pie Chart & Bar Chart
- 📥 Download Prediction Report
- 🗄️ MongoDB Atlas Integration
- 📈 MLflow Model Tracking

---

# 🛠️ Tech Stack

### Programming Language
- Python

### Frontend
- Streamlit

### Backend
- FastAPI

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy

### Database
- MongoDB Atlas

### Model Tracking
- MLflow

### Visualization
- Plotly Express

---

# 📂 Project Structure

```
NetworkSecurity/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── final_model/
├── prediction_output/
├── assets/
├── templates/
└── networksecurity/
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/ranjitdarji/NetworkSecurity.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶ Run FastAPI Backend

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# ▶ Run Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

---

# 📊 Workflow

```
CSV Dataset
      │
      ▼
Upload Dataset
      │
      ▼
FastAPI Backend
      │
      ▼
Preprocessing
      │
      ▼
Machine Learning Model
      │
      ▼
Prediction
      │
      ▼
Streamlit Dashboard
      │
      ▼
Download Prediction Report
```

---

# 🎯 Prediction Labels

| Prediction | Meaning |
|------------|---------|
| 0 | Safe Website |
| 1 | Phishing Website |

---

# 📈 Dashboard Features

- image: D:\udemyfinal\NetworkSecurity\deshboard.png

- Dashboard Overview
- Prediction Summary
- Dataset Information
- Pie Chart
- Bar Chart
- Search Prediction Results
- Download CSV Report

---

# 🎯 Future Improvements

-image: D:\udemyfinal\NetworkSecurity\prediction (2).png , D:\udemyfinal\NetworkSecurity\prediction3.png , D:\udemyfinal\NetworkSecurity\prediction4.png

- URL Prediction using Text Input
- User Authentication
- Cloud Deployment (AWS)
- Docker Support
- Email Alerts
- Real-time Website Detection

---

# 👨‍💻 Developer

- image: D:\udemyfinal\NetworkSecurity\about.png

**Ranjit Darji**

Final Year Engineering Student

Machine Learning | Data Science | MLOps

---

# ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.



