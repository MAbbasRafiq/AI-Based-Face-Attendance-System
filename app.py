import streamlit as st
from features.register import register_student
from features.recognize import detect_faces, encode_faces
from features.recognize import recognize_live

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Attendance System",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("AI-Based Face Recognition Attendance System")

# ---------------- MENU ----------------
menu = st.selectbox(
    "Select Action",
    ["Face Detection",
     "Register Student",
     "Live Face Recognition (Attendance)"]
)

# =========================
# FACE DETECTION SECTION
# =========================
if menu == "Face Detection":
    if st.button("Start Detection"):
        st.warning("Press Q to stop camera")
        detect_faces()

# =========================
# REGISTER STUDENT SECTION
# =========================
elif menu == "Register Student":
    st.subheader("Student Registration")

    student_id = st.text_input("Student ID")
    student_name = st.text_input("Student Name")

    # ---- REGISTER FACE BUTTON ----
    if st.button("Register Face"):
        if student_id and student_name:
            st.warning("Press Q to stop camera early")
            register_student(student_id, student_name)
            st.success("Student registered successfully!")
        else:
            st.error("Please enter both ID and Name")

    # ---- SEPARATOR ----
    st.divider()

    # ---- GENERATE ENCODINGS BUTTON ----
    if st.button("Generate Face Encodings"):
        count = encode_faces()
        st.success(f"{count} face embeddings generated successfully!")
elif menu == "Live Face Recognition (Attendance)":
    subject = st.text_input("Enter Subject Name")

    if st.button("Start Attendance"):
        if subject:
            st.warning("Press Q to stop camera")
            recognize_live(subject)
        else:
            st.error("Please enter subject name")


