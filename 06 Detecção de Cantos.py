import numpy as np
import cv2

img = cv2.imread('Imagens/rubiks-cube.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Passar para Cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Cantos//Corners   Precisa encontrar com a imagem cinza
#                           imagem, qtd de cantos, qualidade do canto (0-1), distância mínima entre cantos
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

corners = np.int0(corners)  # Trasforma os valores do array em int

for corner in corners:
    # Poderia ser feito corner = corner[0], porém numpy tem uma forma melhor:
    x, y = corner.ravel()   # ravel achata um array -> [[[0, 1, 2]]] -> [0, 1, 2] \\ [[1,2], [2,1]] -> [1,2,2,1]
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1) # Lembrar que está em GrayScale

# Desenhar linhas
for i in range(len(corners)):
    for j in range(i+1 ,len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        # Gera Numpy Int que são diferentes de Python Int
        color = map(lambda x: int(x), np.random.randint(0, 255, size=3))
        cv2.line(img, corner1, corner2, tuple(color), 1)


"""
print(corners)  -> retorna float, mas queremos int
##############
[[[410.  98.]]
 [[471. 221.]]
 .
 .
 .
 [[ 94. 399.]]
 [[171. 152.]]]
"""

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()