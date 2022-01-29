import cv2

img = cv2.imread('Imagens/Gary.jpg', -1)

print(type(img))    # Imagem -> Array do numpy

# Formato da imagem ou shape do array numpy
#   H ,  W , C  -> H=altura (Height)| W=largura(Width)| C=canal(Channel) -> RGB na verdade cv2 -> BGR
# (400, 400, 3)
print(img.shape)

"""
Imagem de 2 Pixels
[
[[0, 0, 0], [255, 255, 255]],
[[0, 0, 0], [255, 255, 255]]
]

 B  G  R -> Blue Green Red
[0, 0, 0]

0 -> 255 sendo 0 mínimo e 255 máximo


from random import randint

# Acessar os Pixel da Imagem

print(img[200][45:400])

for i in range(50):    # Linha
    for j in range(img.shape[1]):   # Coluna
        # linha, coluna, canal
        img[i][j] = [randint(0, 255), randint(0, 255), randint(0, 255)]

cv2.imshow('Img', img)
cv2.waitKey(0)
cv2.destroyWindow('Img')
"""

# Copiar parte da Imagem
# 150, 133 -> 250, 233

tag = img[150:250, 133: 233]

img[0: 100, 33:133] = tag
img[100: 200, 133:233] = tag


cv2.imshow('Img', img)
cv2.waitKey(0)
cv2.destroyWindow('Img')