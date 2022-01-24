import cv2 as cv

img = cv.imread('abc.jpg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#  Simple Thresholding
#  The method returns two outputs. The first is the threshold that was used and the second output is the thresholded image.
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
# Here, the algorithm determines the threshold for a pixel based on a small region around it. So we get different thresholds for different regions of the same image which gives better results for images with varying illumination.
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)