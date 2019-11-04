"""PlayerSoccer controller."""

"""pruebaMatrizDifeomorfismo controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import math
import numpy as np
import pickle

# get the time step of the current world.
# timestep = int(robot.getBasicTimeStep())
TIME_STEP = 64

MAX_SPEED = 6.28

# Dimensiones robot
r = 0.0205
l = 0.0355
a = 0.0355

# create the Robot instance.
robot = Robot()
argc = int(robot.getControllerArguments())

# Enable compass
compass = robot.getCompass("compass")
compass.enable(TIME_STEP)
robot.step(TIME_STEP)

# get a handler to the motors and set target position to infinity (speed control)
leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0)
rightMotor.setVelocity(0)

posAct = np.zeros([3])

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(TIME_STEP) != -1:
    # Posiciones actuales y finales según Supervisor
    # print("AGENTE",argc)
    leftMotor.setPosition(float('inf'))
    rightMotor.setPosition(float('inf'))
    
    posAnt = posAct
    
    with open('C:/Users/Andrea Maybell/Documents/AMPE/2019/Robotat/WeBots/PruebasBasicas1/controllers/Datos.pickle','rb') as f:
            posActuales = pickle.load(f)
    # with open('C:/Users/Andrea Maybell/Documents/AMPE/2019/Robotat/WeBots/PruebasBasicas1/controllers/Datos2.pickle','rb') as f:
            # posAnteriores = pickle.load(f)
    with open('C:/Users/Andrea Maybell/Documents/AMPE/2019/Robotat/WeBots/PruebasBasicas1/controllers/Datos3.pickle','rb') as f:
            V = pickle.load(f)
    
    # print("Velocidades", V)
    # Posición nueva/final
    # posAnt = np.asarray([posAnteriores[0][argc], -6.39203e-05, posAnteriores[1][argc]])
    # print("posAnt",posAnt)
    
    # Posición actual
    posAct = np.asarray([posActuales[0, argc], -6.39203e-05, posActuales[1, argc]])
    # print("posAct",posAct)
    
    # Velocidades
    
    # Orientación robot
    comVal = compass.getValues()
    angRad = math.atan2(comVal[0],comVal[2])
    angDeg = (angRad/math.pi)*180
    if(angDeg < 0):
        angDeg = angDeg + 360
    theta_o = angDeg
    # theta_o = 270 - angDeg
    # if(theta_o < 0):
        # theta_o = theta_o + 360
        
    # print("ang",angDeg)
    # print("theta",theta_o)
            
    e_x = posAnt[2] - posAct[2]
    # print("e_x", e_x)
    e_y = posAnt[0] - posAct[0] 
    # print("e_y", e_y)
    e_p = math.sqrt(e_x**2 + e_y**2)
    # print("e_p", e_p)
    k = 1
    # if(e_p < 0.0005 and argc != 0):
        # k = 0.1
    # else:
        # k = 1
    
    #K = 3.12*(1 - math.exp(-2*e_p))/e_p #constante de ponderación
    
    v = k*((V[0][argc])*(math.cos(theta_o*math.pi/180)) + (V[1][argc])*(math.sin(theta_o*math.pi/180)))
    w = k*((V[0][argc])*(-math.sin(theta_o*math.pi/180)/a) + (V[1][argc])*(math.cos(theta_o*math.pi/180)/a))
    
    # print("v1",v)
    # if(abs(v) < 0.05):
        # v = 0
        # w = 0
    # print("v2",v)
    
    phi_r = (v+(w*l))/r
    phi_l = (v-(w*l))/r
 
    
    # Prueba antirebote
    
    
    # Truncar velocidades a la velocidad maxima
    if(phi_r > 0):
        if(phi_r > MAX_SPEED):
            phi_r = MAX_SPEED
    else:
        if(phi_r < -MAX_SPEED):
            phi_r = -MAX_SPEED
            
    if(phi_l > 0):
        if(phi_l > MAX_SPEED):
            phi_l = MAX_SPEED
    else:
        if(phi_l < -MAX_SPEED):
            phi_l = -MAX_SPEED
    
    # print(phi_r)
    # print(phi_l)
       
    leftMotor.setVelocity(phi_l)
    rightMotor.setVelocity(phi_r)
    
    if(phi_l == 0 and phi_r == 0):
        print("Velocidad 0")
        leftMotor.setPosition(0)
        rightMotor.setPosition(0)
        
    pass

# Enter here exit cleanup code.
