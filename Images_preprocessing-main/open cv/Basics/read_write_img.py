import cv2 as cv 
import numpy as np


#read images
img=cv.imread("img/downlaod.jpg",0)# zero is gray img
img=cv.resize(img,dsize=(500,500))


cv.imshow('Demo',img)  #show img

cv.waitKey(0)==ord('q') 
cv.destroyAllWindows()


#  cv.imwrite("saveing.jpg",img)________ #saving img
"""
cap=cv.VideoCapture(0)

if not cap.isOpened():
    print('camera is no open ')
    exit()
while True:
    #cap camera
    ret,frame=cap.read()


    if not ret: #if frame is read corret ret is ture
        print('can"t read a vidio')
        break
    # opration on frame 
 # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)# cap the image frame

    cv.imshow("Frame",gray)
    if cv.waitKey(1)  == ord('q'):
        break

cap.release()
cv.destroyAllWindows()"""