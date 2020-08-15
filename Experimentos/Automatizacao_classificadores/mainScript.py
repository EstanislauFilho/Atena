# -*- coding: utf-8 -*-

import cv2
import csv
import make_Detection
import declaracao_classificadores
import vertices_deteccao
import time

# Escrita dos dados manipulados em arquivo .csv
with open('regiao_deteccao.csv', 'w') as arquivo_csv:
    colunas = ['Imagem', 'widht', 'height', 'class', 'init_x_60', 'init_y_60', 'final_x_60', 'final_y_60',
            'init_x_desvio', 'init_y_desvio', 'final_x_desvio', 'final_y_desvio',
            'init_x_igreja', 'init_y_igreja', 'final_x_igreja', 'final_y_igreja',
            'init_x_museu', 'init_y_museu', 'final_x_museu', 'final_y_museu',
            'init_x_obras', 'init_y_obras', 'final_x_obras', 'final_y_obras',
            'init_x_pare', 'init_y_pare', 'final_x_pare', 'final_y_pare',
            'init_x_pedestre', 'init_y_pedestre', 'final_x_pedestre', 'final_y_pedestre',
            'init_x_semaforo', 'init_y_semaforo', 'final_x_semaforo', 'final_y_semaforo',
            'init_x_semaforo1', 'init_y_semaforo1', 'final_x_semaforo1', 'final_y_semaforo1',
            'init_x_servicos', 'init_y_servicos', 'final_x_servicos', 'final_y_servicos']
    
    escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    escrever.writeheader()

    # Controle do índice de imagem 
    # Coloque sempre o índice da primeira imagem que é de interesse
    imagemAtual = 100

    while imagemAtual:
        # Leitura da imagem e conversão em escala de cinza
        imagem = cv2.imread('/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Frames_Pare/' + str(imagemAtual) + '.jpg')
        try:
            imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        except:
            arquivo_csv.close()
            print('Imagem não encontrada ou acabaram as imagens! Encerrando em  3s...')
            time.sleep(3)
            exit(1)

        # Chamada da função para realizar as detecções
        make_Detection.realiza_deteccao(declaracao_classificadores.classificador_60, declaracao_classificadores.classificador_desvio, 
                                        declaracao_classificadores.classificador_igreja, declaracao_classificadores.classificador_museu,
                                        declaracao_classificadores.classificador_obras, declaracao_classificadores.classificador_pare,
                                        declaracao_classificadores.classificador_pedestre, declaracao_classificadores.classificador_semaforo,
                                        declaracao_classificadores.classificador_semaforo1, declaracao_classificadores.classificador_servicos,
                                        imagem, imagemcinza)


        # Trecho para armazenar o nome da imagem
        # Vale ressaltar que só vale para imagens no mesmo diretório
        diretorio = '/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Frames_Pare/' + str(imagemAtual) + '.jpg'
        trechoComum = '/home/joaopaulo/Documentos/git-BCE/Automatizacao_classificadores/Frames_Pare/'
        nomeImagem = diretorio.split(trechoComum)

        escrever.writerow({'Imagem': nomeImagem[1], 'widht': 'NA', 'height': 'NA', 'class': declaracao_classificadores.classificadorAtual, 'init_x_60': vertices_deteccao.regiao_60['init_x'], 'init_y_60': vertices_deteccao.regiao_60['init_y'], 
                            'final_x_60': vertices_deteccao.regiao_60['final_x'], 'final_y_60': vertices_deteccao.regiao_60['final_y'],
                            'init_x_desvio': vertices_deteccao.regiao_desvio['init_x'], 'init_y_desvio': vertices_deteccao.regiao_desvio['init_y'], 
                            'final_x_desvio': vertices_deteccao.regiao_desvio['final_x'], 'final_y_desvio': vertices_deteccao.regiao_desvio['final_y'],
                            'init_x_igreja': vertices_deteccao.regiao_igreja['init_x'], 'init_y_igreja': vertices_deteccao.regiao_igreja['init_y'], 
                            'final_x_igreja': vertices_deteccao.regiao_igreja['final_x'], 'final_y_igreja': vertices_deteccao.regiao_igreja['final_y'],
                            'init_x_museu': vertices_deteccao.regiao_museu['init_x'], 'init_y_museu': vertices_deteccao.regiao_museu['init_y'], 
                            'final_x_museu': vertices_deteccao.regiao_museu['final_x'], 'final_y_museu': vertices_deteccao.regiao_museu['final_y'],
                            'init_x_obras': vertices_deteccao.regiao_obras['init_x'], 'init_y_obras': vertices_deteccao.regiao_obras['init_y'], 
                            'final_x_obras': vertices_deteccao.regiao_obras['final_x'], 'final_y_obras': vertices_deteccao.regiao_obras['final_y'],
                            'init_x_pare': vertices_deteccao.regiao_pare['init_x'], 'init_y_pare': vertices_deteccao.regiao_pare['init_y'], 
                            'final_x_pare': vertices_deteccao.regiao_pare['final_x'], 'final_y_pare': vertices_deteccao.regiao_pare['final_y'],
                            'init_x_pedestre': vertices_deteccao.regiao_pedestre['init_x'], 'init_y_pedestre': vertices_deteccao.regiao_pedestre['init_y'], 
                            'final_x_pedestre': vertices_deteccao.regiao_pedestre['final_x'], 'final_y_pedestre': vertices_deteccao.regiao_pedestre['final_y'],
                            'init_x_semaforo': vertices_deteccao.regiao_semaforo['init_x'], 'init_y_semaforo': vertices_deteccao.regiao_semaforo['init_y'], 
                            'final_x_semaforo': vertices_deteccao.regiao_semaforo['final_x'], 'final_y_semaforo': vertices_deteccao.regiao_semaforo['final_y'],
                            'init_x_semaforo1': vertices_deteccao.regiao_semaforo1['init_x'], 'init_y_semaforo1': vertices_deteccao.regiao_semaforo1['init_y'], 
                            'final_x_semaforo1': vertices_deteccao.regiao_semaforo1['final_x'], 'final_y_semaforo1': vertices_deteccao.regiao_semaforo1['final_y'],
                            'init_x_servicos': vertices_deteccao.regiao_servicos['init_x'], 'init_y_servicos': vertices_deteccao.regiao_servicos['init_y'], 
                            'final_x_servicos': vertices_deteccao.regiao_servicos['final_x'], 'final_y_servicos': vertices_deteccao.regiao_servicos['final_y']})

        vertices_deteccao.setClean()
        imagemAtual += 1

    arquivo_csv.close()



# Trecho de código para manipulação da saída em console
'''
    leitor = csv.DictReader(arquivo_csv, delimiter=’,’)
    for coluna in leitor:
        print(coluna)
'''

# Variações do trecho de código acima podem ser feitas utilizando os recursos de dicionários, a exemplo do trecho a seguir:
# Serão exibidos apenas os valores contidos na coluna 'init_x'
'''
    leitor = csv.DictReader(arquivo_csv, delimiter=’,’)
    for coluna in leitor:
        print(coluna['init_x'])
'''