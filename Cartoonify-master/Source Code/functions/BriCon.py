import cv2
import numpy as np
def Brightness_contrast(img,bright_val,cont_val):
    img=cv2.addWeighted(img,cont_val,np.zeros(img.shape,img.dtype),1,bright_val)
    return img