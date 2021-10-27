#morphological transformations
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('apple.jpg')
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_,mask=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
_,mask2=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

img2=cv2.bitwise_and(img,img,mask=mask)
##red = np.zeros(img.shape,np.uint8)
##red[:,:,2]=255
##red=cv2.cvtColor(red, cv2.COLOR_BGR2RGB)
##y = cv2.bitwise_and(red,red,mask=mask2)
##img2= y + img2

kernal=np.ones((4,4),np.uint8)
dilation=cv2.dilate(img2,kernal,iterations=10)
# to removes small dots from balls we put a white sqaureover them
erosion=cv2.erode(dilation,kernal,iterations=1)
# erodes the boundaries
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernal)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)
mg=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernal)
th=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernal)



titles=['image','mask','dilation','erosion','opening','closing','mg','th']
images=[img,img2,dilation,erosion,opening,closing,mg,th]


for  i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
