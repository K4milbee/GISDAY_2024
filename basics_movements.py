from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()

print(tello.get_battery())

tello.takeoff()

#       tello.send_rc_control(0,0,0,0) zakres: od -100 do 100
# left_right_velocity
# forward_backward_vel
# up_down_vel
# yaw_velovity
#       sleep(2) in seconds
sleep(2)
tello.send_rc_control(0,0,0,0)
sleep(2)
tello.send_rc_control(0,0,0,0)
sleep(2)

sleep(6)
tello.send_rc_control(0,0,0,0) #it will land like helicopter
tello.land()
# '''
