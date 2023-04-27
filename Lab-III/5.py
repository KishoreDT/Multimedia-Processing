import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
img = cv.imread("1.png",)
histo,bin=np.histogram(img,bins=256,range=(0,256))
plt.title("Histrogram")
plt.plot(bin[0:256],histo)
plt.show()