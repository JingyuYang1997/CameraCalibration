# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os


def circle_detected(filename):
    img = cv2.imread('correct/undistorted_'+filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite('circle_gray.jpg',gray)
    circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,
                                100, param1=100, param2=30, minRadius=50, maxRadius=75)
    circles = circles1[0, :, :]
    circles = np.uint16(np.around(circles))
    for i in circles[:]:
        cv2.circle(img, (i[0], i[1]), i[2], (255,0,0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (255, 0, 255), 2)
        cv2.rectangle(img, (i[0] - i[2], i[1] + i[2]), (i[0] + i[2], i[1] - i[2]), (255, 255, 0), 2)
        cv2.putText(img,'('+str(i[0])+','+str(i[1])+')',(i[0]+10,i[1]+10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.putText(img, 'radius=' + str(i[2]), (i[0] + 10, i[1] + 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    cv2.imwrite('correct/undistorted_'+filename,img)
