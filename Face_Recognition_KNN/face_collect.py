import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier("dataset/haarcascade_frontalface_alt.xml")

skip=0
face_data = []
dataset_path = 'dataset/data/'
file_name=input("Enter the name of user: s")


while True:
    ret,frame = cap.read()
    
    if ret==False:
        continue
    
    
    faces = face_cascade.detectMultiScale(frame,1.3,5)
    faces = sorted(faces,key=lambda f:f[2]*f[3])
    
    for face in faces[-1:]:
        x,y,w,h = face
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        #crop_face
        if ret:
            offset=10
            face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
            face_section = cv.resize(face_section,(100,100),cv.INTER_AREA)
            
            skip+=1
            if(skip%10==0):
                face_data.append(face_section)
                print(len(face_data))       
        
    cv.imshow("Frame",frame)
    # cv2.imshow("crop_face",face_section)
        
    key_pressed = cv.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break

#face_data list to numpy array
face_data =np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

#save data
np.save(dataset_path+file_name+'.npy',face_data)
print("Data Successfully Saved At Location"+dataset_path+file_name+'.npy')
        
cap.release()
cv.destroyAllWindows()