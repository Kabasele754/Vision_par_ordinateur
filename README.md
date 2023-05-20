# Face_Recognition_KNN 
Face Recognition using KNN algorithm and opencv in python.
This is a implementation of knn classifier.

## Dependencies
    Python 3.9 , OpenCv , Numpy

## Breakdown of the code for knn classifier
    1. Read a video stream using opencv
    2. Extract faces out of it and store as a numpy array in dataset
    3. Load the stored data as a Training data (data + label)
    4. Use the Knnto find the prediction of face
    5. Map the predicted ID to name of the user
    6. Finally, Display the prediction on the screen using bounding box and name of user

## How it works! :wink:  
* Run the "face_collect.py" , it will ask for users name,this will collect the face data of user until the user press key 'q' and save in dataset/data/[username].npy format.
* Now run the "face_recog.py", and it will show the detected face of user with bounding box and user's name.
