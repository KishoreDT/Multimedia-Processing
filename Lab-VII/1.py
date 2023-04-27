import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io

img = io.imread("1.png")
mask = cv.imread("mask1.png", 0)
res = cv.inpaint(img, mask, 3, cv.INPAINT_TELEA)
t=["Damaged Image","Masked Image","Restored Image"]
im=[img,mask,res]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.title(t[i])
    plt.imshow(im[i],cmap="gray")
    plt.axis('off')
plt.show()