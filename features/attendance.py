# attendance helper function included in this file
import os
import pandas as pd
from datetime import datetime

def mark_attendance(student_name, subject):
    subject_dir = f"data/attendance/{subject}"
    os.makedirs(subject_dir, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    time_now = datetime.now().strftime("%H:%M:%S")

    file_path = f"{subject_dir}/{today}.csv"

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=["Name", "Date", "Time"])

    # Prevent duplicate attendance (same student, same day)
    if not ((df["Name"] == student_name) & (df["Date"] == today)).any():
        df.loc[len(df)] = [student_name, today, time_now]
        df.to_csv(file_path, index=False)
        return True
    else:
        return False
