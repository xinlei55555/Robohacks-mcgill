import cv2

import numpy as np

import requests

ip = "192.168.96.125"
url = "http://"+ip
cap = cv2.VideoCapture(url + ":81/stream")
print("request done")

all_frames = []
all_masks = []
for i in range(100):
    _, frame = cap.read()
    all_frames.append(frame)
    orig = np.copy(frame)
    red = np.zeros_like(frame)
    red[:, :] = [6, 0, 6]
    img = cv2.add(frame, red)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    L_limit = np.array([0, 0, 0], dtype = "uint8") #insert RGB values for the desired color
    U_limit = np.array([0,0,255], dtype = "uint8")
    #
    mask = cv2.inRange(hsv, L_limit, U_limit)
    print("mask", mask)
    dead_coral = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("original", orig)
    cv2.imshow("color filter", img)
    # plt.imshow(frame)
    cv2.imshow("dead corals", dead_coral)
    # print(frame)
    # print(dead_coral)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
print("difference", all_frames[-1]-all_frames[0])