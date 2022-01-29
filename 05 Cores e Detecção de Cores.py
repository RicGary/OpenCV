import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Atualmente está em BGR, vamos mudar para HSV
    largura = cap.get(3) // 1
    altura = cap.get(4) // 1

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Mudando frame para HSV
    lower_pink = np.array([165-10, 100, 100])   # Colocar Lower [H-10, 100, 100]
    upper_pink = np.array([180, 255, 255])      # Colocar Upper [H+10, 255, 255]

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Máscara para dizer quais pixels devemos manter.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Como se unisse duas imagens e utiliza a máscara
    result = cv2.bitwise_and(frame, frame, mask=mask)

    """
    11 = 1
    01 = 0
    10 = 0
    00 = 0
    """

    cv2.imshow('vid', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
