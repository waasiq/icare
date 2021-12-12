"""
!                               -----   emotions.py ----- 

*-> Anger
*-> Sadness
*-> Happiness
*-> Shock
"""

import cv2
import mediapipe as mp

from Modules.FaceMeshModule import FaceMeshDetector 

from smileDetection import smilingPoints
from sadnessDetection import sadnessPoints
from angerDetection import angerPoints
from shockDetection import shockPoints
from winkDetection import winkPoints

#! Global Variable
#* Default Dimensions for Webcam: 1280 x 720 / Dimensions for Test Videos:  700 x 925
WIDTH = 1280
HEIGHT = 720
DIMENTION = (WIDTH, HEIGHT)

#! Detecting anger 
def detection(img, faces):
    #* Optimal top left and right bottom coordinates for rectangle 
    startPoint = (240, 100)
    endPoint = (440, 350)

    angerLeftHypotenus, angerRightHypotenus, points = angerPoints(img, faces)
    sadnessLeftHypotenus, sadnessRightHypotenus, points = sadnessPoints(img, faces)
    smileLeftHypotenus, smileRightHypotenus,points = smilingPoints(img, faces)
    shockLeftHypotenus, shockRightHypotenus,points = shockPoints(img, faces)
    winkLeftHypotenus, winkRightHypotenus, points = winkPoints(img, faces)

    cv2.rectangle(img, startPoint, endPoint, (255,255,0), 2)    

    #*-> 1. Anger
    #*-> 2. Sadness
    #*-> 3. Smile
    #*-> 4. Shock
    #*-> 5. Wink

    #* Face detection within box limits
    if(boxLimit(points)):
        if ((angerLeftHypotenus > 19.9) and (angerRightHypotenus > 19.9)):
            cv2.putText(img, "Anger >.<", (190, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
            return 1
        elif ((sadnessLeftHypotenus > 22.5) and (sadnessLeftHypotenus < 25)):            
            cv2.putText(img, "Sad :(", (200, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
            return 2
        elif ((smileLeftHypotenus < 17.5) and (smileRightHypotenus < 17.5)):
            cv2.putText(img, "Smile :)", (200, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
            return 3
        elif ((shockLeftHypotenus < 29)):
            cv2.putText(img, "Shocked O.O", (180, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
            return 4
        elif ((winkLeftHypotenus < 8) and (winkRightHypotenus < 8)):
            cv2.putText(img, "Wink ;)", (200, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)
            return 5
    else:
           cv2.putText(img, "Face not inside", (160, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)    


#! Checks if the face corner points are inside the box or not. 
#! Returns true and face accordingly
def boxLimit(points):
    left = points[0]
    right = points[2]

    if (left > 235 and right < 435):
        return True
    else: 
        return False

#! Main function
def main():
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = FaceMeshDetector()

    while True:
        success, img = cap.read() #* Video capture returns the success and img 
        img, faces = detector.findFaceMesh(img)
        detection(img, faces)

        #* Final Image Output
        resizedImg = cv2.resize(img, DIMENTION, interpolation=cv2.INTER_AREA)
        cv2.imshow('Image', resizedImg)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()