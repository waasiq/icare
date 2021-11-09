"""
! Hand Tracking Module
"""
import cv2
import mediapipe as mp
import time

#! Module for detecting hands
class handDetector():
    def __init__(self, mode=False, maxHands=2, model_complexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_complexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    #! Hand finding
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks: # detecting each hand
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    #! Position finding and fancy drawing
    def findPosition(self, img, handNo=0, draw=True):
        landmarkList =[] 

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark): # enumerating dots
                h, w, c = img.shape # height, width, 
                cx ,cy = int(lm.x*w), int(lm.y*h) # center position 
    
                landmarkList.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx, cy), 10, (255,255,0), cv2.FILLED) 

        return landmarkList

#! Main function
def main():
    pTime = 0 # previous time 
    cTime = 0 # current time

    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()

        img = detector.findHands(img, draw=True) # if draw is false, won't draw anything 
        landmarkList = detector.findPosition(img, draw=True) # if draw is false, won't draw anything 
        if len(landmarkList) != 0:
            print(landmarkList[4]) # number that goes here is basically the coordination of the dot(like 0:Wrist, 4:Thumb_tip)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        



if __name__ == "__main__":
    main()

