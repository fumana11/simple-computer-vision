import cv2
cap=cv2.VideoCapture(0)

while (1):
    isTrue, frame=cap.read()
    cv2.imshow('frame',frame)
    k= cv2.waitKey(5) & 0xFF
    if k ==27:
        break

cap.release()
cv2.destroyAllWindows
