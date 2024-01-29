import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('img/downlaod.jpg')


#translation
img=cv2.resize(img,(500,500))


"""
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
 
r, c, _ = img.shape

m= cv2.getAffineTransform(pts1,pts2)


t_img=cv2.warpAffine(img,m,(c,r))

combine_img=np.hstack((img,t_img))
cv2.imshow('Translation', combine_img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""


rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))