# 🧠 AI-Based Face Recognition Attendance System

## 📌 Project Overview

The **AI-Based Face Recognition Attendance System** is a computer vision–based application that detects and recognizes faces in real time using a webcam.  
This project is being developed in a structured, feature-by-feature manner to demonstrate the practical use of deep learning and computer vision.

> Current Status:  
> Face detection, student registration, face encoding, and live face recognition are completed.  


---

## 🎯 Objectives

- Automate attendance using face recognition
- Eliminate manual and proxy attendance
- Apply pretrained deep learning models in a real-world system
- Build a modular and scalable AI application

---

## ✅ Implemented Features (Till Now)

### 1. Face Detection
- Real-time face detection using webcam
- Haar Cascade classifier for detecting faces
- Bounding boxes drawn around detected faces

### 2. Student Face Registration
- Register students using Student ID and Name
- Capture 20–30 face images per student
- Automatic dataset creation

Dataset structure:
```
data/students/
├── 001_Ali/
│   ├── img_1.jpg
│   ├── img_2.jpg
│   └── ...
├── 002_Sara/
│   ├── img_1.jpg
│   └── ...
```

### 3. Face Encoding
- Uses DeepFace with pretrained FaceNet model
- Converts face images into 512-dimensional embeddings
- Encodings stored in a pickle file

File generated:
```
data/encodings.pkl
```

### 4. Live Face Recognition
- Real-time face recognition via webcam
- Uses DeepFace `find()` pipeline
- Displays student name or "Unknown"

---

## 🛠️ Tech Stack

- Python
- OpenCV
- DeepFace (FaceNet)
- Streamlit
- NumPy, Pandas
- Python Virtual Environment (venv)

---

## 📂 Project Structure

```
attendance_system/
├── app.py
├── config.py
├── features/
│   ├── register.py
│   ├── recognize.py
│   └── attendance.py   # To be implemented
├── utils/
│   ├── camera.py
│   └── helpers.py
├── data/
│   ├── students/
│   ├── attendance/
│   ├── encodings.pkl
│   └── haarcascade_frontalface_default.xml
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Create Virtual Environment
```
python -m venv venv
```

### 2. Activate Virtual Environment (Windows)
```
venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Application
```
streamlit run app.py
```

---

## 🧠 Face Recognition Approach

- Pretrained FaceNet model is used via DeepFace
- Each face is represented as a 512-dimensional embedding
- DeepFace internal pipeline ensures face detection, alignment, and comparison

---

## 📌 Project Status

- Face Detection: Completed
- Student Registration: Completed
- Face Encoding: Completed
- Live Face Recognition: Completed
- Attendance Marking: In Progress

---

## 🔮 Upcoming Features

- Attendance marking (CSV / database)
- Duplicate attendance prevention
- Subject-wise attendance
- Teacher dashboard
- Reports and analytics

---


Project is actively under development.
