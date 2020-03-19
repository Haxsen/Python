import cv2 as cv
import numpy as np
img = cv.imread("imageo.png",0)
size=np.shape(img)

#task 1
cv.imwrite("task1-1.png",img)

# flip half top
fimg = cv.flip(img[size[0]//2:size[0],0:size[1]],0)
cimg=img.copy()
cimg[0:size[0]//2,0:size[1]] = fimg

cv.imwrite("task1-2.png",cimg)

#task 2
perc10 = int(size[1]/10)             #10% of x
totalx = size[1]+perc10+perc10       #total x width
ydiv = totalx/size[0]                #y*?=x , ?=x/y
totaly = int(size[0] * (ydiv))       #y*?=x
percy = int((totaly-size[0])/2)

Y_DIMENSION = totaly
X_DIMENSION = totalx
bimg = np.zeros((Y_DIMENSION, X_DIMENSION))

bimg[percy:(size[0]+percy) , perc10:(size[1]+perc10)] = img[0:size[0] , 0:size[1]]

cv.imwrite("task2.png",bimg)

#task3
bimg2 = np.zeros((100, 100), dtype=np.uint8)
f = int(input("Frequency? "))

for i in range(100):
    for j in range(100):
        bimg2[i][j] = (np.sin(2*3.14*f*(i+j))+1)*127

cv.imwrite("task3.png",bimg2)
