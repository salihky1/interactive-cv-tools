import cv2
import numpy as np
import datetime

# -----------------------------------------
# Callback function for trackbars
# -----------------------------------------
def nothing(x):
    pass

# -----------------------------------------
# Create a black image
# -----------------------------------------
width = 600
height = 600
img = np.zeros((height, width, 3), np.uint8)

# -----------------------------------------
# Create window
# -----------------------------------------
window_name = "RGB Color Controller"
cv2.namedWindow(window_name)

# -----------------------------------------
# Create trackbars for RGB
# -----------------------------------------
cv2.createTrackbar("R", window_name, 0, 255, nothing)
cv2.createTrackbar("G", window_name, 0, 255, nothing)
cv2.createTrackbar("B", window_name, 0, 255, nothing)

# -----------------------------------------
# Create switch trackbar
# -----------------------------------------
switch = "0:OFF | 1:ON"
cv2.createTrackbar(switch, window_name, 0, 1, nothing)

# -----------------------------------------
# Font settings
# -----------------------------------------
font = cv2.FONT_HERSHEY_SIMPLEX

# -----------------------------------------
# Main loop
# -----------------------------------------
while True:
    # Show the image
    cv2.imshow(window_name, img)

    # Keyboard input
    key = cv2.waitKey(1) & 0xFF

    # Quit program
    if key == ord("q"):
        print("Program closed.")
        break

    # Reset colors
    if key == ord("r"):
        cv2.setTrackbarPos("R", window_name, 0)
        cv2.setTrackbarPos("G", window_name, 0)
        cv2.setTrackbarPos("B", window_name, 0)
        print("Colors reset.")

    # Save current color to file
    if key == ord("s"):
        r = cv2.getTrackbarPos("R", window_name)
        g = cv2.getTrackbarPos("G", window_name)
        b = cv2.getTrackbarPos("B", window_name)

        time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"saved_color_{time_stamp}.txt"

        with open(filename, "w") as f:
            f.write(f"Saved Color:\nR: {r}\nG: {g}\nB: {b}\n")

        print(f"Color saved to {filename}")

    # Get trackbar positions
    r = cv2.getTrackbarPos("R", window_name)
    g = cv2.getTrackbarPos("G", window_name)
    b = cv2.getTrackbarPos("B", window_name)
    s = cv2.getTrackbarPos(switch, window_name)

    # If switch is OFF
    if s == 0:
        img[:] = [0, 0, 0]
        status_text = "STATUS: OFF"
    else:
        img[:] = [b, g, r]
        status_text = "STATUS: ON"

    # -----------------------------------------
    # Draw UI text
    # -----------------------------------------
    cv2.rectangle(img, (0, 0), (width, 80), (50, 50, 50), -1)

    cv2.putText(img, "RGB Color Controller", (20, 30),
                font, 0.8, (255, 255, 255), 2)

    cv2.putText(img, status_text, (20, 60),
                font, 0.7, (0, 255, 0), 2)

    cv2.putText(img, f"R: {r}", (20, height - 80),
                font, 0.7, (0, 0, 255), 2)

    cv2.putText(img, f"G: {g}", (20, height - 50),
                font, 0.7, (0, 255, 0), 2)

    cv2.putText(img, f"B: {b}", (20, height - 20),
                font, 0.7, (255, 0, 0), 2)

    cv2.putText(img, "Controls:", (width - 250, height - 80),
                font, 0.6, (255, 255, 255), 1)

    cv2.putText(img, "Q - Quit", (width - 250, height - 60),
                font, 0.6, (255, 255, 255), 1)

    cv2.putText(img, "R - Reset", (width - 250, height - 40),
                font, 0.6, (255, 255, 255), 1)

    cv2.putText(img, "S - Save Color", (width - 250, height - 20),
                font, 0.6, (255, 255, 255), 1)

# -----------------------------------------
# Cleanup
# -----------------------------------------
cv2.destroyAllWindows()
