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
import Variaveis_HSV as var_hsv



def hsv_museu(img, dados_museu):
	status_museu = False
	
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			
	min_H, max_H, min_S, max_S, min_V, max_V = dados_museu
	
	hsv_min = np.array([min_H, min_S, min_V])
	hsv_max = np.array([max_H, max_S, max_V])

	mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

	img_resultado = cv2.bitwise_and(img, img, mask=mascara)

	_, contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	'''
	for c in contours:
		if ((cv2.contourArea(c) > var_hsv.CHECK_TESTE)):
			print(cv2.contourArea(c))	
	'''
	
	for c in contours:
		if (((cv2.contourArea(c) > var_hsv.CONST_DETECCAO_MUSEU - 300)) and (cv2.contourArea(c) <= (var_hsv.CONST_DETECCAO_MUSEU + 300))):			
			x,y,w,h = cv2.boundingRect(c)
			distancia_placa = calculo_distancia_placa(x, w)
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 3)
			cv2.putText(img, var_hsv.nome_check_1, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			if(distancia_placa <= var.CONST_DISTANCIA_PLACA):
				status_museu = True
	
			
	return  status_museu





def hsv_igreja(img, dados_igreja):
	status_igreja = False
	
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			
	min_H, max_H, min_S, max_S, min_V, max_V = dados_igreja
	
	hsv_min = np.array([min_H, min_S, min_V])
	hsv_max = np.array([max_H, max_S, max_V])

	mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

	img_resultado = cv2.bitwise_and(img, img, mask=mascara)

	_, contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	'''
	for c in contours:
		if ((cv2.contourArea(c) > var_hsv.CHECK_TESTE)):
			print(cv2.contourArea(c))	
	'''
	
	for c in contours:
		if (((cv2.contourArea(c) > var_hsv.CONST_DETECCAO_IGREJA - 300)) and (cv2.contourArea(c) <= (var_hsv.CONST_DETECCAO_IGREJA + 300))):			
			x,y,w,h = cv2.boundingRect(c)
			distancia_placa = calculo_distancia_placa(x, w)
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 3)
			cv2.putText(img, var_hsv.nome_check_2, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			if(distancia_placa <= var.CONST_DISTANCIA_PLACA):
				status_igreja = True
		
	return  status_igreja




def hsv_teatro(img, dados_teatro):
	status_teatro = False
	
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			
	min_H, max_H, min_S, max_S, min_V, max_V = dados_teatro
	
	hsv_min = np.array([min_H, min_S, min_V])
	hsv_max = np.array([max_H, max_S, max_V])

	mascara = cv2.inRange(img_hsv, hsv_min, hsv_max)

	img_resultado = cv2.bitwise_and(img, img, mask=mascara)

	_, contours, _ = cv2.findContours(mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	'''
	for c in contours:
		if ((cv2.contourArea(c) > var_hsv.CHECK_TESTE)):
			print(cv2.contourArea(c))	
	
	'''
	for c in contours:
		if (((cv2.contourArea(c) > var_hsv.CONST_DETECCAO_TEATRO - 300)) and (cv2.contourArea(c) <= (var_hsv.CONST_DETECCAO_TEATRO + 300))):		
			x,y,w,h = cv2.boundingRect(c)
			distancia_placa = calculo_distancia_placa(x, w)	
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), 3)
			cv2.putText(img, var_hsv.nome_check_2, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)	
			if(distancia_placa <= var.CONST_DISTANCIA_PLACA):
				status_teatro = True
	
	return  status_teatro




def detecta_plc_igreja(img, classificador):
	distancia_plc_igreja = " - ", " - "
	status_plc_igreja = False

	img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)		

	img_detecta_igreja = classificador.detectMultiScale(img_gray, 1.1, 3)

	for (x,y,w,h) in img_detecta_igreja:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		distancia_plc_igreja = calculo_distancia_placa(x, w)
		if(distancia_plc_igreja <= 32):
			status_plc_igreja = True	

	for (x,y,w,h) in img_detecta_igreja:
		cv2.putText(img, var.nome_plc_igreja, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
		cv2.putText(img, str(distancia_plc_igreja)+" cm", (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
			

	return status_plc_igreja





def calculo_distancia_placa(x, w):
	return int((-0.26316) * ((x + w)-x) + 45.78947)


