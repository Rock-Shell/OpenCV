# mouse events
import numpy as np
import cv2

# to get all events avalable
#events=[i for i in dir(cv2) if 'EVENT' in i ]
#print(events)

def click_event(event,x,y, flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:# print cursor coordinates
        print(x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=str(x) +' ,'+ str(y)
        cv2.putText(img,text,(x-10,y),font,.5,(255,255,255),2)
        cv2.imshow('image',img)

    if event==cv2.EVENT_RBUTTONDOWN:# print bgr channel at the point
        font=cv2.FONT_HERSHEY_SIMPLEX
        try:
            blue=img[y,x,0]
            green=img[y,x,1]
            red=img[y,x,2]
            text=str(blue)+','+str(green)+','+str(red)
        except:
            gray=img[y,x]
            text=str(gray)

        cv2.putText(img,text,(x,y),font,.5,(0,255,0),2)
        cv2.imshow('image',img)


#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("img.png")
# img=cv2.resize(img,(512,512))
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
    # to call function click_event. Additional arguments are passed through param

cv2.waitKey(0)
cv2.destroyAllWindows()
