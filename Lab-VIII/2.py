import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('1.png',0)
img = cv.medianBlur(img,5)
ret,th = cv.threshold(img,127,255,cv.THRESH_BINARY)
titles = ['Original Image', 'Global Thresholding (v = 127)',]
images = [img, th]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()