import cv2 as cv
import numpy as np
import os

#------------------- KNN ----------------------#
def distance(v1,v2):
    #-----------------Eucledian distance
    return np.sqrt(((v1-v2)**2).sum())

def knn(train,test,k=5):
    dist=[]

    for i in range(train.shape[0]):
        #get the vector and label
        ix = train[i, :-1]
        iy = train[i, -1]

        #compute distance from test point
        d = distance(test, ix)
        dist.append([d,iy])
    #sort based on distance and get top k
    dk = sorted(dist,key=lambda x:x[0])[:k]
    #retrives only the label
    labels = np.array(dk)[:,-1]

    #get frequency of each label
    output = np.unique(labels,return_counts=True)
    #Find max frequency and corresponding label
    index = np.argmax(output[1])
    return output[0][index]
#----------------------------------------------------#
    
cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier("dataset/haarcascade_frontalface_alt.xml")

skip=0
face_data = []
labels = []
dataset_path = './dataset/data/'

class_id = 0 #labels for given files
names = {} #Mapping btw id and name

for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        names[class_id]=fx[:-4]
        
        data_item = np.load(dataset_path+fx)
        face_data.append(data_item)
        
        #create label for the class 
        target  = class_id*np.ones((data_item.shape[0],))
        class_id +=1
        labels.append(target)
        
face_dataset = np.concatenate(face_data,axis=0)
face_labels = np.concatenate(labels,axis=0).reshape((-1,1))
print("face_dataset",face_dataset.shape)
print("face_labels",face_labels.shape)

trainset = np.concatenate((face_dataset,face_labels),axis=1)
#print(trainset.shape)

#Testing-----------------------------------
while True:
    ret,frame = cap.read()
    if ret==False:
        continue
    
    faces =face_cascade.detectMultiScale(frame,1.3,5)
    
    for face in faces:
        x,y,w,h = face
        
        if ret:
            offset = 10
            face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
            face_section = cv.resize(face_section,(100,100),cv.INTER_AREA)
            
            #prediction
            output = knn(trainset,face_section.flatten())
            
            #Display name  and rectangle
            pred_name = names[int(output)]
            cv.putText(frame,pred_name,(x,y-10),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv.LINE_AA)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
    
    cv.imshow("Faces",frame)
    key = cv.waitKey(1) & 0xFF
    if key ==ord('q'):
        break

cap.release()
cv.destroyAllWindows()