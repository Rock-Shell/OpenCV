import cv2
import numpy as np

def subimage(image,center,theta,width,height):
    shape=(image.shape[1],image.shape[0])

    matrix=cv2.getRotationMatrix2D(center=center,angle=theta,scale=1)
    image=cv2.warpAffine(src=image, M=matrix,dsize=shape)

    x=int( center[0]-width/2)
    y=int(center[1]-height/2)

    return image

def click_event(event,x,y, flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        return x,y

null=np.zeros((512,512,3),np.uint8)
img=cv2.imread('jhony.jpg')
img=cv2.resize(img,(512,512))

img=subimage(img, center=(256,256), theta=30,width=0,height=0)
img=cv2.rectangle(img, (139,100),(197,267), (255,255,255))
null=cv2.rectangle(null, (139,40),(197,207), (255,255,255))#139,148
hand=img[100:267,139:197]
#null[100:267,139:197]=hand
null[40:207,139:197]=hand
null=cv2.cvtColor(null,cv2.COLOR_BGR2GRAY)

img=subimage(img, center=(256,256), theta=-30,width=100,height=200)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2=gray

theta= 0
x=-10
for i in range(72):
    if i==0:
        cv2.imshow('image',gray)
        cv2.waitKey(1000)
    if theta==60 or theta==-80:
        x=-x
    theta=theta+x
    img1=subimage(null, center=(165,267), theta=theta,width=0,height=0)#
    _,mask1=cv2.threshold(img1,1,255,cv2.THRESH_BINARY_INV)
    gray=gray2
    gray2=cv2.bitwise_and(gray,mask1)
    gray=gray2+img1

    #cv2.imshow('NULL',img1)
    #cv2.imshow('mask',mask1)
    cv2.imshow('image',gray)
    cv2.waitKey(50)

gray=cv2.bitwise_and(gray,mask1)
cv2.imshow('image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
