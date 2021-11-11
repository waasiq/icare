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

    detector = FaceMeshDetector() # object call

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        
        idList = faces[0][1]
        print("id: {} x: {} y: {}".format(idList[0], idList[1], idList[2]))
        cv2.circle(img, (idList[1], idList[2]), 3, (255,255,0), 2, cv2.FILLED)

        #TODO --> get coordinates from the id




        #* Final image output
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == '__main__':
    main()