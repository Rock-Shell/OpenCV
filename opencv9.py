#Trackbars in opencv
#COLOR MIXER
import numpy as np
import cv2

def nothing(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

switch="ON/OFF"#"0: OFF\n 1: "
cv2.createTrackbar(switch,'image',0,1,nothing)


while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break

    b=cv2.getTrackbarPos('B','image')
    g=cv2.getTrackbarPos('G','image')
    r=cv2.getTrackbarPos('R','image')
    s=cv2.getTrackbarPos(switch,'image')

    if s==1:
        img[:]=[b,g,r]

cv2.destroyAllWindows()
