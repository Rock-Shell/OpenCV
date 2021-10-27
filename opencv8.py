# bitwise opeators on images

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=np.zeros((250,500,3),np.uint8)#y,x
img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)#x,y

img2=np.zeros((250,500,3),np.uint8)
img2=cv2.rectangle(img2,(250,0),(500,250),(255,255,255),-1)

bitAnd=cv2.bitwise_and(img2,img1)
bitOr=cv2.bitwise_or(img2,img1)
bitXor=cv2.bitwise_xor(img2,img1)
bitNot=cv2.bitwise_not(img2)

images=[img1,img2,bitAnd,bitOr,bitXor,bitNot]
titles=['img1','img2','bitAnd','bitOr','birXor','bitNot']

for i in range(6):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
# cv2.imshow('bitAnd',bitAnd)
# cv2.imshow('bitor',bitOr)
# cv2.imshow('bitXor',bitXor)
# cv2.imshow('bitNot',bitNot)
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()
