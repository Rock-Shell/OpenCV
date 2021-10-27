# To draw geometric shapes using cv2
import cv2
import numpy as np

img=cv2.imread('lena.jpg',1)
img=np.zeros([512,512,3],np.uint8)
            # [h, w], data type

img=cv2.line(img,(0,0),(255,255),(255,0,0),5)
            # image, starting point,end point, bgr,thicknes
img=cv2.arrowedLine(img,(260,0),(255,255),(255,0,255),5)

img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),-1)#for -1 thickness the shape will be solid
            #A B         A       D          color  thickness
            #C D
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'Opencv',(10,500),font,4,(0,255,255),10,cv2.LINE_AA)
                 #   text,start point,font

cv2.circle(img,(256,256),5,(0,255,0),-1)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
