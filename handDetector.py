import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=2, detectionCon=0.5, minTrackCon=0.5)

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img, draw=True, flipType=True)

    if hands:
        hand1 = hands[0]
        fingers1 = detector.fingersUp(hand1)
        print(fingers1)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
