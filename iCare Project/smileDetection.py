"""
!                                               -----   Smile Detection Module  -----

TODO Ideas and Problems:
    * Organising the code.   --> DONE
    * Program can't detect until user reaches a certain distance to the camera. 
        -> Path 1:
            - Adding a rectangle in the output image. User must be within those rectangle limits. 
            - If user is not inside the rectangle, don't calculate.
        -> Path 2:
            - Detecting real-time distance using a depth/distance detection module or algorithm.
    * When a new face enters the frame or face exits the frame, program shuts down. Need to fix.
    * (mention other problems...)

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

#! Defining smiling landmarks and hypotenus calculation
def smilingPoints(img, faces):
    #* Face mesh landmarks to analyse
    left_idList1 = faces[0][216]
    left_idList2 = faces[0][184]
    right_idList1 = faces[0][436]
    right_idList2 = faces[0][408]

    left_topX, left_topY  = left_idList1[1], left_idList1[2]
    left_botX, left_botY  = left_idList2[1], left_idList2[2]
    right_topX, right_topY = right_idList1[1], right_idList1[2]
    right_botX, right_botY = right_idList2[1], right_idList2[2]

    #* Drawing landmarks on the facemesh in green
    cv2.circle(img, (left_idList1[1],  left_idList1[2]),  3, (0,255,0), 2,  cv2.FILLED)
    cv2.circle(img, (left_idList2[1],  left_idList2[2]),  3, (0,255,0), 2,  cv2.FILLED)
    cv2.circle(img, (right_idList1[1], right_idList1[2]), 3, (0,255,0), 2 , cv2.FILLED)
    cv2.circle(img, (right_idList2[1], right_idList2[2]), 3, (0,255,0), 2 , cv2.FILLED)

    #* Calculation of distance between landmarks
    leftHypotenuse = math.hypot(left_topX - left_botX, left_topY - left_botY)
    rightHypotenuse = math.hypot(right_topX - right_botX, right_topY - right_botY)

    return leftHypotenuse, rightHypotenuse


#! Detecting smile 
def smileDetection(img, leftHypotenuse, rightHypotenuse):
    #* Optimal top left and right bottom coordinates for rectangle 
    startPoint = (240, 100)
    endPoint = (410, 350)
    #? These points are debatable.
    cv2.rectangle(img, startPoint, endPoint, (255,255,0), 2)
    
    #TODO -> If user is not in that rectangle, don't detect.
    

    #* This if loop detects the smile. Change the hardcoded values w.r.t the Z axis.
    if ((leftHypotenuse < 18.5) and (rightHypotenuse < 18.5)):
        cv2.putText(img, "Smile :)", (200, 60), cv2.FONT_HERSHEY_PLAIN, 4, (255,0,0), 2)


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

        leftHypo, rightHypo = smilingPoints(img, faces)
        smileDetection(img, leftHypo, rightHypo)

        #* Final Image Output
        resizedImg = cv2.resize(img, DIMENTION, interpolation=cv2.INTER_AREA)
        cv2.imshow('Image', resizedImg)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()