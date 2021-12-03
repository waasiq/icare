"""
! Face Detection Module
"""
import cv2
import mediapipe as mp
import time

#! Module for detecting faces
class FaceDetector():
    def __init__(self, minDetectionConf=0.5):
        self.minDetectionConf = minDetectionConf

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionConf)

    #! Face finding
    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        bboxs = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                imgHeight, imgWidth, imgChannels = img.shape
                bbox = int(bboxC.xmin * imgWidth), int(bboxC.ymin * imgHeight), \
                    int(bboxC.width * imgWidth), int(bboxC.height * imgHeight)

                bboxs.append([id, bbox, detection.score])
                
                if draw:
                    img = self.fancyDraw(img, bbox)
                
                    cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0],bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 2)
        
        return img, bboxs

    #! Fancy drawing
    def fancyDraw(self, img, bbox, lenght=30, thickness=3, rectangleThickness=1):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h

        cv2.rectangle(img, bbox, color=(255,0,255), thickness=rectangleThickness)

        #* Top left (x,y)
        cv2.line(img, (x, y), (x+lenght, y), (255,0,255), thickness=thickness)
        cv2.line(img, (x, y), (x, y+lenght), (255,0,255), thickness=thickness)
        #* Top right (x1,y)
        cv2.line(img, (x1, y), (x1-lenght, y), (255,0,255), thickness=thickness)
        cv2.line(img, (x1, y), (x1, y+lenght), (255,0,255), thickness=thickness)
        #* Bottom left (x,y1)
        cv2.line(img, (x, y1), (x+lenght, y1), (255,0,255), thickness=thickness)
        cv2.line(img, (x, y1), (x, y1-lenght), (255,0,255), thickness=thickness)
        #* Bottom right (x1,y1)
        cv2.line(img, (x1, y1), (x1-lenght, y1), (255,0,255), thickness=thickness)
        cv2.line(img, (x1, y1), (x1, y1-lenght), (255,0,255), thickness=thickness)

        return img

            
#! Main function
def main():
    width = 1180
    height = 720
    dim = (width,height)
    #cap = cv2.VideoCapture("your video path")
    cap = cv2.VideoCapture(0) # live cam
    pTime = 0

    detector = FaceDetector() #* Calling the object

    while True:
        success, img = cap.read()

        img, bboxs = detector.findFaces(img) #* returning 2 values from findFaces()
        print(bboxs)

        #* FPS calculation
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 2)

        #* Resized image
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow("Image", resized)
    
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()