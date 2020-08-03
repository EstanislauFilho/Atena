import cv2
import numpy as np



caminho_imagem = "10000.jpg"




quadros = cv2.imread(caminho_imagem)

quadros = cv2.resize(quadros, (680,420))

def nada(x): pass

# -------------------------- Interface HSV ------------------------------------
cv2.namedWindow("Interface_HSV")

cv2.createTrackbar("Valor Minimo - H", "Interface_HSV", 0, 179, nada) #Hue
cv2.createTrackbar("Valor Minimo - S", "Interface_HSV", 0, 255, nada) #Saturation
cv2.createTrackbar("Valor Minimo - V", "Interface_HSV", 0, 255, nada) #Value

cv2.createTrackbar("Valor Maximo - H", "Interface_HSV", 179, 179, nada) #Hue
cv2.createTrackbar("Valor Maximo - S", "Interface_HSV", 255, 255, nada) #Saturation
cv2.createTrackbar("Valor Maximo - V", "Interface_HSV", 255, 255, nada) #Value
# -----------------------------------------------------------------------------



while(True):
        
    quadros_hsv = cv2.cvtColor(quadros, cv2.COLOR_BGR2HSV)
    
    val_minimo_H = cv2.getTrackbarPos("Valor Minimo - H", "Interface_HSV")
    val_minimo_S = cv2.getTrackbarPos("Valor Minimo - S", "Interface_HSV")
    val_minimo_V = cv2.getTrackbarPos("Valor Minimo - V", "Interface_HSV")
    
    val_maximo_H = cv2.getTrackbarPos("Valor Maximo - H", "Interface_HSV")
    val_maximo_S = cv2.getTrackbarPos("Valor Maximo - S", "Interface_HSV")
    val_maximo_V = cv2.getTrackbarPos("Valor Maximo - V", "Interface_HSV")
    
    intenso = np.array([val_maximo_H, val_maximo_S, val_maximo_V])
    fraco = np.array([val_minimo_H, val_minimo_S, val_minimo_V])
    mascara = cv2.inRange(quadros_hsv, fraco, intenso)
    imagem_resultado = cv2.bitwise_and(quadros, quadros, mask=mascara)
    
    cv2.imshow("Stream Video", quadros)
    
    cv2.imshow('Interface HSV OpenCV', imagem_resultado)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows() 

# FINALIZADO! Todos os métodos implementados e testados. 


