import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img = io.imread("1.png")
print(f"Shape of Image is : {img.shape}")
cp = img[80:280, 150:330]
t=["Orginal Image","Croped Image"]
im=[img,cp]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.title(t[i])
    plt.imshow(im[i])
    plt.axis('off')
plt.show()