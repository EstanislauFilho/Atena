#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:22:38 2020

@author: estanislau
"""

import cv2


#nome_pasta = "desvio"
#nome_pasta = "futebol"
#nome_pasta = "igreja"
#nome_pasta = "obras"
#nome_pasta = "pare"
#nome_pasta = "pedestre"
#nome_pasta = "semaforo_verde"
#nome_pasta = "semaforo_vermelho"
#nome_pasta = "servicos"
#nome_pasta = "teatro"
nome_pasta = "velocidade"

video1 = cv2.VideoCapture("/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/a.webm")
video2 = cv2.VideoCapture("/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/b.webm")
video3 = cv2.VideoCapture("/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/c.webm")
video4 = cv2.VideoCapture("/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/d.webm")
video5 = cv2.VideoCapture("/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/e.webm")
video6 = cv2.VideoCapture("/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/f.webm")
video7 = cv2.VideoCapture("/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/g.webm")
video8 = cv2.VideoCapture("/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/h.webm")
video9 = cv2.VideoCapture("/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/i.webm")


a = "/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/a/"
b = "/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/b/"
c = "/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/c/"
d = "/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/d/"
e = "/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/e/"
f = "/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/f/" 
g = "/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/g/"
h = "/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/h/"
i = "/home/estanislau/Projetos/Atena/base_dados/"+nome_pasta+"/i/"


cont_imagem_1 = 10000
print("Extraindo frames do video a...")
while(True):
    verif, frame = video1.read()
    if verif is True:   
        cv2.imwrite(a + str(cont_imagem_1) + ".jpg", frame)
        cont_imagem_1 += 1
        
    else:
        print("Todos os frames do video a gravadas com sucesso!")
        break
  
    

cont_imagem_1 = 10000
print("Extraindo frames do video b...")
while(True):
    verif, frame = video2.read()
    if verif is True:   
        cv2.imwrite(b + str(cont_imagem_1) + ".jpg", frame)
        cont_imagem_1 += 1
        
    else:
        print("Todos os frames do video b gravadas com sucesso!")
        break
    
    
    

cont_imagem_1 = 10000
print("Extraindo frames do video c...")
while(True):
    verif, frame = video3.read()
    if verif is True:   
        cv2.imwrite(c + str(cont_imagem_1) + ".jpg", frame)
        cont_imagem_1 += 1
        
    else:
        print("Todos os frames do video c gravadas com sucesso!")
        break    
    

    
cont_imagem_1 = 10000
print("Extraindo frames do video d...")
while(True):
    verif, frame = video4.read()
    if verif is True:   
        cv2.imwrite(d + str(cont_imagem_1) + ".jpg", frame)
        cont_imagem_1 += 1
        
    else:
        print("Todos os frames do video d gravadas com sucesso!")
        break    

  
    

cont_imagem_1 = 10000
print("Extraindo frames do video e...")
while(True):
    verif, frame = video5.read()
    if verif is True:   
        cv2.imwrite(e + str(cont_imagem_1) + ".jpg", frame)
        cont_imagem_1 += 1
        
    else:
        print("Todos os frames do video e gravadas com sucesso!")
        break    
     
 
    
    
cont_imagem_1 = 10000
print("Extraindo frames do video f...")
while(True):
    verif, frame = video6.read()
    if verif is True:   
        cv2.imwrite(f + str(cont_imagem_1) + ".jpg", frame)
        cont_imagem_1 += 1
        
    else:
        print("Todos os frames do video f gravadas com sucesso!")
        break     
    


cont_imagem_1 = 10000
print("Extraindo frames do video g...")
while(True):
    verif, frame = video7.read()
    if verif is True:   
        cv2.imwrite(g + str(cont_imagem_1) + ".jpg", frame)
        cont_imagem_1 += 1
        
    else:
        print("Todos os frames do video g gravadas com sucesso!")
        break 



cont_imagem_1 = 10000
print("Extraindo frames do video h...")
while(True):
    verif, frame = video8.read()
    if verif is True:   
        cv2.imwrite(h + str(cont_imagem_1) + ".jpg", frame)
        cont_imagem_1 += 1
        
    else:
        print("Todos os frames do video h gravadas com sucesso!")
        break 

 
cont_imagem_1 = 10000
print("Extraindo frames do video i...")
while(True):
    verif, frame = video9.read()
    if verif is True:   
        cv2.imwrite(i + str(cont_imagem_1) + ".jpg", frame)
        cont_imagem_1 += 1
        
    else:
        print("Todos os frames do video i gravadas com sucesso!")
        break 
    
    
print("Processo Finalizado!")    
    
    