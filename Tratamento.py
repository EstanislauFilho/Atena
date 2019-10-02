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
import Interface as interface
import Obstaculos as obstaculo
import Gerenciador as gerencia
import Sinalizacoes as sinalizacao

# ########################### FUNCAO DE TRATAMENTO DA INTERFACE MENU ###############################
def interface_menu(op):
	inicializacao, destino_igreja, destino_teatro, destino_museu = False, False, False, False

	if(op == 1):
		nome = "Museu"
	elif(op == 2):
		nome = "Igreja"
	elif(op == 3):
		nome = "Teatro" 
	else:
		print("Error")
	
	confir = interface.confirma_opcao(op, nome)

	if(op == 1) and (confir == 1):
		destino_museu = True
		inicializacao = True
	elif(op == 2) and (confir == 1):
		destino_igreja = True
		inicializacao = True
	elif(op == 3) and (confir == 1):
		destino_teatro = True
		inicializacao = True
	
	return inicializacao, destino_museu, destino_igreja, destino_teatro, 
# ###############################################################################################



# ############################## FUNCAO DE DETECCAO DAS FAIXAS ###################################
def deteccao_faixas_visao(img):

	# ------------- Variaveis que irao definir o status de deteccao das faixas -------------------
	status_visao_faixa_dir, status_visao_faixa_esq = False, False

	status_anormalidade_faixa_dir, status_anormalidade_faixa_esq = False, False
	# --------------------------------------------------------------------------------------------


	# --------------- Manipulacao da imagem original para deteccao das faixas --------------------
	img_perspectiva_pista = pista.perspectiva_pista(img)
	img_filtros = pista.filtros_faixas(img_perspectiva_pista) 

	img_faixa_esq = img_filtros[var.y1_faixa_esq:var.y2_faixa_esq, var.x1_faixa_esq:var.x2_faixa_esq]
	img_faixa_esq, cx_esq = pista.detecta_faixas(img_faixa_esq)

	img_faixa_dir = img_filtros[var.y1_faixa_dir:var.y2_faixa_dir, var.x1_faixa_dir:var.x2_faixa_dir]
	img_faixa_dir, cx_dir = pista.detecta_faixas(img_faixa_dir)

	soma_matriz_img_esq = gerencia.analise_matriz_imagem(img_faixa_esq)
	soma_matriz_img_dir = gerencia.analise_matriz_imagem(img_faixa_dir)
	#print(soma_matriz_img_esq, soma_matriz_img_dir)
	# --------------------------------------------------------------------------------------------

	'''
	# ------------- Verificação do status de normalidade na detecção das faixas ------------------
	if((cx_dir <= 25) and (cx_dir >= 55)):
		status_anormalidade_faixa_dir = True

	if((cx_esq <= 63) and (cx_esq >= 93)):
		status_anormalidade_faixa_esq = True

	if(status_anormalidade_faixa_dir is False):
		status_dir = "Normal"
	else:
		status_dir = "ANORMAL"

	if(status_anormalidade_faixa_esq is False):
		status_esq = "Normal"
	else:
		status_esq = "ANORMAL"
	# --------------------------------------------------------------------------------------------
	'''

	# --------------------------- Detecção das faixas com Visao ----------------------------------
	if cx_dir >= 74:
		status_visao_faixa_dir = True

	if cx_esq <= 45:
		status_visao_faixa_esq = True
	# --------------------------------------------------------------------------------------------
	
	#print("Faixa Esq: {0} \tFaixa Dir: {1}: ".format(cx_esq, cx_dir))
	#print("Faixa Esq: {0} {1} \tFaixa Dir: {2} {3}".format(status_visao_faixa_esq, cx_esq, status_visao_faixa_dir, cx_dir))

	retorno = [
				img_perspectiva_pista, 
				img_faixa_esq, 
				img_faixa_dir, 
				status_visao_faixa_dir, 
				status_visao_faixa_esq, 
				status_anormalidade_faixa_dir, 
				status_anormalidade_faixa_esq
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


# ####################### FUNCAO DE TRATAMENTO DE DETECCAO DOS OBSTACULOS #######################
def deteccao_obstaculo(img, distancia_obstaculo):

	# ------------- Variaveis que irao definir o status de deteccao das faixas -------------------
	status_visao_faixa_dir, status_visao_faixa_esq = False, False

	status_anormalidade_faixa_dir, status_anormalidade_faixa_esq = False, False
	# --------------------------------------------------------------------------------------------

	# ------------- Variaveis que irao definir o status de deteccao de obstaculos ----------------
	status_obstaculo_visao = False
	status_obstaculo_vl53x = False
	# --------------------------------------------------------------------------------------------

	# --------------------------- Detecção das faixas com Visao ----------------------------------
	img_perspectiva_obstaculos = obstaculo.perspectiva_obstaculo(img)	

	img_filtros_obs = obstaculo.filtros_obstaculos(img_perspectiva_obstaculos) 

	somatorio_matriz = obstaculo.detecta_obstaculos(img_filtros_obs)

	if(somatorio_matriz  > 17000):
		status_obstaculo_visao = True
	# --------------------------------------------------------------------------------------------


	# --------------------------- Detecção das faixas com VL53X ----------------------------------
	if((distancia_obstaculo > 0) and (distancia_obstaculo <= var.CONST_OBSTAC)):
		status_obstaculo_vl53x = True
	# --------------------------------------------------------------------------------------------

	sensor.aciona_buzina(status_obstaculo_visao)

	#print("\nDetectou Obstaculo: {0} \tValor: {1}".format(status_obstaculo_visao, somatorio_matriz))
	#print(somatorio_matriz)
	retorno = [
				img_filtros_obs,
				status_obstaculo_visao, 
				status_obstaculo_vl53x
			  ]	
	
	return retorno
# ###############################################################################################



# ###################### FUNCAO DE TRATAMENTO DA SINALIZACOES A DIREITA #########################
def sinalizacao_direita(img):
	(	
		status_plc_pare, 
		status_plc_pedestre, 
		status_plc_desvio, 
		status_plc_60, 
		status_plc_proib_virar,
		status_vermelho,  
		status_verde 
	) = False, False, False, False, False, False, False  

	nome_placa, distancia_placa = sinalizacao.detecta_placas_direita(img, var.classificadores_placas_direita)

	estado_semaforo, distancia_semaforo, status_verde = sinalizacao.semaforo(img, var.dados_semaforo)
	
	if nome_placa == var.nome_p1 and (distancia_placa > 15 and distancia_placa <= 20):
		status_plc_pare = True

	if nome_placa == var.nome_p2:
		status_plc_desvio = True

	if nome_placa == var.nome_p3 and (distancia_placa > 9 and distancia_placa <= 17):
		status_plc_pedestre = True

	if nome_placa == var.nome_p4 and (distancia_placa > 9 and distancia_placa <= 17):
		status_plc_60 = True

	if nome_placa == var.nome_p5 and (distancia_placa > 9 and distancia_placa <= 17):
		status_plc_proib_virar = True

	if estado_semaforo == var.nome_semaforo_vermelho:
		status_vermelho = True

	if estado_semaforo == var.nome_semaforo_verde:
		status_verde = True

	retorno = [
				status_plc_pare, 
				status_plc_pedestre, 
				status_plc_desvio, 
				status_plc_60, 
				status_plc_proib_virar,
				status_vermelho,  
				status_verde
			  ]
	
	return retorno


# ###############################################################################################



# ###################### FUNCAO DE TRATAMENTO DAS SINALIZACOES A ESQUERDA #######################
def sinalizacao_esquerda(img):
	status_ck_1, status_ck_2, status_ck_3 = False, False, False 
		
	img_area_ck, nome_ck, status_ck_1, status_ck_2, status_ck_3, distancia_placa = sinalizacao.placas_checkpoints(img, var.dados_hsv)
	
	if nome_ck == var.nome_check_1:
		status_ck_1 = True
	if nome_ck == var.nome_check_2:
		status_ck_2 = True
	if nome_ck == var.nome_check_3:
		status_ck_3 = True
	
	return img_area_ck, status_ck_1, status_ck_2, status_ck_3
# ##############################################################################################














