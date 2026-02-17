import cv2
import numpy as np
import random

# ----------------------------------------
# Create canvas
# ----------------------------------------
width = 600
height = 600
canvas = np.zeros((height, width, 3), dtype=np.uint8)

window_name = "OpenCV Drawing Demo"
cv2.namedWindow(window_name)

# ----------------------------------------
# Default colors
# ----------------------------------------
line_color = (100, 200, 10)
rect_color = (0, 255, 100)
circle_color = (255, 0, 0)

# ----------------------------------------
# Shape positions
# ----------------------------------------
line_start = (350, 150)
line_end = (200, 300)

rect_start = (150, 150)
rect_end = (300, 300)

circle_center = (150, 150)
circle_radius = 60

# ----------------------------------------
# Font
# ----------------------------------------
font = cv2.FONT_HERSHEY_SIMPLEX

# ----------------------------------------
# Draw function
# ----------------------------------------
def draw_shapes(img):
    img[:] = 0  # Clear canvas

    # Draw line
    cv2.line(img, line_start, line_end, line_color, thickness=5)

    # Draw rectangle
    cv2.rectangle(img, rect_start, rect_end, rect_color, -1)

    # Draw circle
    cv2.circle(img, circle_center, circle_radius, circle_color, 4)

    # Draw info panel
    cv2.rectangle(img, (0, 0), (width, 80), (50, 50, 50), -1)

    cv2.putText(img, "OpenCV Shape Drawing Demo", (20, 30),
                font, 0.8, (255, 255, 255), 2)

    cv2.putText(img, "Controls:", (20, 60),
                font, 0.6, (255, 255, 255), 1)

    cv2.putText(img, "L - Change Line Color", (250, 60),
                font, 0.6, (255, 255, 255), 1)

    cv2.putText(img, "R - Change Rectangle Color", (20, height - 60),
                font, 0.6, (255, 255, 255), 1)

    cv2.putText(img, "C - Change Circle Color", (20, height - 40),
                font, 0.6, (255, 255, 255), 1)

    cv2.putText(img, "X - Clear Canvas", (20, height - 20),
                font, 0.6, (255, 255, 255), 1)

# ----------------------------------------
# Main loop
# ----------------------------------------
while True:
    draw_shapes(canvas)
    cv2.imshow(window_name, canvas)

    key = cv2.waitKey(1) & 0xFF

    # Quit
    if key == ord("q"):
        print("Program terminated.")
        break

    # Change line color
    if key == ord("l"):
        line_color = (random.randint(0,255),
                      random.randint(0,255),
                      random.randint(0,255))
        print("Line color changed:", line_color)

    # Change rectangle color
    if key == ord("r"):
        rect_color = (random.randint(0,255),
                      random.randint(0,255),
                      random.randint(0,255))
        print("Rectangle color changed:", rect_color)

    # Change circle color
    if key == ord("c"):
        circle_color = (random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255))
        print("Circle color changed:", circle_color)

    # Clear canvas
    if key == ord("x"):
        canvas[:] = 0
        print("Canvas cleared.")

    # Move line with arrows
    if key == 82:  # Up
        line_start = (line_start[0], line_start[1] - 5)
        line_end = (line_end[0], line_end[1] - 5)

    if key == 84:  # Down
        line_start = (line_start[0], line_start[1] + 5)
        line_end = (line_end[0], line_end[1] + 5)

    if key == 81:  # Left
        line_start = (line_start[0] - 5, line_start[1])
        line_end = (line_end[0] - 5, line_end[1])

    if key == 83:  # Right
        line_start = (line_start[0] + 5, line_start[1])
        line_end = (line_end[0] + 5, line_end[1])

# ----------------------------------------
# Cleanup
# ----------------------------------------
cv2.destroyAllWindows()
