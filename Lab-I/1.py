import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img = io.imread("1.png")
org = io.imread("1.png")
print(f"Shape of Image is : {img.shape}")
n=100*np.ones(150)
print(img[0:100,56,0])
for i in range(45,65):
    img[0:150,i,1]=n
print(img[0:100,46,1])
t=["Orginal Image","Changed Image"]
im=[org,img]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.title(t[i])
    plt.imshow(im[i])
    plt.axis('off')
plt.show()