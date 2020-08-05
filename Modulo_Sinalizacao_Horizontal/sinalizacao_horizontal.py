#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import glob
import numpy as np

pt_pista_1, pt_pista_2, pt_pista_3, pt_pista_4 = (105,380), (567,380), (80,410), (592,410)
pt_destino_1, pt_destino_2, pt_destino_3, pt_destino_4 = (190,0), (490,0), (190,420), (490,420)

pontos_pista = np.float32([[pt_pista_1], [pt_pista_2], [pt_pista_3], [pt_pista_4]])
pontos_destino = np.float32([[pt_destino_1], [pt_destino_2], [pt_destino_3], [pt_destino_4]])



def filtros(img):
    pass

def get_perspectiva_pista(img):
    pass

def detecta_borda_direita():
    pass


def detecta_borda_esquerda():
    pass


def detecta_faixa_pedestre():
    pass


def sinalizacao_horizontal(img):
    pass