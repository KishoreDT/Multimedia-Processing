import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import skimage.io as io
def square_image(x, y):
    X, Y = np.meshgrid(x, y)
    return X**2 + Y**2
factors = 2**np.arange(1, 5)
img = io.imread("1.png")
print(img.shape)
print(factors)
fig, ax = plt.subplots(1, len(factors)+1, figsize=(15, 4))
ax[0].imshow(img)
ax[0].set_title("Orginal Image")
for i, k in enumerate(factors):
    i=i+1
    bins = np.linspace(0, img.max(), k)
    if i==2:
        print(bins)
    image = np.digitize(img, bins)
    if i==2:
        print(image)
    image = np.vectorize(bins.tolist().__getitem__)(image-1)
    if i==2:
        print(image)
    ax[i].imshow(image)
    ax[i].axis('off')
    ax[i].set_title('$k = {}$'.format(k))
plt.show()