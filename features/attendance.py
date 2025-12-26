# attendance helper function included in this file
import os
import pandas as pd
from datetime import datetime

ATTENDANCE_DIR = "data/attendance"

def mark_attendance(student_name, subject):
    os.makedirs(ATTENDANCE_DIR, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")

    file_path = f"{ATTENDANCE_DIR}/{today}.csv"

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=["Name", "Subject", "Date", "Time"])

    # Duplicate check
    if not ((df["Name"] == student_name) & (df["Date"] == today)).any():
        df.loc[len(df)] = [student_name, subject, today, time_now]
        df.to_csv(file_path, index=False)
        return True
    else:
        return False
