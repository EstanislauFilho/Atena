"""
Created on Thu Apr 30 21:38:13 2020
@author: estanislau
"""

import cv2

imagem = cv2.imread("1245.jpg")

'''
Definicoes de constantess
'''
# constantes para cortar a imagem - crop
x0, y0, z0 = 0, 130, 0 # upper left
x1, y1, z1 = 679, 380, 0 # lower right

# cor para pintar regiao do flood fill
# unsigned char color[] = { 255, 0, 0 }
color = (128) # cinza
red = ( 255, 0, 0 )
green = ( 0, 255, 0 )
blue = ( 0, 0, 255 )
purple = ( 255, 0, 255 )
white = ( 255, 255, 255 )
black = ( 0, 0, 0 )


def gerar_matriz(n_linhas, n_colunas):
    return [[0] * n_colunas for _ in range(n_linhas)]

def DetectaObstaculos(imgBin, vet):
    # Variáveis e limiares
    minimo_livre_inf = 200  # na parte de baixo da imagem
    minimo_livre_sup = 110  # na parte de cima da imagem
    num_perfis = 15  # quantidade de perfis a serem analisados na imagem

    largura, altura, _ = imgBin.shape

    print("Largura = {0} Altura = {1}".format(largura, altura))

    passo_vertical = altura / num_perfis

    linhas, colunas = 6, 50
    matriz_contagem = gerar_matriz(linhas, 50)

    '''
     matriz_contagem: primeira linha (0) contem codigo da regiao
     1 - Black (desconhecido)
     2 - Red (região livre, na verdade cinza)
     3 - White (faixa)

     Segunda linha (1) contem o numero de pixels seguidos da regiao em determinado perfil da imagem.
     Terceira linha (2) contem o ponto medio da regiao (coordenada x)
     Quarta linha (3) contem 1 se regiao for candidata a pertencer a faixa de pedestre BR
     Quinta linha (4) contem 1 se regiao for candidata a pertencer a faixa de pedestre BW
     Sexta linha (5) contem 1 se regiao for candidata a pertencer a faixa de pedestre WR
    '''

    matriz_perfis = gerar_matriz(num_perfis, 6)

    '''
    matriz_perfis: resultados da analise de cada perfil
    (uma linha por perfil)
    Colunas: y, classificacao, numero de regioes R validas, ponto medio R1, ponto medio R2

    Classificacao:
    1- livre
    2- obstaculo
    3- faixa
    '''

    # int i, j;

    perfil_atual = 0

    # zera matriz perfis
    for i in range(num_perfis):
        for j in range(6):
            matriz_perfis[i][j] = 0

    # ------------------------------------------
    #  Preenche matriz de contagem
    # ------------------------------------------

    # zera matriz contagem
    for i in range(linhas):
        for j in range(colunas):
            matriz_contagem[i][j] = 0

    R, W, B = 0, 0, 0  # conta quantidade de regioes de cada tipo de cada perfil
    total_regioes = 0

    pixel_atual, pixel_anterior = None, None  # 0 - preto, 128 - cinza(pista), 255 - branco
    indice_matriz = 0  # indice da coluna da matriz_contagem
    pixel_inicial, pixel_final, ponto_medio = 0, 0, 0  # posicao x do pixel para calcular ponto medio

    # return matriz_perfis, matriz_contagem

    x, y = 0,0
    for passo_vertical in range(altura):
        print("Perfil : {0}".format(perfil_atual))
        R,W,B = 0, 0, 0
        pixel_anterior = imgBin[0, y] #pega primeiro pixel do perfil
        indice_matriz, pixel_inicial = 0, 0 # indice da coluna da matriz_contagem
                                         # posicao x do pixel para calcular ponto medio
        # 0 - preto, 128 - cinza(pista), 255 - branco
        if(pixel_anterior.all() == 0): # preto
            matriz_contagem[0][0] = 1
            B += B
        elif (pixel_anterior.all() == 128): # cinza
            matriz_contagem[0][0] = 2
            R += R
        elif (pixel_anterior.all() == 255): # branco
            matriz_contagem[0][0] = 3
            W+=W

        # x, y = 0

        for x in range(largura):
            pixel_atual = imgBin[x,y] # percorre todos os pixels do perfil
            if (pixel_atual.all() == pixel_anterior.all()): #
                matriz_contagem[1][indice_matriz] += 1
            else: # mudou de região
                #calcula o ponto médio da região anterior
                pixel_final = x - 1
                ponto_medio = (pixel_final + pixel_inicial)/2
                matriz_contagem[2][indice_matriz] = ponto_medio

                pixel_inicial = x
                indice_matriz += indice_matriz

                if (pixel_atual.all() == 0): # preto
                    matriz_contagem[0][indice_matriz] = 1
                    matriz_contagem[1][indice_matriz] += 1
                    B+=B
                elif (pixel_atual.all() == 128): #cinza
                    matriz_contagem[0][indice_matriz] = 2
                    matriz_contagem[1][indice_matriz] += 1
                    R+=R
                elif (pixel_atual.all() == 255): #branco
                    matriz_contagem[0][indice_matriz] = 3
                    matriz_contagem[1][indice_matriz] += 1
                    W += W
                pixel_anterior = pixel_atual
        # fim
        #for pixels perfil
        #imprime perfil
        #print("Linha da imagem: ")
        # for m in range(largura):
        #   print(imgBin(m, y, 0, 0))

        print("R = {0}, W = {1}, B = {2}".format(R,W,B))

        '''
   
        Analisa perfil atual da imagem  
   
        '''
        indice_R, k, indice_regiao, num_regioesRvalidas = 0,0,0,0
        total_regioes = indice_matriz + 1
        # verificação
        if total_regioes != (R+B+W):
            print("Erro: problema na contagem de regioes.")
        # preencher matriz perfis: y, classificação, numero R validas ou livres, pontos medios
        matriz_perfis[perfil_atual][0] = y # y

        # se há somente uma região R - verifica se possui tamanho minimo
        if R == 1:
            for k in range(total_regioes):
                if matriz_contagem[0][k] == 2:
                    indice_regiao = k
                    break
                # no caso de 1 R, a regiao sera considerada valida (pista) se tiver pixels suficientes
                # se nao tiver pixels suficientes, pode atrapalhar na obtencao do formato da pista
            if y > altura / 2 and matriz_contagem[1][indice_regiao] >= minimo_livre_inf:
                num_regioesRvalidas = 1
                matriz_perfis[perfil_atual][2] = 1 # numero de regioes R validas
                matriz_perfis[perfil_atual][1] = 1 # classificacao
                matriz_perfis[perfil_atual][3] = matriz_contagem[2][indice_regiao] # ponto medio R1
                print("num pixels Rvalida: {0}".format(matriz_contagem[1][indice_regiao]))
            elif y <=altura/2 and matriz_contagem[1][indice_regiao]>=minimo_livre_sup:
                num_regioesRvalidas = 1
                matriz_perfis[perfil_atual][2] = 1 # numero de regioes R validas
                matriz_perfis[perfil_atual][1] = 1 # classificacao
                matriz_perfis[perfil_atual][3] = matriz_contagem[2][indice_regiao] # ponto medio R1
                print("num pixels Rvalida: {0}".format(matriz_contagem[1][indice_regiao]))
            else: # nao ha regiao valida - pista impedida
                matriz_perfis[perfil_atual][1] = 2 # classificacao
        # fim if R == 1:
        if R > 1: # se há mais de uma região do tipo R no perfil
            # encontra regioes R
            for k in range(total_regioes):
                if matriz_contagem[0][k] == 2:
                    indice_regiao = k
                    # regiao valida: WRW quando ha RWRW ou WRWR
                    # verificar se ha pixels suficientes
                    # perfil da metade inferior
                    if y > altura/2 and matriz_contagem[1][indice_regiao] >= minimo_livre_inf:
                        # se esta entre duas regioes W eh valida
                        if indice_regiao -1 > 0 and indice_regiao + 1 < total_regioes: # verifica se tem W antes
                            if matriz_contagem[0][indice_regiao-1] == 3 and matriz_contagem[0][indice_regiao + 1] == 3:
                                # pista livre
                                matriz_perfis[perfil_atual][1] = 1 #classificação
                                matriz_perfis[perfil_atual][2] += 1 # numero de regioes R validas ou livres
                                matriz_perfis[perfil_atual][3 + num_regioesRvalidas] = matriz_contagem[2][indice_regiao] # ponto medio R
                                num_regioesRvalidas += 1
                                print("num pixels Rvalida: {0}".format(matriz_contagem[1][indice_regiao]))
                    #perfil da metade superior
                    if y <= altura/2 and matriz_contagem[1][indice_regiao] >= minimo_livre_sup:
                        # se esta entre duas regioes W eh valida
                        if indice_regiao - 1 > 0 and indice_regiao + 1 < total_regioes: # verifica se tem W antes
                            if matriz_contagem[0][indice_regiao - 1] == 3 and matriz_contagem[0][indice_regiao + 1] == 3:
                                # pista livre
                                matriz_perfis[perfil_atual][1] = 1 # classificação
                                matriz_perfis[perfil_atual][2] += 1 # numero de regioes R validas ou livres
                                matriz_perfis[perfil_atual][3 + num_regioesRvalidas] = matriz_contagem[2][indice_regiao] # ponto medio R
                                num_regioesRvalidas += 1
                                print("num pixels Rvalida: {0}". format(matriz_contagem[1][indice_regiao]))
            # se nenhuma regiao foi valida, ha impedimento na pista ou faixa
            if num_regioesRvalidas == 0:
                matriz_perfis[perfil_atual][1] = 2 # classificação
                matriz_perfis[perfil_atual][2] = 0 # numero de regioes R validas ou livres
        # fim if R > 1
        if R == 0: # pista impedida ou faixa de pedestres
            matriz_perfis[perfil_atual][1] = 2 # classificação

        '''
        verifica se há faixa de pedestres
        
        '''
        if num_regioesRvalidas == 0:
            matriz_perfis[perfil_atual][1] = 2 # classificação
            if VerificaFaixa(total_regioes, matriz_contagem, altura, y):
                matriz_perfis[perfil_atual][1] = 3 # classifcação
        perfil_atual += perfil_atual
        # zera matriz contagem
        for i in range(linhas):
            for j in range(colunas):
                matriz_contagem[i][j] = 0
        # fim for do perfil
        '''
        Analisa perfis da imagem em conjunto
        
        '''
        Imprime_Perfis(matriz_perfis, num_perfis)
        # pista_livre
        # pista_impedida ou pista_impedida a frente
        # faixa ou faixa a frente
        # formato_pista
        # inconclusivo

        livre, imped, faixa, inconc = 1, 2, 3, 0
        imped_sup, imped_inf = 0, 0 # 1 ou mais se impedido, 0 se livre
        faixa_sup, faixa_inf = 0, 0 # 1 ou mais se faixa, 0 c.c.
        p = 0
        corte_imagem = altura/2 + 10 # local da divisao da imagem em superior e inferior na análise dos perfis

        for p in range(num_perfis):
            # se da metade para baixo estiver livre, entao robo pode avancar - pista livre
            if matriz_perfis[p][0] <= corte_imagem: # parte inferior da imagem
               if matriz_perfis[p][1] == faixa: faixa_sup += faixa_sup
               if matriz_perfis[p][1] == imped: imped_sup += imped_sup
               if matriz_perfis[p][1] == inconc: imped_sup += imped_sup
            else: # parte superior da imagem
                if matriz_perfis[p][1] == faixa: faixa_inf += faixa_inf
                if matriz_perfis[p][1] == imped: imped_inf += imped_inf
                if matriz_perfis[p][1] == inconc: imped_inf += imped_inf
            # falta analisar pontos medios para saber informacoes sobre a pista
            # vetor de resultados
            # cada indice corresponde a:
                # 0 - Impedimento
                # 1 - Pista livre
                # 2 - Faixa
                # 3 - Impedimento a frente
                # 4 - Pista livre a frente
                # 5 - Faixa a frente
                # 0 para nao e 1 para sim

            # int q
            vet = [0]*5
            # resultado

            print("Resultados para a imagem: ")
            if imped_inf > 0:
                print("Impedimetno (faixa ou obst.).")
                vet[0] = 1
            else:
                print("Pista livre")
                vet[1] = 1
            if faixa_inf > 0:
                print("Faixa. ")
                vet[2] = 1
            if imped_sup > 0:
                print("Impedimento (faixa ou obst.) a frente. ")
                vet[3] = 1
            else:
                print("Pista livre a frente")
                vet[4] = 1
            if faixa_sup > 0:
                print("Faixa a frente. ")
                vet[5] = 1

def VerificaFaixa(total_regioes, matriz_contagem, altura, y):

    # BRBRBRBRB...(quando inunda faixa)
    # ou BWBWBWBWBWBWB...
    # ou WRWRWRWR... mais de 3 ou 4 repetições
    # regioes R/W serao pequenas e mais ou menos uniformes
    # B 1
    # R 2
    # W 3
    cont_BR, cont_BW, cont_WR = 0, 0, 0 # conta padrao BR ou BW
    largura_ok_BW = 0 # quantas regioes de faixa tem larguras adequadas
    largura_ok_BR = 0 # quantas regioes de faixa tem larguras adequadas
    largura_ok_WR = 0
    # limiares
    larg_faixa_sup = 15 # largura minima da faixa de pedestres na parte superior
    larg_faixa_inf = 25 # largura minima da faixa de pedestres na parte inferior
    limiar_repet = 4 # limiar_repet limiar para quantidade da repeticao do padrao
    limiar_somat_inf = 0.5 # limiar da media das diferencas relativas entre tamanho e media dos tamanhos
    limiar_somat_sup = 0.61

    # Para saber se regioes da faixa sao aproximadamente uniformes:
    # 1. Calcula media dos tamanhos
    # 2. Calcula a media com somatorio de diferencas relativas (media - tamanhos) / media
    # 3. Se somatorio for maior que limiar, nao eh faixa, senao eh faixa

    soma_BW, soma_BR, soma_WR = 0,0,0
    media_BW, media_BR, media_WR =0.0, 0.0, 0.0
    somatorio_dif_BW, somatorio_dif_BR, somatorio_dif_WR = 0,0,0
    media_diferencas_BW, media_diferencas_BR, media_diferencas_WR = 0,0,0
    #int k
    for k in range(total_regioes - 1):
        if matriz_contagem[0][k] == 1 and matriz_contagem[0][k+1] == 2: # padrao BRBRBR...
            cont_BR += cont_BR
            # verifica se R tem tamanho minimo - R inundada
            if matriz_contagem[1][k+1] >= larg_faixa_sup and y <= altura/2: # parte sup
                largura_ok_BR += 1
                soma_BR = soma_BR + matriz_contagem[1][k + 1]
                matriz_contagem[3][k + 1] = 1 # marca regiao como candidata para fazer calculos depois
            if matriz_contagem[1][k + 1] >= larg_faixa_inf and y > altura/2: #parte inf
                largura_ok_BR += 1
                soma_BR = soma_BR + matriz_contagem[1][k + 1]
                matriz_contagem[3][k + 1] = 1 # marca regiao como candidata
        if matriz_contagem[0][k] == 1 and matriz_contagem[0][k + 1] == 3: # padrao BWBWBW...
            cont_BW += 1
            # verifica se W tem tamanho minimo - faixa nao inundada
            if matriz_contagem[1][k + 1] >= larg_faixa_sup and y <= altura/2: # parte sup
                largura_ok_BW += 1
                soma_BW = soma_BW + matriz_contagem[1][k + 1]
                matriz_contagem[4][k + 1] = 1 # marca regiao como candidata
            if matriz_contagem[1][k + 1] >= larg_faixa_inf and y > altura/2: # parte inf
                largura_ok_BW += 1
                soma_BW = soma_BW + matriz_contagem[1][k + 1]
                matriz_contagem[4][k + 1] = 1
        if matriz_contagem[0][k] == 3 and matriz_contagem[0][k+1] == 2: # padrao WRWRWR...
            cont_WR += 1
            # verifica se W tem tamanho minimo - faixa incompleta, mas pista inundada
            if matriz_contagem[1][k] >= larg_faixa_sup and y <= altura/2: # parte sup
                largura_ok_WR += 1
                soma_WR = soma_WR + matriz_contagem[1][k]
                matriz_contagem[5][k] = 1 # marca regiao como candidata
            if matriz_contagem[1][k] >= larg_faixa_inf and y > altura/2: # parte inf
                largura_ok_WR += 1
                soma_WR = soma_WR + matriz_contagem[1][k]
                matriz_contagem[5][k] = 1 # marca regiao como candidata
    print("cont_BR: {0}".format(cont_BR))
    #print("largura_ok_BR: {0}".format(largura_ok_BR))
    print("cont_BW: {0}".format(cont_BW))
    #print("largura_ok_BW: {0}".format(largura_ok_BW))
    print("cont_WR: {0}".format(cont_WR))

    if cont_BR >= limiar_repet: # ha indicativos de que eh faixa
        if largura_ok_BR >= 3: # se largura das regioes B ou R forem adequadas, ha indicio de faixa
            media_BR = soma_BR / largura_ok_BR
            if media_BR < 0:
                print("Erro: media negativa")
            for k in range(total_regioes-1): # calcula somatorio das diferencas relativas
                if matriz_contagem[3][k] == 1:
                    dif = media_BR - matriz_contagem[1][k]
                    somatorio_dif_BR =somatorio_dif_BR + ((dif, -dif)[dif > 0])/media_BR
            media_diferencas_BR = somatorio_dif_BR / largura_ok_BR
            print("somatorio_dif_BR: {0} , media: {1}.".format(somatorio_dif_BR, media_diferencas_BR))
            if media_diferencas_BR <= limiar_somat_inf and y > altura/2: # eh faixa
                return 1
            if media_diferencas_BR <= limiar_somat_sup and y <= altura/2: # eh faixa
                return 1
    if cont_BW >= limiar_repet: # ha indicativos de que eh faixa
        if largura_ok_BW >= 3: # se largura das regioes B ou R forem adequadas, ha indicio de faixa
            media_BW = soma_BW / largura_ok_BW
            if media_BW < 0:
                print("Erro: media negativa")
            for k in range(total_regioes-1): # calcula somatorio das diferencas relativas
                if matriz_contagem[4][k] == 1:
                    dif = media_BW - matriz_contagem[1][k]
                    somatorio_dif_BW =somatorio_dif_BW + ((dif, -dif)[dif > 0])/media_BW
            media_diferencas_BW = somatorio_dif_BW / largura_ok_BW
            print("somatorio_dif_BW: {0} , media: {1}.".format(somatorio_dif_BW, media_diferencas_BW))
            if media_diferencas_BW <= limiar_somat_inf and y > altura/2: # eh faixa
                return 1
            if media_diferencas_BW <= limiar_somat_sup and y <= altura/2: # eh faixa
                return 1
    if cont_WR >= limiar_repet: # ha indicativos de que eh faixa
        if largura_ok_WR >= 3: # se largura das regioes B ou R forem adequadas, ha indicio de faixa
            media_WR = soma_WR / largura_ok_WR
            if media_WR < 0:
                print("Erro: media negativa")
            for k in range(total_regioes-1): # calcula somatorio das diferencas relativas
                if matriz_contagem[5][k] == 1:
                    dif = media_WR - matriz_contagem[1][k]
                    somatorio_dif_WR =somatorio_dif_WR + ((dif, -dif)[dif > 0])/media_WR
            media_diferencas_WR = somatorio_dif_WR / largura_ok_WR
            print("somatorio_dif_WR: {0} , media: {1}.".format(somatorio_dif_WR, media_diferencas_WR))
            if media_diferencas_WR <= limiar_somat_inf and y > altura/2: # eh faixa
                return 1
            if media_diferencas_WR <= limiar_somat_sup and y <= altura/2: # eh faixa
                return 1
    # obs1: nao eh verificado se faixa tem tamanho maximo, apenas tamanho minimo.
    # obs2: obstaculo na faixa nao foi testado.
    return 0

def Imprime_Perfis(matriz, num_perfis):
  i, j = 0, 0
  print("Perfis da imagem. ")
  print("y | Classif. | Num. Rvalidas | Pontos medios")
  for i in range(num_perfis):
    print(" {0} ".format(matriz[1][0])) #y
    # classif
    if matriz[i][1] == 0:
      print(" inconc.   |")
      pass
    elif matriz[i][1] == 1:
      print(" livre   |")
      pass
    elif matriz[i][1] == 2:
      print(" imped.   |")
      pass
    elif matriz[i][1] == 3:
      print(" faixa   |")
      pass
    else:
      print(" erro    |")
      pass
  print("    {0}    |".format(matriz[i][2])) # Num. Rvalidas
  for j in range(matriz[i][2]): # Pontos medios
    print(" {0} ".format(matriz[i][3 + j]))

'''
Escreve resultado na imagem
'''
def EscreveResultadoImagem(image, vet):
  espaco = 25 # espaco vertical
  j = 5 # local da escrita

  fonte = cv2.FONT_HERSHEY_SIMPLEX
  lineType = 0.5

  if vet[0] == 1:
    cv2.putText(image, "Impedimento (faixa ou obst.).", (3, j), fonte, lineType, purple)
    j = j + espaco
  if vet[1] == 1:
    cv2.putText(image, "Pista livre.", (3, j), fonte, lineType, purple)
    j = j + espaco
  if vet[2] == 1:
    cv2.putText(image, "Faixa de pedestres.", (3, j), fonte, lineType, purple)
    j = j + espaco
  if vet[3] == 1:
    cv2.putText(image, "Impedimento (faixa ou obst.) a frente.", (3, j), fonte, lineType, blue)
    j = j + espaco
  if vet[4] == 1:
    cv2.putText(image, "Pista livre a frente.", (3, j), fonte, lineType, blue)
    j = j + espaco
  if vet[5] == 1:
    cv2.putText(image, "Faixa de pedestres a frente.", (3, j), fonte, lineType, blue)
    j = j + espaco
  return image

def CalculaAreaLivre(image, limiar):
    # carrega imagem
    grayWeight, imgR, imgG, imgB, imgBin = None, None, None, None, None
    grayWeight[image.width(), image.height(), 1, 1, 0]
    imgBlur = image
    imgR[image.width(), image.height(), 1, 3, 0]
    imgG[image.width(), image.height(), 1, 3, 0]
    imgB[image.width(), image.height(), 1, 3, 0]
    imgBin[image.width(), image.height(), 1, 1, 0]

    imgBlur.blur_median(3)


    # for all pixels x, y in image
    for x, y in range(image):
        imgR[x, y, 0, 0] = imgBlur[x, y, 0, 0] # Red component of image sent to imgR
        imgG[x, y, 0, 1] = imgBlur[x, y, 0, 1]  # Green component of image sent to imgG
        imgB[x, y, 0, 2] = imgBlur[x, y, 0, 2] # Blue component of image sent to imgB
        # separation of channels
        R = imgBlur[x, y, 0, 0]
        G = imgBlur[x, y, 0, 1]
        B = imgBlur[x, y, 0, 2]

        # Real weighted addition of channels for gray
        grayValueWeight = (0.299 * R + 0.587 * G + 0.114 * B)
        # saving pixel values into image information
        grayWeight[x, y, 0, 0] = grayValueWeight

        # binarização simples
        if grayWeight[x, y, 0, 0] > limiar:
            imgBin[x, y, 0, 0] = 255
        else:
            imgBin[x, y, 0, 0] = 0

    # corta imagem
    imgBin.crop(x0, y0, z0, x1, y1, z1)

    # flood fill na faixa preta
    # pixel inicial - seed
    x3 = imgBin.width()/2
    y3 = imgBin.height() - 1 # centro inferior

    imgBin.draw_fill(x3, y3, color)
    return imgBin
'''                 

         linha 621.cpp = fim void DetectaObstaculos 
         
         linha 798.cpp = fim void VerificaFaixa
         
         linha 647 = fim void Imprime_Perfis
        
         linha 846 = fim EscreveResultadoImagem
         
         linha 248 = fim CalculaAreaLivre
         
         constantes definidas
         
'''

# ------------------------- Main -------------------------
# matriz_perfis, matriz_contagem = DetectaObstaculos(imagem, None)
DetectaObstaculos(imagem, None)
cv2.imshow("Imagem Pista", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
