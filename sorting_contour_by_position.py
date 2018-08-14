import cv2
import numpy as np
image = cv2.imread('shapes.jpg')
cv2.imshow('Input Image',image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,30,200)
cv2.imshow('canny Edges',edged)
cv2.waitKey(0)

boolean,contours,hirearchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('canny eges after contouring',edged)
cv2.waitKey(0)

original_image = image.copy()
print("no of contours="+str(len(contours)))

def x_cord_contour(contours):
    M=cv2.moments(contours)
    return (int(M['m10']/M['m00']))

def label_contour_center(image,c,i):
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.circle(image,(cx,cy),10,(0,0,255),-1)
    return image

for i,c in enumerate(contours):
    label_contour_center(image,c,i)

cv2.imshow("contours",image)
cv2.waitKey(0)

contour_left_to_right = sorted(contours,key = x_cord_contour,reverse = False)

for (i,c) in enumerate(contour_left_to_right):
    cv2.drawContours(original_image,[c],-1,(0,0,255),3)
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.putText(original_image,str(i+1),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('Left to right contour',original_image)
    cv2.waitKey(0)
    (x,y,w,h) = cv2.boundingRect(c)
    cropped_contour = original_image[y:y+h,x:x+w]
    cv2.imwrite('output_shape_number_'+str(i+1)+'.jpg',cropped_contour)
