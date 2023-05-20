# pip install opencv-python
import cv2

haarCascade = 'dateset/haarcascade_frontalface_alt.xml'
print(haarCascade)
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    classifier = cv2.CascadeClassifier(haarCascade)
    faces = classifier.detectMultiScale(grayFrame)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)

    cv2.imshow('Video', frame)
    k= cv2.waitKey(1)
    if k== ord("q"):
        break
cap.release()
cv2.destroyAllWindows()