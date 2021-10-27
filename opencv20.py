# making histograms
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('jhony.jpg')
img=cv2.resize(img,(512,512))
#b,g,r=cv2.split(img)

cv2.imshow('img',img)
#cv2.imshow('b',b)
#cv2.imshow('g',g)
#cv2.imshow('r',r)


#plt.hist(b.ravel(),256,[0,256])
#plt.hist(g.ravel(),256,[0,256])
#plt.hist(r.ravel(),256,[0,256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
