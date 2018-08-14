import cv2
import numpy as np
image = cv2.imread('shapes.jpg')
cv2.imshow('Input Image',image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,30,200)
cv2.imshow('canny Edges',edged)
cv2.waitKey(0)

boolean,contours,hirearchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('canny eges after contouring',edged)
cv2.waitKey(0)

print("no of contours="+str(len(contours)))


def area(contours):
    allarea = []
    for cnt in contours:
        allarea.append(cv2.contourArea(cnt))
    return allarea

print(area(contours))

sortedcontour = sorted(contours,key = cv2.contourArea,reverse = True)

for cvt in sortedcontour:
    cv2.drawContours(image,[cvt],-1,(0,255,0),2)
    cv2.imshow("contours",image)
    cv2.waitKey(0)
