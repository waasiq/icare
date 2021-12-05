"""
!                                               -----   "Finger Flip" Easter Egg  -----

TODO Ideas and Problems:
    * (mention other problems...)
"""

import cv2
import mediapipe as mp
import time
import math
from Modules.HandTrackingModule import handDetector

#! Global Variables
#* Default Dimensions for Webcam: 1280 x 720 / Dimensions for Test Videos:  700 x 925
WIDTH = 1280
HEIGHT = 720
DIMENTION = (WIDTH, HEIGHT)

def fingerFlipDetection(img, landmarkList):
    if len(landmarkList) != 0:
        # print(landmarkList[4],landmarkList[8]) # getting only values of landmark no 2
        
        #* Coordinations of 2 landmarks we want to work with and the center of the distance
        x1, y1 = landmarkList[12][1], landmarkList[12][2] 
        x2, y2 = landmarkList[8][1], landmarkList[8][2]
        x3, y3 = landmarkList[16][1], landmarkList[16][2]
        x4, y4 = landmarkList[20][1], landmarkList[20][2]

        lenght1 = math.hypot(x2 - x1, y2 - y1)
        lenght2 = math.hypot(x3 - x1, y3 - y1)
        lenght3 = math.hypot(x4 - x1, y3 - y1)

        if lenght1 > 100 and lenght2 > 100 and lenght3>100:
            #! Selenium action will happen here.
            cv2.circle(img, (x1, y1), 10, (0,0,255), cv2.FILLED)

def main():
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector(maxHands=2, detectionCon=0.7)

    while True:
        success, img = cap.read()
        detector.findHands(img) #TODO = change draw when necessary.

        landmarkList = detector.findPosition(img)
        fingerFlipDetection(img, landmarkList)

        #* Final image output
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()