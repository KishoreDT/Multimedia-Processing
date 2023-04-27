import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img1 = io.imread("A1.png")
img2 = io.imread("A2.png")
img3 = io.imread("A3.png")
img4 = io.imread("A4.png")
t=["Basket Ball","Foot Ball","Volly Ball","Hand Ball"]
im=[img1,img2,img3,img4]
c=4
for i in range(c):
    plt.subplot(2,2,i+1)
    plt.title(t[i])
    plt.imshow(im[i])
    plt.axis('off')
plt.show()