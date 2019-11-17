import numpy as np
import matplotlib.pyplot as plt 

prueba = lambda x: -x**2 + 2
prueba2 = lambda x: x

x = np.linspace(0,1)
y = prueba2(x)
yx = prueba(x)*x
yx_y = yx/y

plt.plot(x, y)

plt.show()

# recibiendo función
def Centroide(fun, limi, lims, dx):
    samples = round((lims - limi)/dx)
    x = np.linspace(limi,lims,samples)
    z = fun(x)
    zx = fun(x)*x
    iz = np.trapz(z,x)
    izx = np.trapz(zx,x)
    return izx/iz

# recibiendo arrays
def CentroideA(x,y):
    z = y
    zx = y*x
    iz = np.trapz(z,x)
    izx = np.trapz(zx,x)
    return izx/iz
    
print(Centroide(prueba2,0,1,0.01))
print(CentroideA(x,y))
