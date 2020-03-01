#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import math

#import my functions
from Newton_Model import newton_hit_the_ball

#################
ev3 = EV3Brick()
ev3.speaker.beep()
#################

# initialize motors and sensors
hitter = Motor(Port.D, Direction.COUNTERCLOCKWISE)
arm_start = hitter.angle()

eyes = UltrasonicSensor(Port.S1)
button = TouchSensor(Port.S4)

#------General functions------
def average_distance():
    avgd = 0
    n = 10

    for i in range(0,n):
        avgd += eyes.distance()/1000

    avgd = avgd/n
    return avgd

def reset_arm():
    #hitter.reset_angle(arm_start)
    hitter.run_target(1200,arm_start,Stop.COAST, False)

#------Newton Functions------ (see Newton_Model.py for subfunctions)
def run_Newton():
    while True:
        d = eyes.distance()/1000 #convert to m
        print("distance "+str(d)) 

        if button.pressed():

            avgd = average_distance()

            print("distance "+str(avgd))
            newton_hit_the_ball(hitter,avgd)
            #gets angry if you do not reset arm in a long time
            reset_arm() 

#------AI Training-----------
def run_AI_Training():
    while True:
        d = eyes.distance()/1000 #convert to m
        print("distance "+str(d)) 

        bttn_List = ev3.buttons.pressed()
        print(bttn_List)

        #press center button to begin calibrating new distance
        if len(bttn_List) != 0:
            if bttn_List[0] == Button.CENTER:

                avgd = average_distance() #distance we are trying to hit
                ang_speed = 500 #initial guess
                setSpeed = False #turns to true once we have found the right speed

                while(not setSpeed):
                    #try a hit
                    hitter.run_angle(int(ang_speed),360*2)
                    reset_arm()

                    #wait for feedback
                    bttn_List = ev3.buttons.pressed() 
                    while(len(bttn_List) == 0):
                        wait(1)
                    
                    #decide how good the guess was
                    selected = bttn_List[0]
                    if selected == Button.DOWN:
                        #too far
                        ang_speed = ang_speed - last_speed
                    elif selected == Button.UP:
                        #too close
                    elif selected == Button.CENTER:
                        #just right
                        setSpeed == True
                    

                print("distance "+str(avgd))
                



#------AI Post-Training------


#-----------MAIN-----------------

#run_Newton()
run_AI_Training()


        
        
        
