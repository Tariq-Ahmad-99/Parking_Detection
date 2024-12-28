import cv2
import pickle
import numpy as np
from tensorflow.keras.models import load_model # type: ignore

# Load the trained model

model = load_model('model/model_final.h5')
class_dictionary = {0: 'no_car', 1: 'car'}

video = cv2.VideoCapture("assets/car_test.mp4")

with open('model/carposition.pkl', 'rb') as f:
    positionList = pickle.load(f)

width = 130
height = 65

def checkingCarParking(img):
    imgCrops = []
    spaceCounter = 0
    for pos in positionList:
        x, y = pos
        cropped_img = img[y:y+height, x:x+width]
        imgResized = cv2.resize(cropped_img, (48,48))
        imgNormalized = imgResized / 255.0
        imgCrops.append(imgNormalized)
    imgCrops = np.array(imgCrops)
    predictions = model.predict(imgCrops)

    # Draw a rectangle on the image
    for i, pos in enumerate(positionList):
        x, y = pos
        inId = np.argmax(predictions[i])
        label = class_dictionary[inId]
        if label == 'no_car':
            color = (0,255,0)
            thickness = 2
            spaceCounter += 1
        else:
            color = (0,0,255)
            thickness = 2

        cv2.rectangle(image, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), thickness)
        cv2.putText(image, label, (x, y+height-3), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), thickness)

while True:
    if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ret, image = video.read()
    image = cv2.resize(image, (1280,720))
    if not ret:
        break

    checkingCarParking(image)
    cv2.imshow("image", image)
    if cv2.waitKey(10) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
