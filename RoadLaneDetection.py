import numpy as np
import cv2
from matplotlib import pyplot as plt

def roi(img,vertices):
    mask=np.zeros_like(img)
    #channel_count=img.shape[2]
    match_mask_color=255
    cv2.fillPoly(mask,vertices, match_mask_color)
    masked_image=cv2.bitwise_and(img,mask)
    return masked_image

def draw_lines(img,lines):
    img=np.copy(img)
    blank_image=np.zeros((img.shape[0],img.shape[1],3), dtype=np.uint8)
    print(blank_image.shape)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image, (x1,y1),(x2,y2),(0,255,0),thickness=3)

    img=cv2.addWeighted(img, 0.8,blank_image,1,0.0)
    return img

image=cv2.imread("highway.jpg")
image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(image.shape)
height=image.shape[0]
width=image.shape[1]
roiv=[
#(0,height),
(0,140),
(width/2,height/3+15),
(width,140),
#(width, height)
]# region of interest vertices
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray, 100,200)
#plt.imshow(canny)
masked_image=roi(canny, np.array([roiv], np.int32))
lines= cv2.HoughLinesP(masked_image,
                        rho=6,
                        theta=np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25)

#plt.imshow(masked_image)
print(masked_image.shape)
image_with_lines=draw_lines(image,lines)
plt.imshow(image_with_lines)

plt.show()
