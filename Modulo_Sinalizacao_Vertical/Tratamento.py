#-*- coding utf-8 -*-

# ------------------ Projeto Atena -----------------------

# 	Autores: Estanislau Filho e José Antônio
# 	Ano: 2019
# 	Orientadora: Natália Batista
#	Instituição: CEFET-MG	
# 	Link github: https://github.com/EstanislauFilho/Atena

#	Script: Tratamento

# --------------------------------------------------------

import cv2
import time
import numpy as np
import Pista as pista
import Motores as motor
import Variaveis as var
import Sensores as sensor
import Gerenciador as gerencia
import Sinalizacoes as sinalizacao


# ############################## FUNCAO DE DETECCAO DAS FAIXAS ###################################
def deteccao_faixas_visao(img):

	# ------------- Variaveis que irao definir o status de deteccao das faixas -------------------
	status_visao_faixa_dir, status_visao_faixa_esq, status_faixa_contencao_visao = False, False, False

	# --------------------------------------------------------------------------------------------


	# --------------- Manipulacao da imagem original para deteccao das faixas --------------------
	img_perspectiva_pista = pista.perspectiva_pista(img)
	img_filtros = pista.filtros_faixas(img_perspectiva_pista) 

	img_faixa_esq = img_filtros[var.y1_faixa_esq:var.y2_faixa_esq, var.x1_faixa_esq:var.x2_faixa_esq]
	img_faixa_esq, cx_esq = pista.detecta_faixas(img_faixa_esq)

	img_faixa_dir = img_filtros[var.y1_faixa_dir:var.y2_faixa_dir, var.x1_faixa_dir:var.x2_faixa_dir]
	img_faixa_dir, cx_dir = pista.detecta_faixas(img_faixa_dir)

	
	# --------------------------------------------------------------------------------------------

	

	# --------------------------- Detecção das faixas com Visao ----------------------------------
	if cx_dir >= 60 and cx_esq <= 73:
		status_visao_faixa_dir = True

	if cx_dir >= 50 and cx_esq <= 55:
		status_visao_faixa_esq = True

	if ((cx_dir >= 80 and cx_esq <= 30)):
		status_contencao_visao = True
	# --------------------------------------------------------------------------------------------
	
	#print("Faixa Dir: {0}: \tFaixa Esq: {1} \tFaixa de Contenção: {2}".format(cx_dir, cx_esq, status_contencao_visao))
	#print("Faixa Esq: {0} {1} \tFaixa Dir: {2} {3}".format(status_visao_faixa_esq, cx_esq, status_visao_faixa_dir, cx_dir))

	retorno = [
				img_perspectiva_pista, 
				img_faixa_esq, 
				img_faixa_dir, 
				status_visao_faixa_dir, 
				status_visao_faixa_esq, 
				status_faixa_contencao_visao
              ]

	return retorno
# ###############################################################################################



def deteccao_faixas_fototransistores(a0, a1, a2, a3, b0, b1, b2, b3):

	# ------------- Variaveis que irao definir o status de deteccao das faixas -------------------
	status_a0, status_a1, status_a2, status_a3 = False, False, False, False 
	status_b0, status_b1, status_b2, status_b3 = False, False, False, False 
	# --------------------------------------------------------------------------------------------


	# -------------- Verificação da deteccao das faixas com os fototransistores ------------------
	if (a0 <= var.CONST_A0):
		status_a0 = True
	if (a1 <= var.CONST_A1):
		status_a1 = True
	if (a2 <= var.CONST_A2):
		status_a2 = True
	if (a3 <= var.CONST_A3):
		status_a3 = True

	if (b0 <= var.CONST_B0):
		status_b0 = True
	if (b1 <= var.CONST_B1):
		status_b1 = True
	if (b2 <= var.CONST_B2):
		status_b2 = True
	if (b3 <= var.CONST_B3):
		status_b3 = True
	# --------------------------------------------------------------------------------------------

	retorno = [ 
				status_a0, 
				status_a1, 
				status_a2, 
				status_a3,
				status_b0, 
				status_b1, 
				status_b2,
				status_b2
              ]

	return retorno
# ###############################################################################################



# ###################### FUNCAO DE TRATAMENTO DA SINALIZACOES A DIREITA #########################
def sinalizacao_direita(img):
	(	
		status_plc_pare, 
		status_plc_pedestre, 
		status_plc_desvio, 
		plc_pare,
		plc_pedestre,
		plc_desvio
	) = False, False, False, False, False, False

	plc_pare, distancia_placa = sinalizacao.detecta_placas_direita(img, var.nome_p1, var.classificador_p1)
	#plc_pedestre, distancia_placa = sinalizacao.detecta_placas_direita(img, var.nome_p2, var.classificador_p2)
	#plc_desvio, distancia_placa = sinalizacao.detecta_placas_direita(img, var.nome_p3, var.classificador_p3)
	
	if((plc_pare is True) and (distancia_placa > 2 and distancia_placa <= 20)):
		status_plc_pare = True

	if((plc_pedestre is True) and (distancia_placa > 9 and distancia_placa <= 19)):
		status_plc_pedestre = True
		
	if(plc_desvio is True) and (distancia_placa <= 17):
		status_plc_desvio = True
	
	retorno = [
				status_plc_pare, 
				status_plc_pedestre, 
				status_plc_desvio 	
			  ]
	
	return retorno
# ###############################################################################################





