import cv2 
import numpy as np
import pandas as pd
img=cv2.imread('.ipynb_checkpoints/saveing.jpg')
#Learn to read and edit pixel values, working with image ROI and other basic operations.


"""Goal
Learn to:

Access pixel values and modify them
Access image properties
Set a Region of Interest (ROI)
Split and merge images
"""
print('image shape',img.shape)
print('image size',img.size)
print('image datatype',img.dtype)

#._______________accesing pixel /numpy acces array


blue=img[255,255,0]
print(blue)


#--------Image ROI


#=-------split&merge

r,g,b=i=cv2.split(img)
print('color is red',r)
print('color is green',g)
print('color is blue',b)


img=cv2.merge((r,g,b))