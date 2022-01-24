import cv2 as cv
import numpy as np

# img = cv.imread('abc.jpg')
# cv.imshow('Image',img)

# drawing a Blank Image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#  1. Paint the image a certain colour
# blank[:] = 0,0,255          #B,G,R
# cv.imshow('Red',blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle',blank)

# 3. Drawing a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle',blank)

# 4. Drawing a Line
cv.line(blank, (100,100), (300,400), (255,255,255), thickness=3)
cv.imshow('Line',blank)

# 5. Write text on an Image
cv.putText(blank, 'Harsimran', (300,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text',blank)

cv.waitKey(0) 