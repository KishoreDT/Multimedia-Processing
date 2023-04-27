import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
def square_image(x, y):
    X, Y = np.meshgrid(x, y)
    return X**2 + Y**2
factors = 2**np.arange(1, 5)
squ_image = square_image(np.linspace(0, 1, num=5), np.linspace(0, 1, num=5))
print(squ_image)
print(factors)
fig, ax = plt.subplots(1, len(factors)+1, figsize=(15, 4))
ax[0].imshow(squ_image)
ax[0].set_title("Orginal Image")
for i, k in enumerate(factors):
    i=i+1
    bins = np.linspace(0, squ_image.max(), k)
    if i==2:
        print(bins)
    image = np.digitize(squ_image, bins)
    if i==2:
        print(image)
    image = np.vectorize(bins.tolist().__getitem__)(image-1)
    if i==2:
        print(image)
    ax[i].imshow(image)
    ax[i].set_title('$k = {}$'.format(k))
plt.show()