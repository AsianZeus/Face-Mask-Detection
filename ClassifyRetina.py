from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from RetinaFace_Detector import RetinaFace

model = load_model("Models/mask_detector.model")

def classify(image):
    count= 0
    labels = []
    obj = RetinaFace.detect_faces(image)
    for key in obj:
        count+=1
        identity = obj[key]
        facial_area = identity["facial_area"]
        face = image[facial_area[1]: facial_area[3], facial_area[0]: facial_area[2]]
        (startX, startY, endX, endY) = (facial_area[0], facial_area[1], facial_area[2], facial_area[3])
        face = cv2.resize(face, (224, 224))
        face = img_to_array(face)
        face = preprocess_input(face)
        face = np.expand_dims(face, axis=0)
        (mask, withoutMask) = model.predict(face)[0]
        label = "Mask" if mask > withoutMask else "No Mask"
        labels.append(label)
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
        cv2.putText(image, label, (startX, startY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
    return (count, labels, image)