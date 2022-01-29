"""
Série de Tutoriais de OpenCV
- Serve para vários tópicos de imagem.

Para instalar no PyCharm:

1 - Tecle Ctrl + Alt + S
2 - Project: -> Python Interpreter -> Clica no + no canto sup. dir. e pesquisa por OpenCV-Python
"""
import cv2

# Carregar Imagem
#                  Local           | Modo de carregar a imagem
img = cv2.imread('Imagens/Gary.jpg', 0)

# Altera o tamanho da imagem determinada
# img = cv2.resize(img, (300, 300)) -> Forma de conseguir um tamanho fixo

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # Muda a escala em 1/2, ou seja metade do tamanho original
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)  # Para mais opções, olhar documentação

cv2.imwrite('Imagens/nova_imagem.jpg', img)  # Salva a imagem feita

# Alguns modos são:
# IMREAD_COLOR : Carrega uma imagem colorida. Transparências são perdidas. -> -1
# IMREAD_GREYSCALE : Carrega uma imagem com escala cinza. -> 0
# IMREAD_UNCHANGED : Carrega a imagem com o canal alfa (se tem transparência, ela permanece). -> 1

# Mostra a imagem
#      Nome da tela|Nome arq
cv2.imshow('Imagem', img)
cv2.waitKey(0)  # -> Espera um tempo infinito até apertar um botão. Colocando valores ex: 5 significa que fecha em 5s.
cv2.destroyWindow('Imagem')  # -> Fecha a tela
