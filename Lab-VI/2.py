import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
from skimage.filters import unsharp_mask as um
img=cv.imread("2.png",0)
r1=um(img, radius=5, amount=1)
r2=um(img, radius=10, amount=1)
t=["Orginal Image","Unsharp Mask radius=5","Unsharp Mask radius=10"]
im=[img,r1,r2]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.title(t[i])
    plt.imshow(im[i],cmap="gray")
    plt.axis('off')
plt.show()