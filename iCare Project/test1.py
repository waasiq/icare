import cv2
import mediapipe as mp
import time
from Modules.FaceMeshModule import FaceMeshDetector 

#* Resolution settings
wCam, hCam = 640, 480

def main():
    #* Video capture settings
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime = 0

    detector = FaceMeshDetector()

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img, drawIds=True)

        #* Final image output
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == '__main__':
    main()