
"""



# Initialize variables
drawing = False
mode = None  # No initial drawing mode
ix, iy = -1, -1
points = []  # Points for polygon
temp_img = None  # Temporary image for intermediate drawing

# Define button areas
buttons = {'rectangle': (10, 10, 100, 40), 'circle': (120, 10, 100, 40),
           'ellipse': (230, 10, 100, 40), 'polygon': (340, 10, 100, 40),
           'freehand': (450, 10, 100, 40)}

# Mouse callback function
def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode, points, temp_img

    # Check if a button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        for key, value in buttons.items():
            x1, y1, x2, y2 = value
            if x1 <= x <= x1 + x2 and y1 <= y <= y1 + y2:
                mode = key
                points = []
                if mode != 'freehand':
                    temp_img = img.copy()
                return

        if mode:
            # Start drawing
            drawing = True
            ix, iy = x, y
            if mode == 'polygon' or mode == 'freehand':
                points.append((x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode == 'freehand':
                cv2.line(img, (ix, iy), (x, y), (0, 255, 0), 5)
                ix, iy = x, y
                points.append((x, y))
            else:
                temp_img = img.copy()
                draw_shape(temp_img, ix, iy, x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            drawing = False
            if mode != 'freehand':
                draw_shape(img, ix, iy, x, y)
            points = []
            temp_img = None



# Function to draw the selected shape
def draw_shape(img, x1, y1, x2, y2):
    if mode == 'rectangle':
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    elif mode == 'circle':
        radius = int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        cv2.circle(img, (x1, y1), radius, (0, 0, 255), 2)
    elif mode == 'ellipse':
        axis_length = (abs(x1 - x2), abs(y1 - y2))
        cv2.ellipse(img, (x1, y1), axis_length, 0, 0, 360, (255, 0, 0), 2)
    elif mode == 'polygon':
        if len(points) > 1:
            cv2.polylines(img, [np.array(points)], True, (0, 255, 255), 2)

# Function to draw buttons
def draw_buttons(img):
    for key, value in buttons.items():
        x1, y1, x2, y2 = value
        cv2.rectangle(img, (x1, y1), (x1+x2, y1+y2), (255, 255, 255), -1)
        cv2.putText(img, key, (x1+10, y1+30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
# Create a black image and a window
img = np.zeros((600, 600, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

while True:
    if temp_img is not None:
        display_img = temp_img
    else:
        display_img = img.copy()
    draw_buttons(display_img)
    cv2.imshow('image', display_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
"""


import numpy as np
import cv2

# Initialize variables
drawing = False
mode = None  # No initial drawing mode
ix, iy = -1, -1
points = []  # Points for polygon
temp_img = None  # Temporary image for intermediate drawing

# Define button areas
buttons = {'rectangle': (10, 10, 100, 40), 'circle': (120, 10, 100, 40),
           'ellipse': (230, 10, 100, 40), 'polygon': (340, 10, 100, 40),
           'freehand': (450, 10, 100, 40)}

# Function to check if two line segments intersect
def do_intersect(p1, q1, p2, q2):
    # Utility functions for the algorithm
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0: return 0
        return 1 if val > 0 else 2

    def on_segment(p, q, r):
        if (min(p[0], q[0]) <= r[0] <= max(p[0], q[0])) and (min(p[1], q[1]) <= r[1] <= max(p[1], q[1])):
            return True
        return False

    # Find orientations
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special cases
    if o1 == 0 and on_segment(p1, q1, p2): return True
    if o2 == 0 and on_segment(p1, q1, q2): return True
    if o3 == 0 and on_segment(p2, q2, p1): return True
    if o4 == 0 and on_segment(p2, q2, q1): return True

    return False

# Mouse callback function
def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode, points, temp_img

    # Check if a button is clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        for key, value in buttons.items():
            x1, y1, x2, y2 = value
            if x1 <= x <= x1 + x2 and y1 <= y <= y1 + y2:
                mode = key
                if mode != 'polygon':
                    points = []
                if mode != 'freehand':
                    temp_img = img.copy()
                return

        if mode:
            # Start drawing
            drawing = True
            ix, iy = x, y
            if mode == 'polygon':
                # Check if new point intersects with any existing line
                for i in range(1, len(points)):
                    if do_intersect(points[i - 1], points[i], points[-1], (x, y)):
                        # Close the polygon
                        cv2.polylines(img, [np.array(points + [(x, y)])], True, (0, 255, 255), 2)
                        points = []
                        drawing = False
                        mode = None
                        return
                points.append((x, y))
                temp_img = img.copy()
                cv2.polylines(temp_img, [np.array(points + [(x, y)])], False, (0, 255, 255), 2)
            elif mode == 'freehand':
                points.append((x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing and mode == 'freehand':
            cv2.line(img, (ix, iy), (x, y), (0, 255, 0), 5)
            ix, iy = x, y
            points.append((x, y))
        elif drawing and mode == 'polygon':
            temp_img = img.copy()
            cv2.polylines(temp_img, [np.array(points + [(x, y)])], False, (0, 255, 255), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing and mode != 'freehand' and mode != 'polygon':
            drawing = False
            draw_shape(img, ix, iy, x, y)
            points = []
            temp_img = None


# Function to draw the selected shape
def draw_shape(img, x1, y1, x2, y2):
    if mode == 'rectangle':
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    elif mode == 'circle':
        radius = int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        cv2.circle(img, (x1, y1), radius, (0, 0, 255), 2)
    elif mode == 'ellipse':
        axis_length = (abs(x1 - x2), abs(y1 - y2))
        cv2.ellipse(img, (x1, y1), axis_length, 0, 0, 360, (255, 0, 0), 2)
    elif mode == 'polygon':
        if len(points) > 1:
            cv2.polylines(img, [np.array(points)], True, (0, 255, 255), 2)

# Function to draw buttons
def draw_buttons(img):
    for key, value in buttons.items():
        x1, y1, x2, y2 = value
        cv2.rectangle(img, (x1, y1), (x1+x2, y1+y2), (255, 255, 255), -1)
        cv2.putText(img, key, (x1+10, y1+30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

# Create a black image and a window
img = np.zeros((600, 600, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)

while True:
    if temp_img is not None:
        display_img = temp_img
    else:
        display_img = img.copy()
    draw_buttons(display_img)
    cv2.imshow('image', display_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()