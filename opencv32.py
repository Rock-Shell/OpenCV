import cv2
import numpy as np

img=cv2.imread("world.png")
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img=cv2.blur(img,(3,3))
ret,thresh=cv2.threshold(img, 244, 255, cv2.THRESH_BINARY)

_,contours=cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# print(len(contours))
# for i in contours:
    # cv2.drawContours(thresh,i,-1,(0,255,0),1)
cv2.imshow('image',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
