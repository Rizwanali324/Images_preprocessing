import cv2 
import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

"""Goal
In this tutorial, you will learn how to convert images from one color-space to another, like BGR ↔ Gray, BGR ↔ HSV, etc.
In addition to that, we will create an application to extract a colored object in a video
You will learn the following functions: cv.cvtColor(), cv.inRange(), etc.
"""


img = cv2.imread('img/downlaod.jpg')  # Ensure the path is correct
img = cv2.resize(img, (500, 500))

if img is None:
    print('Error: Image not found. Please check the path.')
else:
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert the grayscale image back to BGR format
    gray_img_bgr = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
    # Convert the image from BGR to HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Stack the original and the grayscale images horizontally
    combined_img = np.hstack((img, gray_img_bgr,hsv_img))

    # Display the combined image
    cv2.imshow('Original and Grayscale Image Side by Side', combined_img)

    # Wait for the 'q' key to be pressed to close the window
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()