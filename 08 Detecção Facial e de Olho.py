import numpy as np
import cv2

# Utiliza algo chamado HAAR CASCADE, caso queira pesquisar

cap  = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Transformar em cinza
    faces = face_cascade.detectMultiScale(gray, 1.05, 5) # Retorna as coord de onde estão os rostos
    """
    Como funciona esse detectMultiScale??
    
    detectMultiScale(cor, scaleFactor, minNeighbors)
    scaleFactor -> reduz a imagem para que o computador consiga compreender melhor
        1 -> não muda nada
        1.05 -> muda 5%
        Quanto menor, mais acurácia porém mais lento.
        Quanto maior, menos acurácia porém mais rápido.
        
    minNeighbors -> Acurácia do algorítmo para quantos rostos na imagem.
        3~6 -> bons valores
        Quanto menor, mais acurácia porém mais lento.
        Quanto maior, menos acurácia porém mais rápido.
        
    minSize -> Tamanho mínimo do retângulo no rosto, rostos menores que isto serão ignorados.
    
    maxSize -> Tamanho máximo do retângulo no rosto, rostos maiores que isto serão ignorados.
    
    """
    for x, y, w, h in faces:
        # Coloca um retangulo no rosto
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

        """
        # Já que os olhos estão no rosto, não precisamos procurar na imagem inteira
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w] # Modificar aqui, modificará o frame original
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.05, 5)
        for ex, ey, ew, eh in eyes:
            # Passamos roi_color e não frame pois ele se refere a outras coordenadas
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 3)
            """

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()