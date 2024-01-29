import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image and a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# Create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

while True:
    # Get current positions of trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')

    # Set image color
    img[:] = [b, g, r]

    # Display image
    cv2.imshow('image', img)

    # Break loop on ESC key
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ESC key
        break

cv2.destroyAllWindows()
