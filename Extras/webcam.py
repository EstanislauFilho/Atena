


import cv2

webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 840)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 680)

cont_frames = 0

while(True):
	# O vetor com os frames capturados sao armazenados no vetor image	
	conexao, imagem = webcam.read()

	# Apresenta as imagens capturas por meio dos frames
	cv2.imshow("Original", imagem)


	print(cont_frames)	

	cont_frames += 1	
	# Se prescionar a tecla Esc sai do programa
	if cv2.waitKey(1) & 0xFF == 27:
		break

webcam.release()
cv2.destroyAllWindows()



