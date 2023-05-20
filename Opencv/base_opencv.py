import cv2 as cv
img=cv.imread ("Ressource/1.jpg")
cv.imshow("1",img)

#changer couleur
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("1",gray)
#blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("1 Blur",blur)
cv.waitKey(0)
