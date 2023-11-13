from picarx import Picarx
from robot_hat import TTS
import time

t = 0.2     # time delay for servos
l = 5       # distance set for alarm "too close!"
words = ["stop", "turn left", "move forward", "turn right"]

def detect():
    obs = False
    dist = round(pc.ultrasonic.read(), 2)
    print("distance: ",dist)
    if dist < l:
        se.say(words[0])  
        print("stop!")
        obs = True
    time.sleep(t)  
    return obs
    
def track():
    vlist = pc.get_grayscale_data()
    minv = vlist.index(min(vlist))
    if minv == 0:
        se.say(words[1])
        print(words[1])
    elif minv == 1:
        se.say(words[2])
        print(words[2])
    elif minv == 2:
        se.say(words[3])
        print(words[3])
    time.sleep(t)

def throttle(s):
    if s >= 0:
        pc.forward(s)
    else:
        pc.backward(-s)
    time.sleep(t)
        
def rudder(r):
    d = 8
    pc.set_dir_servo_angle(d + r)
    time.sleep(t)
    
def aileron(r):
    d = 11
    r = d + r
    pc.set_cam_pan_angle(r)
    time.sleep(t)

def elevator(r):
    d = 0
    r = d + r
    pc.set_camera_tilt_angle(r)
    time.sleep(t)
        
def init():
    global pc
    global se 
    pc = Picarx()
    se = TTS()
    time.sleep(t)
    throttle(0)
    rudder(0)
    aileron(0)
    elevator(0)

def stop(): 
    throttle(0)
    rudder(0)
    aileron(0)
    elevator(0)
    pc.stop()
    time.sleep(t)
