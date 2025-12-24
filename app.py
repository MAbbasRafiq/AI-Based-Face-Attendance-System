import streamlit as st
from features.register import register_student
from features.recognize import detect_faces

st.set_page_config(page_title="AI Attendance System")

st.title("AI-Based Face Recognition Attendance System")

menu = st.selectbox(
    "Select Action",
    ["Face Detection", "Register Student"]
)

if menu == "Face Detection":
    if st.button("Start Detection"):
        detect_faces()

elif menu == "Register Student":
    student_id = st.text_input("Student ID")
    student_name = st.text_input("Student Name")

    if st.button("Register Face"):
        if student_id and student_name:
            st.warning("Press Q to stop camera early")
            register_student(student_id, student_name)
            st.success("Student registered successfully!")
        else:
            st.error("Please enter both ID and Name")









# Adding std name,reg etc to database after this
# import streamlit as st
# from features.recognize import detect_faces

# st.set_page_config(page_title="AI Attendance System")

# st.title("AI-Based Face Recognition Attendance System")

# if st.button("Start Face Detection"):
#     st.warning("Press Q to stop camera")
#     detect_faces()
