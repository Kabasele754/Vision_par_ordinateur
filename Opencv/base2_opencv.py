import cv2 as cv 
cap = cv.VideoCapture(0)
haarCascade="dataset/haarcascade_frontalface_alt.xml"
while True:
    ret,frame= cap.read()
    grayFrame=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    classifier= cv.CascadeClassifier(haarCascade)
    faces= classifier.detectMultiScale(grayFrame)
    for x,y,w,h in faces :
        cv.rectangle(frame,(x,y),(x+w,y+h), color =(0,255,0),thickness=3)
    cv.imshow("cap", frame)
    k=cv.waitKey(1)
    if k==ord("q"):
        break
cap.release()
cv.destroyAllWindows()
