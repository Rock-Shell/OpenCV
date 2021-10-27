# setting camera values
import cv2
import datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#property 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#property 4

#cap.set(3,1208)
#cap.set(4,720)

#print(cap.get(3))
#print(cap.get(4))
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:

        font=cv2.FONT_HERSHEY_SIMPLEX
        text="width"+str(cap.get(3))+" height"+str(cap.get(4))
        date=str(datetime.datetime.now())
        frame=cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)

        frame=cv2.putText(frame,date,(10,100),font,1,(0,255,255),2,cv2.LINE_AA)

        #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
