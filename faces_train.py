import os
import cv2 as cv
import numpy as np

people = ['Harsimran', 'Kunal', 'Nimrat', 'Noor_Chahal', 'Rishit']
DIR = r'C:\Users\Aman\Desktop\OpenCv\Faces_Train' 

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# features -> image array of faces 
# labels -> corresponding label(name) of images in feature array
features = []
labels = []

def create_train():
    for person in people:       #Now, here we are inside every index's folder e.g. inside Harsimran
        path = os.path.join(DIR, person)
        label = people.index(person)

        #Now, we will iterate over every image in Harsimran's Folder
        for img in os.listdir(path):
            img_path = os.path.join(path,img)    #Here, we grab the path of every image inside Harsimran's Folder

            # Reading the images from above path
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

            # now, we will iterate over faces detected and stored in faces_rect list
            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h , x:x+w]      #roi-> region of interest i.e. we have cropped out only the detected part of the image.
                # Now, we will append the roi in the features list declared above and
                # their correspomding labels in labels list
                features.append(faces_roi)
                labels.append(label)


create_train()
print('Training done.........................')


features = np.array(features , dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

np.save('features.npy', features)
np.save('labels.npy', labels)

# Now we also need to save our trained recognizer so that we can use it outside in any other file or directory without having the need of writing the long code again.
# This can be achieved by making a yml file of model and save it
face_recognizer.save('face_trained.yml')