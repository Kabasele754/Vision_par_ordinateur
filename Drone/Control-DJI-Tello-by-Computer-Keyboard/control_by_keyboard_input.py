import easytello as tello
import keyboard

drone = tello.Tello()

while True:

    input = keyboard.read_key()

    if input == 'enter':
        drone.takeoff()

    elif input == 'w':
        drone.forward(50)

    elif input == 's':
        drone.back(50)

    elif input == 'd':
        drone.cw(90)

    elif input == 'a':
        drone.ccw(90)

    elif input == 'space':
        drone.land()
        
    elif input == 'up':
        drone.up(40)

    elif input == 'down':
        drone.down(40)

    elif input == 'right':
        drone.right(40)

    elif input == 'left':
        drone.left(40)

    else:
        pass

