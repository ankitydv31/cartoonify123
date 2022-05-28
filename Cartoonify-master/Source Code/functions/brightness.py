import numpy as np
import cv2
def adjust_brightness(image, brightness):
	invGamma = 1.0 / brightness
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)