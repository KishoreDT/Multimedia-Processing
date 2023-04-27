import math
import cv2 as cv
import matplotlib as mp
import matplotlib.image as img
import numpy as np
import sys
from matplotlib import pyplot as plt
#r =int(input("Enter the radius: "))
#perimeter=2*math.pi*r
#print(perimeter)
print("My version of opencv is: " + cv.__version__)
img1 = cv.imread('1.png')
img2 = cv.imread('1.png',flags = cv.IMREAD_GRAYSCALE)
im3 = img.imread('1.png')
cv.imshow('newimg',img1)
if img1 is None:
    print('Could not read the image')
print(f'Shape of image 1: {img1.shape}')
print(f'Shape of image 2: {img2.shape}')
print(img1[1,2,0])

n1 = 200 * np.ones(50)
n3 = 0 * np.ones(167)
print(img1[0:100,51,2])

for i in range(120,140):
    img1[100:150,i,2] = n1
    img2[100:150,i] = n1

print(img1[0:100,51,2])
#img1[0:167,51,1] = n1
#img1[0:167,52,1] = n1
#img1[0:167,53,1] = n1
cv.imshow('newimg',img1)
cv.waitKey(0)
cv.imshow('newimg1',img2)
cv.waitKey(0)
h1 = 50
w1 = 50
y1 = 40
x1 = 100
crop_img = img1[y1:y1+h1, x1:x1+w1]

rsimg = cv.resize(img2, (60, 50),interpolation= cv.INTER_LINEAR)
print(f'Shape of resized image: {rsimg.shape}')
print(img2[0:100,0])
print(rsimg[0:50,0])

rshapeimg = img2.reshape(299,168)

plt.subplot(4, 2, 1), plt.imshow(cv.cvtColor(img1,cv.COLOR_BGR2RGB)),plt.axis('off')
plt.subplot(4, 2, 2), plt.imshow(img2,cmap='gray'),plt.axis('off') #hsv
plt.subplot(4, 2, 3), plt.imshow(cv.cvtColor(crop_img,cv.COLOR_BGR2RGB)),plt.axis('off') #hsv
plt.subplot(4, 2, 4), plt.imshow(rsimg,cmap='gray'),plt.axis('off') #hsv
plt.subplot(4, 2, 5), plt.imshow(rshapeimg,cmap='bgr'),plt.axis('off') #hsv
plt.show()
cv.waitKey(0)
cv.imshow('Image display',img1)
keypress = cv.waitKey(0)

#if keypress == ord("y"): # ord() returns unicode for a given character
#    cv.imwrite('appl_newimg.jpg',img1)