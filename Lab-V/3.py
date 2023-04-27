import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img=cv.imread("3.png")
print("Shape of image :",img.shape)
img1=cv.medianBlur(img,7)
t=["Orginal Image","Medium Blur"]
im=[img,img1]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.title(t[i])
    plt.imshow(im[i])
    plt.axis('off')
plt.show()
