import cv2
import pickle
import numpy as np
from tensorflow.keras.models import load_model # type: ignore

# Load the trained model

model = load_model('model/model_final.h5')
class_dictionary = {0: 'no_car', 1: 'car'}

video = cv2.VideoCapture("assets/parkingvideo.mp4")

with open('model/carposition.pkl', 'rb') as f:
    positionList = pickle.load(f)
