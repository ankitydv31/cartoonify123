import cv2
from functions.outline import edge
def cartoon(img):
  color = cv2.bilateralFilter(img, 9,300,300)
  cartoon = cv2.bitwise_and(color, color, mask = edge())
  cartoon = cv2.detailEnhance(cartoon, sigma_s= 20, sigma_r=0.15)
  return cartoon
