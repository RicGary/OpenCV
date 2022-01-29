import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    largura = int(cap.get(3))
    altura = int(cap.get(4))

    # Criar linha
    #            Coordenadas iniciais || finais         B  G  R    Thic
    #linha = cv2.line(frame, (0, 0), (largura, altura), (0, 0, 255), 50)
    #linha2 = cv2.line(linha, (0, altura), (largura, 0), (0, 0, 255), 50)
    #retangulo = cv2.rectangle(linha2, (25, 25), (largura-25, altura-25), (0, 0, 255), 50)   # Se passar -1 vai preencher

    # Cículo -> centro e o raio
    ciruclo = cv2.circle(frame, (largura//2, altura//2), altura//3, (100, 200, 255), 50)

    # Fonte
    font = cv2.QT_FONT_NORMAL
    #                                     Bottom-left ||  escala da fonte  ||  faz o texto ficar melhor
    texto = cv2.putText(frame, 'Eric', (largura//2 - 60, 100), font, 2,(0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('Vid', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()