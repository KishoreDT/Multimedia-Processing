import math
import cv2 as cv
import matplotlib as mp
import matplotlib.image as img
import numpy as np
import sys
import skimage #install scikit-image package
from matplotlib import pyplot as plt
from skimage import io
from skimage.io import imshow, imread
from skimage.transform import downscale_local_mean

img1 = imread('1.png') #,as_gray='False'
img2 = cv.imread('1.png',flags = cv.IMREAD_GRAYSCALE) #,as_gray='False'
print(img1.shape)
#print(img2)
io.imshow(img2)
io.show()
factors = 3**np.arange(1, 5)
figure, axis = plt.subplots(3,3)
ax = axis.ravel() # returns array
ax[0].imshow(img1,cmap='brg')
ax[0].set_title('$N1 = {} N2 = {} N3 = {} $'.format(img1.shape[0], img1.shape[1],img1.shape[2]))
#sampling an image
print(img1[0:60,20:23,1])
for i in range(6):
    i1 = i+1
    image = downscale_local_mean(img1, factors = (i1,i1,1),cval=0).astype(int)
    if i1==3:
        print(image[0:20,20,1])
    print(image.shape)
    ax[i1].imshow(image,cmap='brg')
    ax[i1].set_axis_off()
    ax[i1].set_title('$N1 = {} N2 = {} N3 = {} $'.format(image.shape[0], image.shape[1],image.shape[2]))
    #ax[1].imshow(image,cmap='brg')
    #ax[1].set_title('$N1 = {} N2 = {} N3 = {} $'.format(image.shape[0], image.shape[1], image.shape[2]))
io.show()
#plotting histogram
#plt.hist(img2.ravel(), bins=256, range=(0, 256), fc='k', ec='k')
histogram, bin_edges = np.histogram(img2, bins=256, range=(0, 256))
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 255])  # <- named arguments do not work here

plt.plot(bin_edges[0:256], histogram)  # <- or here
plt.show()

equ = cv.equalizeHist(img2)

# stacking images side-by-side
res = np.hstack((img2, equ))

# show image input vs output
cv.imshow('Equalization',res)

fig1, ax1 = plt.subplots(1,2)
ax2 = ax1.ravel() # returns arra

histogram, bin_edges = np.histogram(img2, bins=256, range=(0, 256))
hist1, bined1 = np.histogram(equ, bins=256, range=(0, 256))

ax2[0].set_title('Grayscale Histogram')
ax2[0].set_xlabel('grayscale value')
ax2[0].set_ylabel('pixels')
ax2[0].set_xlim([0, 255])  # <- named arguments do not work here

ax2[0].plot(bin_edges[0:256], histogram)  # <- or here

ax2[1].set_title('Equalized Histogram')
ax2[1].set_xlabel('grayscale value')
ax2[1].set_ylabel('pixels')
ax2[1].set_xlim([0, 255])  # <- named arguments do not work here

ax2[1].plot(bined1[0:256], hist1)  # <- or here


plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

