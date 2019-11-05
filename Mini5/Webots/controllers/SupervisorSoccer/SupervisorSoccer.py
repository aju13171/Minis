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

""" JUGADOR """
r = 0.0205
l = 0.0355
a = 0.0355
rP = 0.1
MAX_SPEED = 6.28
player = supervisor.getFromDef("Player")
posP = player.getField("translation")
orP = player.getField("rotation")


## Posiciones iniciales aleatorias ##
sizeX = sizeVec[0] - 2*rP
sizeY = sizeVec[1] - 2*rP

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


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while supervisor.step(TIME_STEP) != -1:
    
    # Posiciones actuales
    posAP = posP.getSFVec3f()
    posAB = posB.getSFVec3f()
    vecDist = [0,0]
    vecDist[0] = posAB[0] - posAP[0]
    vecDist[1] = posAB[2] - posAP[2]
    
    dist = math.sqrt(vecDist[0]**2 + vecDist[1]**2)
    
    
    # Orientación actual
    orAP = orP.getSFRotation()
    vecP = [0,0]
    vecP[0] = math.sin(orAP[3])
    vecP[1] = math.cos(orAP[3])
    
    ang = math.acos((vecDist[0]*vecP[0] + vecDist[1]*vecP[1])/((math.sqrt((vecDist[0])**2+(vecDist[1])**2))*(math.sqrt((vecP[0])**2+(vecP[1])**2))))
    
    v = 0.5*dist
    w = 0.5*ang
    
    phi_r = (v+(w*l))/r
    phi_l = (v-(w*l))/r
    
    leftMotor.setVelocity(phi_l)
    rightMotor.setVelocity(phi_r)
    
    pass

# Enter here exit cleanup code.
