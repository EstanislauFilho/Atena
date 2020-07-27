#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:32:47 2019

@author: estanislau
"""
import cv2
import glob


nome_pasta = "desvio"
#nome_pasta = "futebol"
#nome_pasta = "igreja"
#nome_pasta = "obras"
#nome_pasta = "pare"
#nome_pasta = "pedestre"
#nome_pasta = "semaforo_verde"
#nome_pasta = "semaforo_vermelho"
#nome_pasta = "servicos"
#nome_pasta = "teatro"
#nome_pasta = "velocidade"


cont_imagem_cinza = 10000
largura_imagem, altura_imagem = 50, 50

caminho_pasta_original = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/plc_"+nome_pasta+"_original/*.jpg"
caminho_pasta_artificial = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/plc_"+nome_pasta+"_artificial/*.jpg"
caminho_pasta_destino = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/plc_"+nome_pasta+"/"




cont_imagem = 11000
total = 0

a = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/a/*.jpg"
b = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/b/*.jpg"
c = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/c/*.jpg"
d = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/d/*.jpg"
e = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/e/*.jpg"
f = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/f/*.jpg" 
g = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/g/*.jpg"
h = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/h/*.jpg"
x = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/i/*.jpg"
j = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/j/*.jpg"

pasta_positivas = "/home/estanislau/Projetos/Atena/Base_Dados/"+nome_pasta+"/plc_"+nome_pasta+"_artificial/"


print("copiando imagens da pasta a/...")
for i in glob.glob(a):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1
print(cont_imagem)  
    

print("copiando imagens da pasta b/...")
for i in glob.glob(b):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1
print(cont_imagem)



print("copiando imagens da pasta c/...")
for i in glob.glob(c):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1
print(cont_imagem)    
    


print("copiando imagens da pasta d/...")
for i in glob.glob(d):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1  
print(cont_imagem)   



print("copiando imagens da pasta e/...")
for i in glob.glob(e):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1   
print(cont_imagem)   
   



print("copiando imagens da pasta f/...")
for i in glob.glob(f):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1    
print(cont_imagem)    
    



print("copiando imagens da pasta g/...")
for i in glob.glob(g):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1   
print(cont_imagem)    
   



print("copiando imagens da pasta h/...")
for i in glob.glob(h):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1   
print(cont_imagem)    



 
print("copiando imagens da pasta i/...")
for i in glob.glob(x):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1   
print(cont_imagem)    
    


print("copiando imagens da pasta j/...")
for i in glob.glob(j):
	imagem = cv2.imread(i)
	try:
		cv2.imwrite(pasta_positivas + str(cont_imagem) + ".jpg", imagem)
	except ValueError:
		print("Falha no salvamento das imagens.")
	cont_imagem += 1  
print(cont_imagem)    

    
    
    
########################## Conversão Escala de Cinza ###################################    
    

print("Iniciando transformação para cinza...")

for i in sorted(glob.glob(caminho_pasta_original)):
    imagem = cv2.imread(i)
    
    try:
        imagem_red = cv2.resize(imagem, (largura_imagem, altura_imagem))
    
        imagem_cinza = cv2.cvtColor(imagem_red, cv2.COLOR_BGR2GRAY)
    except:
        print("Imagem {0} com problema!".format(cont_imagem_cinza))
    
    try:
        cv2.imwrite(caminho_pasta_destino+str(cont_imagem_cinza)+".jpg", imagem_cinza)
    except ValueError:
        print("Falha no salvamento das imagens.")
      
    cont_imagem_cinza += 1
    
print(cont_imagem_cinza)

for i in sorted(glob.glob(caminho_pasta_artificial)):
    imagem = cv2.imread(i)
    
    try:
        imagem_red = cv2.resize(imagem, (largura_imagem, altura_imagem))
    
        imagem_cinza = cv2.cvtColor(imagem_red, cv2.COLOR_BGR2GRAY)
    except:
        print("Imagem {0} com problema!".format(cont_imagem_cinza))
    
    try:
        cv2.imwrite(caminho_pasta_destino+str(cont_imagem_cinza)+".jpg", imagem_cinza)
    except ValueError:
        print("Falha no salvamento das imagens.")
       
    cont_imagem_cinza += 1

print("Fim da transformação cinza das imagens!")











