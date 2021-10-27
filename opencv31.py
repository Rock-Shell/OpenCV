import cv2
import numpy as np

img=cv2.imread('lena.jpg',0)
img2=np.zeros([510,510],np.uint8)
kernal=[[1,1,1],[1,1,1],[1,1,1]]
kernal=np.array(kernal)*(1/18)
r=range(0,510,4)
for i in r:
    for j in r:
        mat=np.array([img[i,j:j+3],img[i+1,j:j+3],img[i+2,j:j+3]])
        x=np.sum(mat[:3,0]*kernal[:3,0]) + np.sum(mat[:3,1]*kernal[:3,1]) + np.sum(mat[:3,2]*kernal[:3,2])
        img2[i,j]=x
img2=np.pad(img2,pad_width=1,mode='constant',constant_values=0)
cv2.imshow("image",img)
cv2.imshow('image2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
