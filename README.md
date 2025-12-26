
# AI-Based Face Recognition Attendance System 🎓🤖

An end-to-end **AI-powered attendance system** that uses **real-time face recognition** to automatically mark student attendance.  
Built using **Python, DeepFace (FaceNet), OpenCV, and Streamlit**, this project demonstrates a complete computer vision pipeline — from data collection to real-world deployment logic.

---

## 🚀 Features

- 🔍 **Live Face Recognition**
  - Real-time webcam-based face recognition
  - Uses DeepFace with pretrained **FaceNet** model
  - Automatically labels unknown faces

- 🧑‍🎓 **Student Registration**
  - Capture 20–30 face samples per student
  - Structured dataset creation
  - Easy to extend for new students

- 🕒 **Automatic Attendance Marking**
  - Subject-wise attendance
  - Date-based **duplicate prevention**
  - Attendance stored in CSV format

- 📊 **User-Friendly Interface**
  - Built with **Streamlit**
  - Simple teacher controls
  - Live feedback (Marked / Already Marked)

---

## 🧠 System Workflow

1. Register students by capturing face images  
2. Generate face embeddings using DeepFace (FaceNet)  
3. Start live recognition via webcam  
4. Recognized faces trigger attendance marking  
5. Attendance saved automatically with date & time  

---

## 🗂️ Project Structure

```
attendance_system/
│
├── app.py                     # Streamlit main app
├── config.py
│
├── features/
│   ├── register.py            # Student face registration
│   ├── recognize.py           # Live face recognition
│   └── attendance.py          # Attendance logic
│
├── utils/
│   ├── camera.py              # Webcam handler
│   └── helpers.py
│
├── data/
│   ├── students/              # Face image datasets
│   ├── attendance/            # Daily attendance CSV files
│   └── encodings.pkl          # Face embeddings
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <your-github-repo-url>
cd attendance_system
```

### 2️⃣ Create & Activate Virtual Environment (Windows)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 📁 Attendance Output

Attendance files are automatically generated here:

```
data/attendance/YYYY-MM-DD.csv
```

Example:
```csv
Name,Subject,Date,Time
001_Ali,AI,2025-01-15,10:45:32
```

---

## 🧪 Technologies Used

- **Python**
- **DeepFace**
- **FaceNet (Pretrained Model)**
- **OpenCV**
- **Streamlit**
- **NumPy & Pandas**

---

## 🧠 Key Learning Outcomes

- Practical face recognition pipeline
- Handling real-world AI integration issues
- Dataset creation & preprocessing
- Duplicate prevention logic
- Deployment-ready Streamlit applications

---

## 🔮 Future Enhancements

- 📊 Attendance analytics dashboard
- 🗄️ SQLite / Database integration
- 🛡️ Anti-spoofing (photo/video attack detection)
- 👥 Admin & role-based access
- ☁️ Cloud deployment

---
