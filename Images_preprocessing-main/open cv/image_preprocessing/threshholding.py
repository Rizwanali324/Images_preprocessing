import cv2
import numpy as np
import matplotlib.pyplot as plt



"""
Image thresholding is 
a simple yet effective 
technique in image processing and 
computer vision, used to create binary 
images from grayscale images. It involves
 comparing each pixel's intensity in the 
 grayscale image to a predefined threshold 
 value. Based on this comparison, the 
 pixels are assigned a new value 
 (usually black or white), effectively
   segmenting the 
image into foreground and background.

"""

"""
Types of Image Thresholding:
Simple Thresholding: In this method, a global threshold value is chosen manually. Pixels with intensity higher than the threshold are set to one value (often white), and others are set to another value (often black).

Adaptive Thresholding: Unlike simple thresholding, adaptive thresholding determines the threshold value dynamically for different regions of the image. This method is useful when lighting conditions vary across the image.

Otsu’s Thresholding: This is an automatic way of selecting the optimal threshold value from the image histogram. Otsu’s method assumes the image contains two classes of pixels (foreground and background) and then calculates the optimum threshold separating these two classes.
"""

# Read image in grayscale
image=cv2.imread('img/downlaod.jpg', cv2.IMREAD_GRAYSCALE)

# Simple Thresholding
ret, thresh_simple = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Adaptive Thresholding
thresh_adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                        cv2.THRESH_BINARY, 11, 2)

# Otsu's Thresholding
ret2, thresh_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display images using Matplotlib
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(thresh_simple, cmap='gray')
plt.title('Simple Thresholding')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(thresh_adaptive, cmap='gray')
plt.title('Adaptive Thresholding')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(thresh_otsu, cmap='gray')
plt.title("Otsu's Thresholding")
plt.axis('off')

plt.show()


# Apply different thresholding types
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
_, binary_inv = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
_, trunc = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
_, tozero = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
_, tozero_inv = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

# Display images
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [image, binary, binary_inv, trunc, tozero, tozero_inv]

plt.figure(figsize=(15, 5))
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


# Apply adaptive thresholding
adaptive_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                      cv2.THRESH_BINARY, 11, 2)
adaptive_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 11, 2)

# Display images
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 3, 2), plt.imshow(adaptive_mean, cmap='gray'), plt.title('Adaptive Mean Thresholding')
plt.subplot(1, 3, 3), plt.imshow(adaptive_gaussian, cmap='gray'), plt.title('Adaptive Gaussian Thresholding')
plt.show()