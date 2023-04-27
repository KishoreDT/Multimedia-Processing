import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img=cv.imread("2.png",0)
m,n=img.shape
k1=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
img_s1=cv.filter2D(src=img, ddepth=-1, kernel=k1)
k2=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
img_s2=cv.filter2D(src=img, ddepth=-1, kernel=k2)
t=["Orginal Image","Sharpened Image with k1","Sharpened Image with k2"]
im=[img,img_s1,img_s2]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.title(t[i])
    plt.imshow(im[i],cmap="gray")
    plt.axis('off')
plt.show()
