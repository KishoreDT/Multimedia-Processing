import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io

img = io.imread("2.png")
mask = cv.imread("mask2.png", 0)
res = cv.inpaint(img, mask, 1, cv.INPAINT_NS)
t=["Image with logo","Masked Image","Image without logo"]
im=[img,mask,res]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.title(t[i])
    plt.imshow(im[i],cmap="gray")
    plt.axis('off')
plt.show()