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
#arena = supervisor.getFromDef("Arena")
#size = arena.getField("floorSize")
#sizeVec = size.getSFVec2f()

""" PELOTA """
rB = 0.05
ball = supervisor.getFromDef("Ball")
posB = ball.getField("translation")

""" JUGADOR """
rP = 0.1
MAX_SPEED = 6.28
player = supervisor.getFromDef("Player")
posP = player.getField("translation")


## Posiciones iniciales aleatorias ##
sizeX = sizeVec[0] - 2*rP
sizeY = sizeVec[1] - 2*rP

# Pelota
xB = random.random()*sizeX - sizeX/2
yB = random.random()*sizeY - sizeY/2
ball.setSFVec3f([xB, 0.05, yB])
print(ball.getSFVec3f(posB))

# Jugador
xP = random.random()*sizeX - sizeX/2
yP = random.random()*sizeY - sizeY/2
player.setSFVec3f([xP, -6.40422e-05, yP])




# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    pass

# Enter here exit cleanup code.
