"""
! Advanced Computer Vision FreeCodeCamp  
* Chapter 5: Gesture Volume Control Project

TODO--> Things that can be useful for iCare:
    * We can detect the distance changes between landmarks. 
    * This should be tested on face mesh module too.
"""
import cv2
import time 
import numpy as np
import HandTrackingModule as htm
import math 

#* PyCaw module for PC volume control
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPercentage = 0

#* Resolution settings
wCam, hCam = 640, 480

#* Video capture settings
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7) # calling the object with increased detection confidence(for more smooth footage)

while True:
    success, img = cap.read()
    detector.findHands(img)
    
    landmarkList = detector.findPosition(img, draw=False)
    if len(landmarkList) != 0:
        # print(landmarkList[4],landmarkList[8]) # getting only values of landmark no 2
        
        #* Coordinations of 2 landmarks we want to work with and the center of the distance
        x1, y1 = landmarkList[4][1], landmarkList[4][2] 
        x2, y2 = landmarkList[8][1], landmarkList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 +y2 ) // 2  #* cx and cy is the middle of the circle

        cv2.circle(img, (x1,y1), 15, (255,255,0), cv2.FILLED)
        cv2.circle(img, (x2,y2), 15, (255,255,0), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,255,0), 3)
        cv2.circle(img, (cx, cy), 10, (255,255,0), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        # Hand range 50 - 300
        # Volume range -65 - 0 (with the part below, we can redefine the ranges with numpy function)
        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 100])
        volPercentage = np.interp(length, [50, 300], [0, 100])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)

        # now we will create the condition to control the distance changes
        if length < 50: #TODO --> for 'good soup' project, we can go for under 15
            cv2.circle(img, (cx, cy), 10, (255,0,255), cv2.FILLED)

    #* Percentage and range output
    cv2.rectangle(img, (50,100), (85,400), (0,255,0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85,400), (0,255,0), cv2.FILLED)
    cv2.putText(img, f'{int(volPercentage)} %', (40,450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

    #* FPS calculation
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)

    #* Final image output
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break