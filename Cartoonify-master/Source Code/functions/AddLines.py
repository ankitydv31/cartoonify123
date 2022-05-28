import cv2
def getedges(img):
    ##converts image to greyscale
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    grey=cv2.medianBlur(grey,1)
    ##grey=cv2.GaussianBlur(grey,(3,3),5,5)
    edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    ##edges=cv2.bitwise_not(edges)
    ##edge=cv2.GaussianBlur(edge,(5,5),cv2.BORDER_DEFAULT)
    bil=cv2.bilateralFilter(img,9,300,300)
    cartoonimg = cv2.bitwise_and(bil, bil, mask=edges)
    return cartoonimg