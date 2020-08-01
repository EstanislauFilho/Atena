# -*- coding: utf-8 -*-

import cv2

classificador_60 = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_60.xml')
classificador_desvio = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_desvio.xml')
classificador_igreja = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_igreja.xml')
classificador_museu = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_museu.xml')
classificador_obras = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_obras.xml')
classificador_pare = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_pare.xml')
classificador_pedestre = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_pedestre.xml')
classificador_semaforo = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_semaforo.xml')
classificador_semaforo1 = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_semaforo1.xml')
classificador_servicos = cv2.CascadeClassifier('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Classificadores/cascade_servicos.xml')