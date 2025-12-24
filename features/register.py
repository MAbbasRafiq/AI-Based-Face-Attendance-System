import cv2
import os
from utils.camera import get_camera

def register_student(student_id, student_name, img_count=25):
    save_path = f"data/students/{student_id}_{student_name}"
    os.makedirs(save_path, exist_ok=True)

    face_cascade = cv2.CascadeClassifier(
        "data/haarcascade_frontalface_default.xml"
    )

    cap = get_camera()
    count = 0

    while count < img_count:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            img_name = f"{save_path}/img_{count+1}.jpg"
            cv2.imwrite(img_name, face_img)
            count += 1

            cv2.rectangle(frame, (x, y),
                          (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Registering Face", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
