from djitellopy import Tello
import KeyPressModule as kp
from time import sleep, time

kp.init()
tello = Tello()
tello.connect()
print(tello.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr= -speed
    elif kp.getKey("RIGHT"): lr= speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): yv = tello.land()
    if kp.getKey("e"): yv = tello.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'C:\Users\User\Desktop\Aplikacje\Studia\GReG\tello\images\{time.time()},pg')

    return [lr, fb, ud, yv]


tello.takeoff()

while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

