import numpy as np
import cv2

img = cv2.resize(cv2.imread('Imagens/Cookie Clicker.JPG', 0), (0,0), fx=0.8, fy=0.8)   # Cinza
template = cv2.resize(cv2.imread('Imagens/Cursor.JPG', 0), (0,0), fx=0.8, fy=0.8)   # Cinza

h, l = template.shape # Não tem o CHannel pois está em escala cinza

# TM -> Template Matching
metodos = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# Vamos testar vários métodos, o que funcionar melhor, é o que vamos usar
for metodo in metodos:
    img2 = img.copy()

    # Array com valores de quão perto o template está da imagem.
    resultado = cv2.matchTemplate(img2, template, metodo)   # (W - w + 1, H - h - 1) // Convolução de imagem
    # Valor retornado de quão próximo o template está da nossa img
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    # As vezes o mínimo é melhor e as vezes o máximo
    if metodo in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
        local = min_loc
    else:
        local = max_loc

    # Já que sabemos o tamanho da imagem, podemos saber onde está a coord. inferior
    inf_dir = (l + local[0], h + local[1])
    cv2.rectangle(img2, local, inf_dir, 255, 5)

    cv2.imshow('Comparação', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()