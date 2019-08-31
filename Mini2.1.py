""" MINIPROYECTO 2 """

# imports
import numpy as np
import random

# Ejercicio 1: Función acumulada ponderada
"""descripción del algoritmo"""

# Ejercicio 2: Función acumulada ponderada
def FuncionAcumulada(n,pi,Fi):
    FX = 0
    for i in range(n)
        FX = FX + pi(i)*Fi(i)
    return FX

# Ejercicio 3: Valor presente neto
def Ejercicio3(iteraciones,tasa):
    ganaHotel = 0
    ganaCC = 0
    for i in range(iteraciones):
        vpnH = VPN(flujos(0),tasa)
        vpnCC = VPN(flujos(1),tasa)
        if (vpnH < vpnCC):
            ganaHotel = ganaHotel + 1
        else:
            ganaCC = ganaCC + 1
    return [ganaHotel, ganaCC]
        

def flujos(num):
    flujo = np.empty([7,1])
    if (num == 0):
        flujo[0] = -800
        flujo[1] = Normal(-800,50)
        flujo[2] = Normal(-800,100)
        flujo[3] = Normal(-700,150)
        flujo[4] = Normal(300,200)
        flujo[5] = Normal(400,200)
        flujo[6] = Normal(500,200)
        flujo[7] = Uniform(200,8440)
    else:
        flujo[0] = -900
        flujo[1] = Normal(-600,50)
        flujo[2] = Normal(-200,50)
        flujo[3] = Normal(-600,100)
        flujo[4] = Normal(250,150)
        flujo[5] = Normal(350,150)
        flujo[6] = Normal(400,150)
        flujo[7] = Uniform(1600,6000)


def VPN(flujo, tasa):
    n = len(flujo)
    vpn = 0
    for i in range(n):
        P = flujo[i]*(1/((1+tasa)**i))
        vpn = vpn + P
    return vpn
        
    
def Normal(mu,sigma):
    y1 =
    y2 =
    fun = y2 - ((y1-1)**2)/2
    if (fun>0):
        y = y2 - ((y1-1)**2)/2
        u = random.uniform()
        if (u<0.5):
            return mu + sigma*y1
        else:
            return mu - sigma*y1


# Ejercicio 4: Repartidor de periódicos
def Periodicos(dias,p_comprados):
    p_vendidos = 0
    p = [0.3,0.4,0.3]
    x = random.Random()
    if (x < p[0]):
        p_solicitados = 9
    elif(x < p[0]+p[1]):
        p_solicitados = 10
    else:
        p_solicitados = 11

    if(p_solicitados <= p_comprados):
        retorno = (p_comprados - p_solicitados)*0.5
        perdida = 0
    else:
        retorno = 0
        perdida = (p_solicitados - p_comprados)

    
    
        



        
