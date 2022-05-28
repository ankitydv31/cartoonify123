import cv2
import numpy as np
def AddEyePatch(cartoonimg,img):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.15,5)
    for (x, y, w, h) in faces:
            blue_ch, green_ch, red_ch = cv2.split(cartoonimg)
            alpha_ch = np.ones(blue_ch.shape, dtype=blue_ch.dtype) *0.01
            alpha_ch=alpha_ch.astype(np.uint8)
            cartoonimg = cv2.merge((blue_ch, green_ch, red_ch, alpha_ch))
            grey_small = grey[y:y+h, x:x+w]
            colour_small = cartoonimg[y:y+h, x:x+w]
            eyes=eye_cascade.detectMultiScale(grey_small,1.2,5)
            for (ex, ey, w1, h1) in eyes:
                img1=colour_small[ey:ey+h1, ex:ex+w1]
                flare=cv2.imread("source code\Assets\eyepatch.png",cv2.IMREAD_UNCHANGED)
                flare_resized=cv2.resize(flare,(w1,h1))
                added_image=flare_resized
                for i in range(0,img1.shape[0]):
                    for j in range(0,img1.shape[1]):
                        if(flare_resized[i][j][3]==0):
                            added_image[i][j]=img1[i][j]
                        else:
                            added_image[i][j]=flare_resized[i][j]
                
                cartoonimg[y+ey:y+ey+h1, x+ex:x+ex+w1] = added_image
                blue_ch, green_ch, red_ch,alpha_ch = cv2.split(cartoonimg)
                cartoonimg = cv2.merge((blue_ch, green_ch, red_ch))
                break
    return cartoonimg