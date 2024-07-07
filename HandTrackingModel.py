import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands = 2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw=True):
        # fps
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handno=0,draw= True ):

        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handno]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList





#fps
# imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# results = hands.process(imgRGB)
# #print(results.multi_hand_landmarks)
#
# if results.multi_hand_landmarks:
#     for handLms in results.multi_hand_landmarks:
#         for id, lm in enumerate(handLms.landmark):
#             # print(id, lm)
#             h, w, c = img.shape
#             cx, cy = int(lm.x*w), int(lm.y*h)
#             print(id, cx, cy)
#             # if id ==0:
#             cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
#             mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



def main():
    Ptime = 0
    Ctime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) !=0:
            print(lmList[4])
        Ctime = time.time()
        fps = 1 / (Ctime - Ptime)
        Ptime = Ctime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (65, 252, 3), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()