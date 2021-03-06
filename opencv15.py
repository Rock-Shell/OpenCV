# image gradient and edge detection
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('lena.jpg',0)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)#2- data type
lap=np.uint8(np.absolute(lap))

sobelX=cv2.Sobel(img,cv2.CV_64F, 1 ,0)# 3,4 deriv. of x,y
sobelY=cv2.Sobel(img,cv2.CV_64F, 0 ,1)#
sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))
sobelCombo=cv2.bitwise_or(sobelX,sobelY)

canny=cv2.Canny(img, 100, 200)#,L2gradient=True)



titles=['image','lap','sobelX','sobelY','sobelCombo','CannyEdge']
images=[img,lap,sobelX,sobelY,sobelCombo,canny]
for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
