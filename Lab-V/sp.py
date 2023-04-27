import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img=cv.imread("1.png",0)
i=cv.imread("2.png",0)
print("Shape of image :",img.shape)
img1=cv.medianBlur(i,7)
img2=cv.blur(img,[7,7],borderType=cv.BORDER_CONSTANT)
kernel=np.ones((5,5),np.float32)/25
img3=cv.filter2D(img,-1,kernel)
img4=cv.GaussianBlur(img,(7,7),0.5)
img5=cv.bilateralFilter(img,9,50,10)
cv.imshow("Image",img1)
