import time
import picamera
#from picamera import PiCamera

with picamera.PiCamera() as camera:
	camera.resolution = (1040, 780)
	camera.start_preview()
	camera.start_recording('/home/pi/Desktop/video.h264')
	time.sleep(240)
	camera.stop_recording()
	camera.stop_preview()
