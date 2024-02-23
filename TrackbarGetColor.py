import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Tackbars")
cv2.createTrackbar("L-H","Tackbars",0,255,nothing)
cv2.createTrackbar("L-S","Tackbars",0,255,nothing)
cv2.createTrackbar("L-V","Tackbars",0,255,nothing)
cv2.createTrackbar("U-H","Tackbars",0,255,nothing)
cv2.createTrackbar("U-S","Tackbars",0,255,nothing)
cv2.createTrackbar("U-V","Tackbars",0,255,nothing)



while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("L-H","Tackbars")
    l_s = cv2.getTrackbarPos("L-S","Tackbars")
    l_v = cv2.getTrackbarPos("L-V","Tackbars")
    u_h = cv2.getTrackbarPos("U-H","Tackbars")
    u_s= cv2.getTrackbarPos("U-S","Tackbars")
    u_v = cv2.getTrackbarPos("U-V","Tackbars")

    lower_color = np.array([l_h,l_s,l_v])
    Upper_color = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv,lower_color,Upper_color)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key ==27:
        break
cap.release()
cv2.destroyAllWindows()