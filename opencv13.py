# Blurring images
import cv2
from matplotlib import pyplot as plt
import numpy as np
# matplotlib reads image in bgr format, cv2 reads in  rgb fromat
# low pass filter helps in blurring images and removing noises
# HPF helps in finding edges in the images

img=cv2.imread('lena.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernal=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernal)
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
mblur=cv2.medianBlur(img,5)
bf=cv2.bilateralFilter(img,9,75,75)


titles=['image','2D conv.','blur','GBlur','median','bf']
images=[img,dst,blur,gblur,mblur,bf]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
