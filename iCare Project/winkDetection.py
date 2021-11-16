"""
!                                               -----   Wink Detection Module  -----

TODO Ideas and Problems:
    * 

"""

import cv2
import mediapipe as mp
import time
import math
from Modules.FaceMeshModule import FaceMeshDetector 

#! Global Variables
#* Default Dimensions for Webcam: 1280 x 720 / Dimensions for Test Videos:  700 x 925
WIDTH = 1280
HEIGHT = 720
DIMENTION = (WIDTH, HEIGHT)

#! Defining wink landmarks and hypotenus calculation
def winkPoints(img, faces):
    pass

#! Detecting winks
def winkDetection(img, leftHypotenus, rightHypotenus):
    pass

#! Main function
def main():
    pTime = 0
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture('videos/2.mp4')
    detector = FaceMeshDetector()

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)

        #* FPS Calculation and Output
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)

        leftHypo, rightHypo = winkPoints(img, faces)
        winkDetection(img, leftHypo, rightHypo)

        #* Final Image Output
        resizedImg = cv2.resize(img, DIMENTION, interpolation=cv2.INTER_AREA)
        cv2.imshow('Image', resizedImg)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()