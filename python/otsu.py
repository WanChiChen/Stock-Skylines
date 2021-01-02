from PIL import Image, ImageOps
from scipy.signal import convolve
from scipy import ndimage
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 as cv

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
            
def run(src):

    # Open Image
    image = Image.open(f"../imgs/{src}")
    image = ImageOps.grayscale(image)
    I = np.asarray(image)

    # Histogram
    
    hist = histogram(I)

    # Otsu
    threshold = otsu(hist)
    img = applyThreshold(threshold, I)

    # blur image
    #img = cv.blur(img,(5,5), 1)
    img = Image.fromarray(img)
    img.convert("L").save(f"../segmented/{src}")