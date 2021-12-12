"""
!                                               -----   "Good Soup" Easter Egg  -----

TODO Ideas and Problems:
    * (mention other problems...)
"""

import cv2
import mediapipe as mp
import time
import math
from Modules.HandTrackingModule import handDetector
from selenium import webdriver
from seleniumModule import good_soup

#! Global Variables
#* Default Dimensions for Webcam: 1280 x 720 / Dimensions for Test Videos:  700 x 925
WIDTH = 1280
HEIGHT = 720
DIMENTION = (WIDTH, HEIGHT)

#! Detecting "Good Soup"
def goodSoupDetection(img, landmarkList):
    if len(landmarkList) != 0:
        # print(landmarkList[4],landmarkList[8]) # getting only values of landmark no 2
        
        #* Coordinations of 2 landmarks we want to work with and the center of the distance
        x1, y1 = landmarkList[4][1], landmarkList[4][2] 
        x2, y2 = landmarkList[8][1], landmarkList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2 

        #TODO-> shut after use.
        # cv2.circle(img, (x1,y1), 15, (255,255,0), cv2.FILLED)
        # cv2.circle(img, (x2,y2), 15, (255,255,0), cv2.FILLED)
        # cv2.line(img, (x1,y1), (x2,y2), (255,255,0), 3)
        # cv2.circle(img, (cx, cy), 10, (255,255,0), cv2.FILLED)

        lenght = math.hypot(x2 - x1, y2 - y1)

        if lenght < 15:
            #! Selenium action will happen here.
            cv2.circle(img, (cx, cy), 10, (0,0,255), cv2.FILLED)
            driver = webdriver.Chrome()
            driver.maximize_window()
            good_soup(driver=driver)
    

def main():
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector(maxHands=2, detectionCon=0.7)

    while True:
        success, img = cap.read()
        detector.findHands(img, draw=False) #TODO = change draw when necessary.

        landmarkList = detector.findPosition(img, draw=False)
        goodSoupDetection(img, landmarkList)

        #* Final image output
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()