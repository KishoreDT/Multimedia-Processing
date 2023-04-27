import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
import skimage.color as cl
img=io.imread("img.png")
img_gr=cl.rgb2gray(img)
img_fft1=np.fft.fftshift(np.fft.fft2(img_gr))
img_fft2=np.fft.fftshift(np.fft.fft2(img_gr[0:100,0:100]))
t=["Orginal Image","Grayscaled Image","Magnituded Spectrum 1","Magnituded Spectrum 2"]
im=[img,img_gr,np.log(abs(img_fft1)),np.log(abs(img_fft2))]
for i in range(1):
    plt.subplot(2,2,i+1)
    plt.title(t[i])
    plt.imshow(im[i])
    plt.axis('off')
for i in range(1,4):
    plt.subplot(2,2,i+1)
    plt.title(t[i])
    plt.imshow(im[i],cmap="gray")
    plt.axis('off')
plt.show()