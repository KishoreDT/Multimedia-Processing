import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img=cv.imread("1.png",0)
print("Shape of image :",img.shape)
m,n=img.shape
mask=np.ones([3,3],dtype=int)
mask=mask/9
newimg=np.zeros([m,n])
for i in range(1,m-1):
    for j in range(1,n-1):
        temp=img[i-1,j-1]*mask[0,0]+img[i-1,j]*mask[0,1]+img[i-1,j+1]*mask[0,2]+img[i,j-1]*mask[1,0]+img[i,j]*mask[1,1]+img[i,j+1]*mask[1,2]+img[i+1,j-1]*mask[2,0]+img[i+1,j]*mask[2,1]+img[i+1,j+1]*mask[2,2]
        newimg[i,j]=temp
t=["Orginal Image","Blur Image"]
im=[img,newimg]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.title(t[i])
    plt.imshow(im[i],cmap='gray')
    plt.axis('off')
plt.show()
