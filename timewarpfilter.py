import numpy as np
import os
from scipy import ndimage
import cv2

cap = cv2.VideoCapture(0)
downscale = .5
# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

ret, img = cap.read()
#wait for it to actually start working
while ret == 0:
    ret, img = cap.read()
img = cv2.resize(img, None, fx=downscale, fy=downscale, interpolation=cv2.INTER_AREA)
cv2.imshow('Input', img)

images = {}
step = 12
buffsize = int(img.shape[0]/step)
blocksize = int(img.shape[0]/buffsize) #yes, step and blocksize are the same val

for i in range(1,buffsize+1):
    images[i] = img


while True:
    ret, img = cap.read()
    img = cv2.resize(img, None, fx=downscale, fy=downscale, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', img)

    output = []

    for i in range(0,buffsize):
        current = images[i+1]
        block = current[1+i*blocksize:step+i*blocksize]
        if i == 0:
            output = block
        else:
            output = np.concatenate((output,block),axis=0)

        #cycle buffer
        if i != buffsize-1:
            images[i+1] = images[i+2]




    images[buffsize] = img
    #output = cv2.resize(output,None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input',output)


    c = cv2.waitKey(1)
    if c == 27:
        break


cap.release()
cv2.destroyAllWindows()
