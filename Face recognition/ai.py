import cv2 
import numpy as np
from random import randrange

#classifier is just a fancy word for face detector
trained_face_data = cv2.CascadeClassifier('trainingfaces.xml') 

#img = cv2.imread('test.png') #load image to detect faces in
webcam = cv2.VideoCapture(0) #load video feed

while True:
    successful_frame_read, frame = webcam.read()
    
    grescaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#turning image to greyscale as hardcastle only works on greyscale images

    face_coordinates = trained_face_data.detectMultiScale(grescaled_img)#detect faces

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h) , (randrange(255), randrange(255), randrange(255)), 2)

    cv2.imshow('Random ass joshi face detector', frame)#to view the image
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
    	break
webcam.release()#released the webcam object

