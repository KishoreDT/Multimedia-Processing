import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('1.png',0)
ret,th1 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
blur = cv.GaussianBlur(img,(5,5),0)
ret,th2 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
images = [img, 0, th1,
          blur, 0, th2]
titles = ['Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(2):
    plt.subplot(2,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.axis('off')
    plt.subplot(2,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.axis('off')
    plt.subplot(2,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.axis('off')
plt.show()
