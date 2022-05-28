import cv2
def img(img,height,width):
  multx = 600/width
  multy = 600/height
  k = min(multx, multy)
  img = cv2.resize(img, (0,0), fx = k, fy = k)
  return img
