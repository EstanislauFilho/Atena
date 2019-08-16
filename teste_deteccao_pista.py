#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Classe: Teste de Detecção da Pista

# --------------------------------------------------------

# Processos:
# 1º Conversão da imagem para escala de cinza
# 2º Aplicação do Gaussiano Blur

import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread("Imagens/imagem_teste.jpg")

copia_imagem = np.copy(imagem)

imagem_cinza = cv2.cvtColor(copia_imagem, cv2.COLOR_RGB2GRAY)

imagem_blur = cv2.GaussianBlur(imagem_cinza, (5,5), 0) # Distorce a imagem

imagem_canny = cv2.Canny(imagem_blur, 50, 150) # A função distingue todas as cores em preto e branco

cv2.imshow("",imagem)
cv2.waitKey(0)
cv2.imshow("",imagem_cinza)
cv2.waitKey(0)
cv2.imshow("",imagem_blur)
cv2.waitKey(0)
cv2.imshow("",imagem_canny)
cv2.waitKey(0)

