import cv2 as cv

#  Reading Images
# img =cv.imread('abc.jpg')
# cv.imshow('HS',img)

# Reading Videos
capture = cv.VideoCapture('video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
 
