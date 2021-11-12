import cv2
import mediapipe as mp
import time
from Modules.FaceMeshModule import FaceMeshDetector 

#* Resolution settings
wCam, hCam = 640, 480
dim = (620, 900)

def main():
    #* Video capture settings
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture('videos/2.mp4')
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = FaceMeshDetector() # object call

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        
        idList1 = faces[0][216]
        idList2 = faces[0][96]
        # print("id: {} x: {} y: {}".format(idList1[0], idList1[1], idList1[2]))
        cv2.circle(img, (idList1[1], idList1[2]), 3, (0,255,0), 2, cv2.FILLED)
        cv2.circle(img, (idList2[1], idList2[2]), 3, (0,255,0), 2, cv2.FILLED)

        #TODO --> get coordinates from the id




        #* Final image output
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow("resized", resized)
        # cv2.imshow('Image', img)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break



if __name__ == '__main__':
    main()