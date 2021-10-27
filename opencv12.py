# image thresholding
#adaptive thresholding
import cv2
import numpy as np
from matplotlib import pyplot as plt

#img=cv2.imread('gradient.png')
img=cv2.imread('apple.jpg',0)

_,th1=cv2.threshold(img,100,255,cv2.THRESH_BINARY)# if value lies in range gives 1 else 0
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)# inverse of binary
_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)# for given range value remains 127
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#0 for out of range values
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
th6=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C ,cv2.THRESH_BINARY,11,2);
th7=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C ,cv2.THRESH_BINARY,11,2);



#cv2.imshow('Image',img)
#cv2.imshow('th1',th1)
#cv2.imshow('th2',th2)
#cv2.imshow('th3',th3)
#cv2.imshow('th4',th4)
#cv2.imshow('th5',th5)
#cv2.imshow('th6',th6)
#cv2.imshow('th7',th7)
titles=['original','binary','inverse binary','trunc','tozero','TOZERO_INV','ADAPTIVE_mean','ADAPTIVE_GAUSSIAN']
images=[img,th1,th2,th3,th4,th5,th6,th7]

for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')# 2 rows 4 col
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
