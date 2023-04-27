import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
from skimage.filters import unsharp_mask as um
img=cv.imread("I2.png",0)
m,n=img.shape
k1=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
img_s1=cv.filter2D(src=img, ddepth=-1, kernel=k1)
k2=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
img_s2=cv.filter2D(src=img, ddepth=-1, kernel=k2)
r1=um(img, radius=5, amount=1)
r2=um(img, radius=10, amount=1)
t=["Orginal Image","Sharpenned Image with k1","Sharpenned Image with k2","Unsharp Mask radius=5","Unsharp Mask radius=10"]
im=[img,img_s1,img_s2,r1,r2]
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.title(t[i])
    plt.imshow(im[i],cmap="gray")
    plt.axis('off')
plt.show()
