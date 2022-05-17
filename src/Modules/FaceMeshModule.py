"""
!                        ----   Face Mesh Module  ----
"""
import cv2
import mediapipe as mp

#! Module for detecting 468 different points in the face 
class FaceMeshDetector():
    def __init__(self, staticMode=False, maxFaces=2, refine_landmarks=False ,minDetectionConf=0.5, minTrackConf=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.refine_landmarks = refine_landmarks
        self.minDetectionConf = minDetectionConf
        self.minTrackConf = minTrackConf    

        #* Face mesh 
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces, self.refine_landmarks, self.minDetectionConf, self.minTrackConf) # max face num for now
        self.drawSpec = self.mpDraw.DrawingSpec(color=(255,0,0),thickness=1, circle_radius=1) # drawing settings

    #! Face mesh finding
    def findFaceMesh(self, img, draw=False, drawIds=False):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLandmarks in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLandmarks, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec, self.drawSpec)
                
                face = []
                for id,landmark in enumerate(faceLandmarks.landmark): 
                    imageHeight, imageWidth, imageChannel = img.shape
                    x, y = int(landmark.x * imageWidth), int(landmark.y * imageHeight)
                    if drawIds:
                        cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN, 0.4, (255,0,0), 1) # id's of the dots are visible on the output now

                    face.append([id, x, y])
            
                faces.append(face)

        return img, faces
        

#! Main function
def main():
    width = 1180
    height = 720
    dim = (width,height)
    cap = cv2.VideoCapture("your video path")
    # cap = cv2.VideoCapture(0) # live cam
    pTime = 0
    detector = FaceMeshDetector()

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)

        if len(faces) != 0:
            print("Detected face count: {}".format(len(faces))) # detected face counts
            # print(faces[0]) # prints all the 468 landmark 
 
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow("Image", resized)
        # cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == "__main__":
    main()