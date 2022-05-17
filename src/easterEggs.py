from fingerFlipEasterEgg import *
from goodSoupEasterEgg import * 

def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector(maxHands=2, detectionCon=0.7)

    while True:
        success, img = cap.read()
        detector.findHands(img, draw=False) #TODO = change draw when necessary.

        landmarkList = detector.findPosition(img)
        #fingerFlipDetection(img, landmarkList)
        goodSoupDetection(img, landmarkList)

        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()