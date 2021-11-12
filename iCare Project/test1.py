import cv2
import mediapipe as mp
import time
import math
from Modules.FaceMeshModule import FaceMeshDetector 

#* Resolution settings
wCam, hCam = 640, 480

#! Default Dimensions for Webcame: 1280 x 720
#! Dimensions for Test Videos:  700 x 925
dim = (1280, 720)
#dim = (700,925)


def main():
    #* Video capture settings
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('videos/2.mp4')
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = FaceMeshDetector() # object call

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        
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

        leftHypotonus = math.hypot(left_topX - left_botX, left_topY - left_botY)
        rightHypotonus = math.hypot(right_topX - right_botX, right_topY - right_botY)

        #* This if loop detects the smile. Change the hardcoded values w.r.t the Z axis.
        if ((leftHypotonus < 18.5) and (rightHypotonus < 18.5)):
           cv2.putText(img, "Smile :)", (20, 70), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 3)


        #* Final image output
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow("resized", resized)
        # cv2.imshow('Image', img)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()