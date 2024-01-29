import numpy as np
import cv2 as cv





cap=cv.VideoCapture(0)
"""
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
cv.destroyAllWindows()

"""

#saving cap

#src
src=cv.VideoWriter_fourcc(*'MJPG')
out=cv.VideoWriter('output.avi',src,10,(500,500)) #output
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        print('can"t recive frame ////')
        break
    frame=cv.flip(frame,0)
    out.write(frame)

    cv.imshow("frame",frame)
    if cv.waitKey(1)==ord('q'):
        break


#release if job is done
cap.release()
out.release()
cv.destroyAllWindows()