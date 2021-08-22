import math
from numpy import arange
from matplotlib import pyplot as plt 
from scipy import integrate
c=1
H0=1
Omega_r0=0
Omega_m0=1
Omega_k0=0
Omega_lam0=0
k=0
def DL(z,x,k):
    return (1+z)*fk(x,k)

def DA(z,x,k):
    return fk(x,k)/(1+z)

def fk(x,k):
    if k>0:
        return (k**(-0.5))*math.sin((k**(0.5))*x)
    elif k==0:
        return x
    else:
        return ((-k)**(-0.5))*math.sinh(((-k)**(0.5))*x)


def E(z):
    a=1/(1+z)
    return math.sqrt(Omega_r0*(a**(-4))+Omega_m0*(a**(-3))+Omega_k0*(a**(-2))+Omega_lam0)

def F(z):
    a=1/(1+z)
    return c/(H0*a*a*E(z))

def x(z):
    a=1/(1+z)
    res, err = integrate.quad(F, a, 1)
    return res
    

sta = 0 #starting time
en = 5 #ending time
N =100 #step number
h = (en-sta)/N
zpoints = arange(sta,en,h) 
DLpoints=[]
DApoints=[]
for z1 in zpoints:
    DLpoints.append(DL(z1,x(z1),k))
    DApoints.append(DA(z1,x(z1),k))
    

plt.title("Angular Diameter Distance and Luminosity Distance for different Redshifts") 
plt.xlabel("z") 
plt.ylabel("distance") 
plt.plot(zpoints, DLpoints ,label="Luminosity Distance")
plt.plot(zpoints, DApoints ,label="Angular Diameter Distance")
plt.legend()
plt.show()    









