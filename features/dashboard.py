import os
import pandas as pd
import streamlit as st

ATTENDANCE_ROOT = "data/attendance"

def show_dashboard():
    st.subheader("📊 Attendance Dashboard")

    if not os.path.exists(ATTENDANCE_ROOT):
        st.info("No attendance data available yet.")
        return

    subjects = os.listdir(ATTENDANCE_ROOT)
    if not subjects:
        st.info("No subjects found.")
        return

    subject = st.selectbox("Select Subject", subjects)

    subject_path = os.path.join(ATTENDANCE_ROOT, subject)
    dates = sorted(os.listdir(subject_path), reverse=True)

    if not dates:
        st.warning("No attendance files for this subject.")
        return

    date = st.selectbox("Select Date", dates)

    file_path = os.path.join(subject_path, date)
    df = pd.read_csv(file_path)

    # Summary
    st.markdown("### 📌 Summary")
    st.metric("Total Present", len(df))

    # Table
    st.markdown("### 📋 Attendance Records")
    st.dataframe(df)

    # Chart
    st.markdown("### 📈 Attendance Chart")
    chart_df = df["Name"].value_counts()
    st.bar_chart(chart_df)

    # Download
    with open(file_path, "rb") as f:
        st.download_button(
            label="⬇ Download CSV",
            data=f,
            file_name=f"{subject}_{date}",
            mime="text/csv"
        )
