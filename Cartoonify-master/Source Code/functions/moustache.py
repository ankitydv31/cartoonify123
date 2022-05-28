import cv2
import numpy as np
def AddMoustache(cartoonimg,img):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    nose_cascade = cv2.CascadeClassifier('source code\Haarcascades\\nose.xml')
    must=cv2.imread("source code\Assets\mustache.png",cv2.IMREAD_UNCHANGED)
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(grey,1.15,5)
    nose=nose_cascade.detectMultiScale(grey,1.2,5)
    added_image=cartoonimg

    for (x, y, w, h) in faces:
            blue_ch, green_ch, red_ch = cv2.split(cartoonimg)
            alpha_ch = np.ones(blue_ch.shape, dtype=blue_ch.dtype) *0.01
            alpha_ch=alpha_ch.astype(np.uint8)
            cartoonimg = cv2.merge((blue_ch, green_ch, red_ch, alpha_ch))
            grey_small = grey[y:y+h, x:x+w]
            colour_small = cartoonimg[y:y+h, x:x+w]
            nose=nose_cascade.detectMultiScale(grey_small,1.2,5)
            for (nx, ny, nw1, nh1) in nose:
                muswidth=nw1*3
                must=cv2.imread("source code\Assets\mustache.png",cv2.IMREAD_UNCHANGED)
                origH, origW = must.shape[:2]
                
                musHeight = int(muswidth * origH / origW)
                Xs=int(nx-(muswidth/4))
                Xe=int(nx+nw1+(muswidth/4))
                Ys=int(ny+nh1-(musHeight/2))
                Ye=int(ny+nh1+(musHeight/2))
                if Xs < 0:
                    Xs = 0
                if Ys < 0:
                    Ys = 0
                if Xe > w:
                    Xe = w
                if Ye > h:
                    Ye = h
                img1=colour_small[Ys:Ye, Xs:Xe]
                musHeight=Ye-Ys
                muswidth=Xe-Xs
                must_resized=cv2.resize(must,(muswidth,musHeight))
                added_image=must_resized
                for i in range(0,img1.shape[0]):
                    for j in range(0,img1.shape[1]):
                        if(must_resized[i][j][3]==0):
                            added_image[i][j]=img1[i][j]
                        else:
                            added_image[i][j]=must_resized[i][j]
                cartoonimg[y+Ys:y+Ye, x+Xs:x+Xe] = added_image
                break
            
            blue_ch, green_ch, red_ch,alpha_ch = cv2.split(cartoonimg)
            cartoonimg = cv2.merge((blue_ch, green_ch, red_ch))
    return(cartoonimg)
