import cv2
from utils.camera import get_camera
# for function 2
import os
import pickle
from deepface import DeepFace

def detect_faces():
    face_cascade = cv2.CascadeClassifier(
        "data/haarcascade_frontalface_default.xml"
    )

    cap = get_camera()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    

def encode_faces():
    dataset_path = "data/students"
    encodings = []
    names = []

    for student_folder in os.listdir(dataset_path):
        student_path = os.path.join(dataset_path, student_folder)

        if not os.path.isdir(student_path):
            continue

        for img_name in os.listdir(student_path):
            img_path = os.path.join(student_path, img_name)

            try:
                embedding = DeepFace.represent(
                    img_path=img_path,
                    model_name="Facenet",
                    enforce_detection=False
                )

                encodings.append(embedding[0]["embedding"])
                names.append(student_folder)

            except Exception as e:
                print(f"Skipping {img_path}: {e}")

    data = {
        "encodings": encodings,
        "names": names
    }

    with open("data/encodings.pkl", "wb") as f:
        pickle.dump(data, f)

    return len(encodings)
