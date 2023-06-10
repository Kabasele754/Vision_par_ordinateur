import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

cv2.imwrite("picture.png", frame_read.frame)

tello.land()