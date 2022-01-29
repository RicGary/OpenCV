"""
Como capturar webcam
"""
import numpy as np
import cv2

cap = cv2.VideoCapture(0)   # Começa a usar

while True:
    ret, frame = cap.read() # ret -> se funciona para gravar

    # Para altura 4, largura 3 // vai de 0 até 17
    altura = int(cap.get(4))
    largura = int(cap.get(3))

    # Criar um array vazio para poder copiar a imagem // frame
    imagem = np.zeros(frame.shape, np.uint8)    # np.uint8 -> tipo de dado
    # Para caber no array de zeros, vamos reduzir o frame
    reduzido = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Topo Esquerdo
    imagem[:altura//2, :largura//2] = reduzido
    # Inferior Esquerdo
    imagem[altura//2:, :largura//2] = cv2.rotate(reduzido, cv2.cv2.ROTATE_180)
    # Topo Direito
    imagem[:altura//2, largura//2:] = reduzido
    # Inferior Direito
    imagem[altura//2:, largura//2:] = cv2.rotate(reduzido, cv2.cv2.ROTATE_180)

    cv2.imshow('frame', imagem)

    # A cada 1 ms verá se apertamos alguma tecla e converterá em
    # valor HEX, ex q = 113 || ou seja se apertarmos q ficará assim
    #       133       ==    133
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()   # Desativa
cv2.destroyAllWindows()