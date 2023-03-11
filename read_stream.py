import cv2
import numpy as np

import requests

ip = ""
url = "http://"+ip
cap = cv2.VideoCapture(url + ":81/stream")

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    L_limit = np.array([]) #insert RGB values for the desired color
    U_limit = np.array([])

    mask = cv2.inRange(hsv, L_limit, U_limit)
    dead_coral = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("original", frame)
    cv2.imshow("dead corals", dead_coral)
    cv2.waitkey(0)

cv2.destroyAllWindows()
cap.release()