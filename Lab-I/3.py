import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img = io.imread("1.png")
x=int(input("Enter a number for x-axis :"))
y=int(input("Enter a number for y-axis :"))
#h=int(input("Enter a height :"))
#l=int(input("Enter a length :"))
rs = cv.resize(img,(x,y))
t=["Orginal Image","Resized Image"]
im=[img,rs]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.title(t[i])
    plt.imshow(im[i])
    plt.axis('off')
plt.show()