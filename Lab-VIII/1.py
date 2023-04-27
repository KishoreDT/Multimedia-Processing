import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io

no=4

ft='.png'
name=[]
for i in range(no):
    n=str(i+1)
    name.append(n+ft)
print(name)

for j in range(no):
    image1 = io.imread(name[j])
    img = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
    
    ret, thresh1 = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
    ret, thresh2 = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV)
    ret, thresh3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)
    ret, thresh4 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)
    ret, thresh5 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)

    t=["Orginal Image","Binary Threshold","Binary Threshold Inverted","Truncated Threshold","Set to 0","Set to 0 Inverted"]
    im=[img,thresh1,thresh2,thresh3,thresh4,thresh5]
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.title(t[i])
        plt.imshow(im[i],cmap="gray")
        plt.axis('off')
    plt.show()
