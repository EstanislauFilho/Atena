#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Sinalizacoes

# --------------------------------------------------------
import cv2
import numpy as np
import Variaveis as var

def detecta_placas_direita(img, nome, classificador):
	distancia_placa = " - "
	status_placa =  False

	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			
	img_detecta_placa = classificador.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=10)
	
	for (x,y,w,h) in img_detecta_placa:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		distancia_placa = calculo_distancia_placa(x, w)
		cv2.putText(img, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
		cv2.putText(img, str(distancia_placa)+" cm", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
		status_placa = True

	return status_placa, distancia_placa



def calculo_distancia_placa(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)


