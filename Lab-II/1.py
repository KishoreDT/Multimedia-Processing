import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from skimage.transform import downscale_local_mean as dlm
import skimage.io as io
img = io.imread("1.png")
print("Shape :",img.shape)
factors = 3**np.arange(1, 5)
figure, axis = plt.subplots(3,3)
ax=axis.ravel()
ax[0].imshow(img,cmap='brg')
ax[0].axis('off')
ax[0].set_title('Orginal Image \n $N1={}, N2={}, N3={}$'.format(img.shape[0],img.shape[1],img.shape[2]))
print(img[0:60,20:23,1])
for i in range(8):
    i1=i+1
    image = dlm(img,factors=(i1,i1,1),cval=0).astype(int)
    if i1==3:
        print(image[0:20,20,1])
    ax[i1].imshow(image,cmap='brg')
    ax[i1].axis('off')
    ax[i1].set_title('$N1={}, N2={}, N3={}$'.format(image.shape[0],image.shape[1],image.shape[2]))
plt.show()