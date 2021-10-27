#capturing video through camera and saving it

import cv2
cap=cv2.VideoCapture(0);# for capturing video

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20,(640,480))# for saving the video
#a1=filename, a2=fourcc code    a3=fps        a4=frame dimensions

print(cap.isOpened())
while cap.isOpened():
    ret, frame=cap.read()# ret is T/F frame contains frames
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#or cap.get(3),3 is property id
                                # to get frame width
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# or cap.get(4)
                                # to get frame height

        out.write(frame)

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
