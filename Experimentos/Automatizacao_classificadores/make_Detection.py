# -*- coding: utf-8 -*-

import cv2
import vertices_deteccao
import declaracao_classificadores

# O valor de verbose define se vamos usar debugs manuais do código ou não
VERBOSE = False

def realiza_deteccao(classificador60, classificadorDesvio, classificadorIgreja, classificadorMuseu, classificadorObras, classificadorPare, 
                     classificadorPedestre, classificadorSemaforo, classificadorSemaforo1, classificadorServicos, imagem, imagemGray):

    deteccoes = classificador60.detectMultiScale(imagemGray, scaleFactor=1.02,
                                                minNeighbors=5,
                                                minSize=(30,30),
                                                maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_60['init_x'] = x
        vertices_deteccao.regiao_60['init_y'] = y
        vertices_deteccao.regiao_60['final_x'] = x + l
        vertices_deteccao.regiao_60['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Velocidade'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)

    deteccoes = classificadorDesvio.detectMultiScale(imagemGray, scaleFactor=1.02,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_desvio['init_x'] = x
        vertices_deteccao.regiao_desvio['init_y'] = y
        vertices_deteccao.regiao_desvio['final_x'] = x + l
        vertices_deteccao.regiao_desvio['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Desvio'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)
    
    deteccoes = classificadorIgreja.detectMultiScale(imagemGray, scaleFactor=1.02,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_igreja['init_x'] = x
        vertices_deteccao.regiao_igreja['init_y'] = y
        vertices_deteccao.regiao_igreja['final_x'] = x + l
        vertices_deteccao.regiao_igreja['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Igreja'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)

    deteccoes = classificadorMuseu.detectMultiScale(imagemGray, scaleFactor=1.02,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_museu['init_x'] = x
        vertices_deteccao.regiao_museu['init_y'] = y
        vertices_deteccao.regiao_museu['final_x'] = x + l
        vertices_deteccao.regiao_museu['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Museu'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)

    deteccoes = classificadorObras.detectMultiScale(imagemGray, scaleFactor=1.02,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_obras['init_x'] = x
        vertices_deteccao.regiao_obras['init_y'] = y
        vertices_deteccao.regiao_obras['final_x'] = x + l
        vertices_deteccao.regiao_obras['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Obras'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)

    deteccoes = classificadorPare.detectMultiScale(imagemGray, scaleFactor=1.02,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_pare['init_x'] = x
        vertices_deteccao.regiao_pare['init_y'] = y
        vertices_deteccao.regiao_pare['final_x'] = x + l
        vertices_deteccao.regiao_pare['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Pare'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)

    deteccoes = classificadorPedestre.detectMultiScale(imagemGray, scaleFactor=1.02,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_pedestre['init_x'] = x
        vertices_deteccao.regiao_pedestre['init_y'] = y
        vertices_deteccao.regiao_pedestre['final_x'] = x + l
        vertices_deteccao.regiao_pedestre['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Pedestre'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)

    deteccoes = classificadorSemaforo.detectMultiScale(imagemGray, scaleFactor=1.02,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_semaforo['init_x'] = x
        vertices_deteccao.regiao_semaforo['init_y'] = y
        vertices_deteccao.regiao_semaforo['final_x'] = x + l
        vertices_deteccao.regiao_semaforo['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Semaforo'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)

    deteccoes = classificadorSemaforo1.detectMultiScale(imagemGray, scaleFactor=1.02,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_semaforo1['init_x'] = x
        vertices_deteccao.regiao_semaforo1['init_y'] = y
        vertices_deteccao.regiao_semaforo1['final_x'] = x + l
        vertices_deteccao.regiao_semaforo1['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Semafoto1'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)

    deteccoes = classificadorServicos.detectMultiScale(imagemGray, scaleFactor=1.02,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           maxSize=(100,100))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

        vertices_deteccao.regiao_servicos['init_x'] = x
        vertices_deteccao.regiao_servicos['init_y'] = y
        vertices_deteccao.regiao_servicos['final_x'] = x + l
        vertices_deteccao.regiao_servicos['final_y'] = y + a
        declaracao_classificadores.classificadorAtual = 'Servicos'

    if VERBOSE:
        print (x)
        print (l)
        print (x + l)
        print (y + a)