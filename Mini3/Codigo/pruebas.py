import random
import math

def poisson(ldpp,t):
    return t-((1/ldpp)*math.log(random.random()))

def exponencial(lde,t):
    return -((1/lde)*math.log(random.random()))#lde*math.exp(-lde*random.random())#

def caso1(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde):
    t = ta
    Na+=1
    n+=1
    Tt = poisson(ldpp,t)
    ta = Tt
    if (n == 1):
        Y = exponencial(lde,t)
        td = t + Y
    A.append(t)
    return t,Na,Nd,n,ta,td,A,D,Tp

def caso2(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde):
    t = td
    n-=1
    Nd+=1
    if(n == 0):
        td = float('Inf')
    else:
        Y = exponencial(lde,t)
        td = t + Y
    D.append(t)
    return t,Na,Nd,n,ta,td,A,D,Tp

def caso3(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde):
    t = td
    n-=1
    Nd+=1
    if(n > 0):
        Y = exponencial(lde,t)
        td = t + Y
    D.append(t)
    return t,Na,Nd,n,ta,td,A,D,Tp

def caso4(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde):
    Tp = max(t-T,0)
    return t,Na,Nd,n,ta,td,A,D,Tp

def selector(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde):
    B = 0
    if(ta <= td and ta <= T):
        # El siguiente evento es una llegada de una solicitud al 
        # sistema y aún no es la hora de cierre.
        print("CASO 1")
        t,Na,Nd,n,ta,td,A,D,Tp = caso1(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde)
    elif(td < ta and td <= T):
        # El siguiente evento es una salida de una solicitud del
        # sistema y aún no es la hora de cierre.
        print("CASO 2")
        t,Na,Nd,n,ta,td,A,D,Tp = caso2(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde)
    elif(min(ta,td)>T and n > 0):
        # El próximo evento ocurre luego de la hora de cierre 
        # y aún hay solicitudes en el sistema.
        print("CASO 3")
        t,Na,Nd,n,ta,td,A,D,Tp = caso3(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde)
    else:
        # El próximo evento ocurre luego de la hora de cierre
        # y ya no hay solicitudes en cola.
        print("CASO 4")
        t,Na,Nd,n,ta,td,A,D,Tp = caso4(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde)
        B = 1
    return t,Na,Nd,n,ta,td,A,D,Tp,B

def tiempoOcupado(A,D,N):
    tO = 0
    tD = 0
    C = []
    solcol = 0
    for i in range(0,min(len(A),len(D))):
        tO = tO + (D[i] - A[i]) # tiempo ocupado
    for j in range(0,min(len(A)-1,len(D)-1)):
        tD = tD + (A[j+1] - D[j]) # tiempo desocupado
    for k in range(0,len(A)-1):
        if(A[k+1] < D[k]):
            tC = D[k] - A[k+1]
        else:
            tC = 0
        C.append(tC)
        tCT = sum(C)
    for l in range(0,len(N)):
        if(N[l] >= 2):
            solcol = solcol + (N[l]-1)
        
    return tO, tD, tCT, solcol

def servidor(T,ldpp,lde):
    t = 0
    Na = 0
    Nd = 0
    n = 0
    N = []
    T0 = poisson(ldpp,t)
    ta = T0
    td = float('Inf')
    Tp = 0
    A = []
    D = []
    B = 0
    while(t<T and B == 0):
        t,Na,Nd,n,ta,td,A,D,Tp,B = selector(t,Na,Nd,n,ta,td,A,D,Tp,ldpp,lde)
        N.append(n)
        #print("t",t,"\n","Na",Na,"\n","Nd",Nd,"\n","ta",ta,"\n","td",td,"\n","Tp",Tp,"n",n)
        print(len(A))
        print(len(D))
    print("Solicitudes ingresadas",Na)
    print("Solicitudes egresadas",Nd)
    print("Tiempo ocupado", tiempoOcupado(A,D,N)[0])
    print("Tiempo desocupado",tiempoOcupado(A,D,N)[1])
    print("Tiempo total en cola",tiempoOcupado(A,D,N)[2])
    print("Promedio en cola de cada solicitud",tiempoOcupado(A,D,N)[2]/sum(N))
    print("Solicitudes en cola por segundo",tiempoOcupado(A,D,N)[3]/T)
    print("Tiempo de salida de la última solicitud",td)
    print("Tiempo promedio por solicitud",tiempoOcupado(A,D,N)[0]/len(D))
    

# caracteristicas servidor
T = 1
lde = 100
ldpp = 2400/60

servidor(T,ldpp,lde)
