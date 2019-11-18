"""SupervisorSoccer controller."""

from controller import Supervisor
import numpy as np
import random
import math
import pickle


TIME_STEP = 64
# create the Robot instance.
supervisor = Supervisor()
supervisor.step(TIME_STEP)

""" ARENA """
arena = supervisor.getFromDef("Arena")
size = arena.getField("floorSize")
sizeVec = size.getSFVec2f()

""" PELOTA """
rB = 0.05
ball = supervisor.getFromDef("Ball")
posB = ball.getField("translation")

""" PORTERÍA """
port = supervisor.getFromDef("Porteria")
posPo = port.getField("translation")

""" JUGADOR """
r = 0.0205
l = 0.0355
a = 0.0355
rP = 0.1
MAX_SPEED = 6.28
player = supervisor.getFromDef("Player")
posP = player.getField("translation")
orP = player.getField("rotation")
# get a handler to the motors and set target position to infinity (speed control)
leftMotor = supervisor.getMotor('left wheel motor')
rightMotor = supervisor.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0)
rightMotor.setVelocity(0)


## Posiciones iniciales aleatorias ##
sizeX = sizeVec[0] - 2*rP - 0.5
sizeY = sizeVec[1] - 2*rP - 0.5

# Pelota
xB = random.random()*sizeX - sizeX/2
yB = random.random()*sizeY - sizeY/2
posB.setSFVec3f([xB, 0.05, yB])

# Jugador
xP = random.random()*sizeX - sizeX/2
yP = random.random()*sizeY - sizeY/2
oP = random.random()*2*math.pi
posP.setSFVec3f([xP, -6.40422e-05, yP])
vecOrP = orP.getSFRotation()
orP.setSFRotation([vecOrP[0], vecOrP[1], vecOrP[2], oP])

i = 0
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while supervisor.step(TIME_STEP) != -1:
    
    # Posiciones actuales
    posAP = posP.getSFVec3f()
    posAB = posB.getSFVec3f()
    posAPo = posPo.getSFVec3f()
    vecDist = [0,0]
    vecDist[0] = posAB[0] - posAP[0]
    vecDist[1] = posAB[2] - posAP[2]
    vecDist2 = [0,0]
    vecDist2[0] = posAPo[0] - posAP[0]
    vecDist2[1] = posAPo[2] - posAP[2]
    
    dist = math.sqrt(vecDist[0]**2 + vecDist[1]**2)
    dist2 = math.sqrt(vecDist2[0]**2 + vecDist2[1]**2)
    uVecDist2 = [0,0]
    uVecDist2[0] = vecDist2[0]/dist2
    uVecDist2[1] = vecDist2[1]/dist2
    print("dist")
    print(dist)
    
    
    # Orientación actual
    orAP = orP.getSFRotation()
    vecP = [0,0]
    vecP[0] = math.sin(orAP[3])
    vecP[1] = math.cos(orAP[3])
    
    ang = -math.pi + math.acos((vecDist[0]*vecP[0] + vecDist[1]*vecP[1])/((math.sqrt((vecDist[0])**2+(vecDist[1])**2))*(math.sqrt((vecP[0])**2+(vecP[1])**2))))
    ang2 = -math.pi + math.acos((vecDist2[0]*vecP[0] + vecDist2[1]*vecP[1])/((math.sqrt((vecDist2[0])**2+(vecDist2[1])**2))*(math.sqrt((vecP[0])**2+(vecP[1])**2))))
    
    print("ang", ang*180/math.pi)
    print("ang2", ang2*180/math.pi)
    
    v = 0.04*dist
    w = 0.04*ang
    
    phi_r = (v+(w*l))/r
    phi_l = (v-(w*l))/r
    # print("phi_r", phi_r)
    # print("phi_l", phi_l)
    
    # Truncar velocidades a la velocidad maxima
    # if(phi_r > 0):
        # if(phi_r > MAX_SPEED):
            # phi_r = MAX_SPEED
    # else:
        # if(phi_r < -MAX_SPEED):
            # phi_r = -MAX_SPEED
            
    # if(phi_l > 0):
        # if(phi_l > MAX_SPEED):
            # phi_l = MAX_SPEED
    # else:
        # if(phi_l < -MAX_SPEED):
            # phi_l = -MAX_SPEED

    if(dist > 0.12 and i == 0): 
        posB.setSFVec3f([xB, 0.05, yB])
        print("Distancia mayor a 0.12")           
        leftMotor.setVelocity(phi_l)
        rightMotor.setVelocity(phi_r)
        
    else:
        print("Distancia menor a 0.12") 
        if(i == 0):
            print("-----------------")
            print("CAMBIO DE ANGULO")
            print("-----------------")
            leftMotor.setVelocity(0)
            rightMotor.setVelocity(0) 
            # alinear E-Puck con porteria
            if(posAP[2]<0):
                orP.setSFRotation([orAP[0],orAP[1],orAP[2],orAP[3]+ang2])
                # posicionamiento de la pelota
                posB.setSFVec3f([0.12*uVecDist2[0] + posAP[0], 0.05, 0.12*uVecDist2[0] + posAP[2]])
            else:
                orP.setSFRotation([orAP[0],orAP[1],orAP[2],orAP[3]-ang2])
                # posicionamiento de la pelota
                posB.setSFVec3f([0.12*uVecDist2[0] + posAP[0], 0.05, -0.12*uVecDist2[0] + posAP[2]])
        elif(i<6):
            leftMotor.setVelocity(6)
            rightMotor.setVelocity(6)
            leftMotor.setPosition(3)
            rightMotor.setPosition(3)
        elif(i == 6):
            leftMotor.setVelocity(0)
            rightMotor.setVelocity(0)  
        # elif(i<10):
            # leftMotor.setVelocity(6)
            # rightMotor.setVelocity(6)
            # leftMotor.setPosition(1)
            # rightMotor.setPosition(1)
        # else:
            # leftMotor.setVelocity(0)
            # rightMotor.setVelocity(0) 
            
        i += 1
                        
        
    
    pass

# Enter here exit cleanup code.
