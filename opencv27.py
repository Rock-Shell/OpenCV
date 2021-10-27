# background substraction
import cv2
import numpy as np
cap=cv2.VideoCapture('vtest.avi')
#fgbg1= cv2.createBackgroundSubtractorMOG2(detectShadows=True)
#fgbg2=cv2.bgsegm.createBackgroundSubtractorMOG()
#kernal=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#fgbg=cv2.bgsegm.createBackgroundSubtractorGMG()#kernal
fgbg=cv2.createBackgroundSubtractorKNN()
while True:
    ret,frame=cap.read()
    if frame is None:
        break
    fgmask=fgbg.apply(frame)
    #fgmask=cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernal)

    cv2.imshow('frame',frame)
    cv2.imshow('fg mask',fgmask)

    keyboard=cv2.waitKey(30)
    if keyboard=='q' or keyboard==27:
        break
cap.release()
cv2.destroyAllWindows()
