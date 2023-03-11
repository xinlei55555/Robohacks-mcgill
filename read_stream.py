import cv2
import matplotlib.pyplot as plt

import numpy as np

import requests

ip = "192.168.96.125"
url = "http://"+ip
cap = cv2.VideoCapture(url + ":81/stream")
print("request done")

while True:
    _, frame = cap.read()
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # L_limit = np.array([]) #insert RGB values for the desired color
    # U_limit = np.array([])
    #
    # mask = cv2.inRange(hsv, L_limit, U_limit)
    # dead_coral = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("original", frame)
    # plt.imshow(frame)
    # cv2.imshow("dead corals", dead_coral)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()