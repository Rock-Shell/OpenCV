import cv2
import numpy as np

img=cv2.imread("messi.jpg")
mask=np.zeros(img.shape[:2],np.uint8)

#newmask=cv2.imread("messi5.jpg",0)
#mask[newmask==0]=0
#mask[newmask==255]=1

bgdModel=np.zeros((1,65),np.float64)
fgdModel=np.zeros((1,65),np.float64)

newmask=cv2.imread("messi5.jpg",0)
mask[newmask==0]=0
mask[newmask==255]=1
cv2.imshow('mask',mask)
mask,bgdModel,fgdModel=cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
mask=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask[:,:,np.newaxis]
cv2.imshow('image1',img)

mask=np.zeros(img.shape[:2],np.uint8)
rect=(50,50,450,290)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')# condition,if true,if false
img=img*mask2[:,:,np.newaxis]
cv2.imshow("image2",img)

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

##img=cv2.imread("messi.jpg")
##mask=np.zeros(img.shape[:2],np.uint8)
##bgdModel=np.zeros((1,65),np.float64)
##fgdModel=np.zeros((1,65),np.float64)
##rect=(38,15,150,180)
##cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
##mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
##img=img*mask2[:,:,np.newaxis]
##
## gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
## x=255
## while x!=0:
##     gray=np.where(gray==x,0,gray)
##     cv2.imshow('image',gray)
##     x=x-1
##     cv2.waitKey(10)
##
## mask3=np.zeros(img.shape[:2],np.uint8)
## mask4=np.ones(img.shape[:2],np.uint8)
## mask4=mask4*255
## mask3=np.where(gray==0,mask3,mask4)
##cv2.imshow("image",img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
