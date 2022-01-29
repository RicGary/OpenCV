import numpy as np
import cv2

BGR_LOW = np.uint8([[[178, 129, 255]]])
BGR_UP = np.uint8([[[130, 81, 236]]])

x_low = cv2.cvtColor(BGR_LOW, cv2.COLOR_BGR2HSV)
x_up = cv2.cvtColor(BGR_UP, cv2.COLOR_BGR2HSV)

print(x_low, x_up)

