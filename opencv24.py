#circle detection
import numpy as np
import cv2
img=cv2.imread("shapes.jpg")
output=img.copy()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,30, param1=50,
                        param2=30, minRadius=0,maxRadius=30)
            #image, method, dp, min distance, param1, param2, minradius, maxradius
            # screenshots dekhie

detected_circles=np.uint8(np.around(circles))
for (x,y,r) in detected_circles[0, :]:
    cv2.circle(output, (x,y),r, (0,255,0),3)
    cv2.circle(output, (x,y),2, (0,0,0),3)

cv2.imshow("output",output)
cv2.waitKey(0)
cv2.destroyAllWindows()
