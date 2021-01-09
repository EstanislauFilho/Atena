# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import glob



numero_pasta = '11'

caminho_pasta = '/home/estanislau/Projetos/TCC/Avaliacao/Imagens_Avaliacao/FRAMES_VIDEO_SIN_VER_HOR_'+numero_pasta+'/*.jpg'


sys.path.append("/home/estanislau/Projetos/tensorflow1/models/research/object_detection/")

from utils import label_map_util
from utils import visualization_utils as vis_util

PATH_TO_CKPT = '/home/estanislau/Projetos/tensorflow1/models/research/object_detection/inference_graph/frozen_inference_graph.pb'

PATH_TO_LABELS = '/home/estanislau/Projetos/tensorflow1/models/research/object_detection/training/labelmap.pbtxt'


NUM_CLASSES = 16

cont_imagem = 1000

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')


detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')


detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

try:
	for i in sorted(glob.glob(caminho_pasta)):  
		image = cv2.imread(i)
		image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		image_expanded = np.expand_dims(image_rgb, axis=0)


		(boxes, scores, classes, num) = sess.run(
			[detection_boxes, detection_scores, detection_classes, num_detections],
			feed_dict={image_tensor: image_expanded})

		_, vetorDicionario = vis_util.visualize_boxes_and_labels_on_image_array(
			image,
			np.squeeze(boxes),
			np.squeeze(classes).astype(np.int32),
			np.squeeze(scores),
			category_index,
			use_normalized_coordinates=True,
			line_thickness=5,
			min_score_thresh=0.60)


		print(len(vetorDicionario))

		for dicionario in vetorDicionario:
			for classe, coord in dicionario.items():
				print("Classe: {0}, Coordenadas: {1}".format(classe, coord))
			

		#print("Frame: {}".format(cont_imagem))   

		print()
		cv2.imshow("Object detector ", image)
		cv2.waitKey(0)


		cont_imagem += 1
		if cv2.waitKey(1) & 0xFF == 27:
			cv2.destroyAllWindows()	

		if cv2.waitKey(1) & 0xFF == ord('q'):
			print("Saida forçada!")
			break
except:
	cv2.destroyAllWindows()

finally:
    cv2.destroyAllWindows()	

# Clean up
cv2.destroyAllWindows()
