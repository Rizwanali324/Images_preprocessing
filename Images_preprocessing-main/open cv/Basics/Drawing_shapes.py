import numpy as np
import cv2 as cv



img=cv.imread('img/downlaod.jpg',1)

img=cv.resize(img,(500,500))
#lines 


l=cv.line(img,(84,84),(44,44),color=(255,0,0),thickness=5,lineType=cv.LINE_AA)

# rectangle
r=cv.rectangle(img,(150,150),(100,100),color=(0,255,0),thickness=9,lineType=cv.LINE_8)

# ciicle
c=cv.circle(img,(150,150),radius=90,color=(0,0,255),lineType=cv.LINE_4,thickness=9)

# elipse
cv.ellipse(img,center=(256,256),axes=(100,200),angle=20,startAngle=30,endAngle=90,color=(0,255,255),thickness=8)
    
    
cv.putText(img,text="ADDing color",org=(60,94),fontFace=4,fontScale=3.3,color=(255,0,0))
cv.imshow('frame',img)
cv.waitKey(0)==ord('q')
cv.destroyAllWindows()