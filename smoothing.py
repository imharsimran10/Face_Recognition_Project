from random import gauss
from statistics import median
import cv2 as cv
import numpy as np

img = cv.imread('abc.jpg')
cv.imshow('Image', img)

# Averaging.....
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3),0)
cv.imshow('Gaussian Blur', gaussian)

# Median Blur
median1 = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median1)

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)