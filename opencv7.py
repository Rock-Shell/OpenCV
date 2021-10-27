# resizing image, adding image
import cv2

img=cv2.imread('messi.jpg')
img2=cv2.imread('chicky.png')

print(img.shape)#return no of rows,columns and channels
print(img.size)#return total no of pixels in mycolorimage
print(img.dtype)# return image datatype
b,g,r=cv2.split(img)# to get bgr channel
img=cv2.merge((b,g,r))

ball=img[148:174,171:207]#y,x
img[148:174,27:63]=ball

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

dst=cv2.addWeighted(img, .7, img2, .3, 0);
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
