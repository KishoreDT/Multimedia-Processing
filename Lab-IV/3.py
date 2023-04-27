import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img = cv.imread("1.png",flags=2)
equ = cv.equalizeHist(img)
histo1,bin=np.histogram(img,bins=256,range=(0,256))
histo2,bin=np.histogram(equ,bins=256,range=(0,256))
t=["Orginal Image","Equalized Image","Orginal Image [Histogram]","Equalized Image [Histogram]"]
im=[img,equ,histo1,histo2]
c=4
for i in range(2):
    plt.subplot(2,2,i+1)
    plt.title(t[i])
    plt.imshow(im[i],cmap='gray')
    plt.axis('off')
for i in range(2,3):
    plt.subplot(2,2,i+1)
    plt.title(t[i])
    plt.plot(bin[0:256],histo1)
for i in range(3,4):
    plt.subplot(2,2,i+1)
    plt.title(t[i])
    plt.plot(bin[0:256],histo2)
plt.show()