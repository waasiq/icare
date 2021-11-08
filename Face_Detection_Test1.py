"""
! Advanced Computer Vision FreeCodeCamp  
* Chapter 3: Face Detection - Basics
"""

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("videos/3.mp4") 
# cap = cv2.VideoCapture(0)
width = 1180
height = 720
dim = (width,height)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()


while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    # print(results) # brings up the classes

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection) 
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
    
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    # cv2.imshow("Image", resized)
    cv2.imshow("Image", img)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

