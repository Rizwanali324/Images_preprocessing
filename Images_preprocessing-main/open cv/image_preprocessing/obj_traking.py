import cv2
import numpy as np


"""
Object Tracking
Now that we know how to convert a BGR image to HSV, we can use this to extract a colored object. In HSV, it is easier to represent a color than in BGR color-space. In our application, we will try to extract a blue colored object. So here is the method:

Take each frame of the video
Convert from BGR to HSV color-space
We threshold the HSV image for a range of blue color
Now extract the blue object alone, we can do whatever we want on that image.

"""
    # define range of blue color in HSV
lower_blue = np.array([50,50,50])
upper_blue = np.array([120,255,255])
cap=cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv2.resize(frame,(250,250))
        
    #convert BGR to HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #threshhold
    mask=cv2.inRange(hsv,lowerb=lower_blue,upperb=upper_blue)

    #bitwise and mask and original image
    blue_obj=cv2.bitwise_and(frame,frame,mask=mask)
    mask_res=cv2.resize(mask,(250,250))
    blue_obj_res=cv2.resize(blue_obj,(250,250))
    
    # Convert mask to BGR format for concatenation
    mask_res_bgr = cv2.cvtColor(mask_res, cv2.COLOR_GRAY2BGR)
    combined_img=np.hstack((frame,mask_res_bgr,blue_obj_res))
    
    cv2.imshow("OBJ Traking",combined_img)

    # break the loop if q is presed

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()