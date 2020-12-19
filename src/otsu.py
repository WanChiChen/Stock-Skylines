from PIL import Image, ImageOps
from scipy.signal import convolve
from scipy import ndimage
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# return histogram of pixel values of input img
def histogram(img):
    values = np.zeros(256)
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            values[img[i,j]] += 1
    return values

# calculate optimal threshold level from histogram
def otsu(histogram):
    wB = 0
    sumB = 0
    maxVal = 0.0
    total = np.sum(histogram)
    sum1 = np.dot(np.arange(256), histogram) 
    for i in range(1, 256):
        wF = total - wB
        if wB > 0 and wF > 0:
            mF = (sum1-sumB) / wF
            val = wB * wF * ((sumB / wB)-mF)**2
            if val >= maxVal:
                level = i
                maxVal = val

        wB += histogram[i]
        sumB += i * histogram[i]
    return level

# apply a threshold to an image
# pixels > threshold are white
# pixels < threshold are black
def applyThreshold(threshold, img):
    img_val = img.shape
    rows, cols = img.shape
    new = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if img[i,j] >= threshold:
                new[i,j] = 255
            else:
                new[i,j] = 0
    return new
            
# Open Image
image = Image.open('../imgs/shanghai.jpg')
image = ImageOps.grayscale(image)
I = np.asarray(image)

fig=plt.figure()
fig.add_subplot(2, 3, 1)
plt.imshow(I, cmap='gray')
plt.xlabel("Original")

# Histogram
hist = histogram(I)

fig.add_subplot(2, 3, 2)
plt.bar(np.arange(0,256), hist, color='b', width=5, align='center', alpha=0.25)
plt.xlabel("Histogram")

# Threshold 1
threshold = 75
img = applyThreshold(threshold, I)
fig.add_subplot(2, 3, 3)
plt.imshow(img, cmap='gray')
plt.xlabel("Threshold = " + str(threshold))

# Threshold 2
threshold = 100
img = applyThreshold(threshold, I)
fig.add_subplot(2, 3, 4)
plt.imshow(img, cmap='gray')
plt.xlabel("Threshold = " + str(threshold))

# Threshold 3
threshold = 110
img = applyThreshold(threshold, I)
fig.add_subplot(2, 3, 5)
plt.imshow(img, cmap='gray')
plt.xlabel("Threshold = " + str(threshold))

# Otsu
threshold = otsu(hist)
img = applyThreshold(threshold, I)

fig.add_subplot(2, 3, 6)
plt.imshow(img, cmap='gray')
plt.xlabel("Otsu = " + str(threshold))

plt.show()