import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
import skimage.color as cl
img=io.imread("img.png")
img_gr=cl.rgb2gray(img)
img_fft=np.fft.fftshift(np.fft.fft2(img_gr))
img_recons=abs(np.fft.ifft2(img_fft))
t=["Orginal Image","Grayscaled Image","Magnituded Spectrum","Reconstructed Image"]
im=[img,img_gr,np.log(abs(img_fft)),img_recons]
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