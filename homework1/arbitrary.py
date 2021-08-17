import math
from numpy import arange
from matplotlib import pyplot as plt 

def rho(a,adot,t):
    return 1 

def k(a,adot,t):
    return 1

def lam(a,adot,t):
    return 1

def F(a, adot, t):
    return math.sqrt((a**2)*8*math.pi*6.754*((10)**(-11))*rho(a,adot,t)/3+k(a,adot,t)+lam(a,adot,t)*a*a/3)

sta = 0 #starting time
en = 5 #ending time
N =5000 #step number
h = (en-sta)/N

tpoints = arange(sta,en,h) 
apoints = []
adotpoints = []

y = 0#a(sta)
u = 0#adot(sta)

for x in tpoints: #Runge-Kutta
    apoints.append(y)
    adotpoints.append(u)

    m1 = h*u
    k1 = h*F(y, u, x)  

    m2 = h*(u + 0.5*k1)
    k2 = h*F(y+0.5*m1, u+0.5*k1, x+0.5*h)

    m3 = h*(u + 0.5*k2)
    k3 = h*F(y+0.5*m2, u+0.5*k2, x+0.5*h)

    m4 = h*(u + k3)
    k4 = h*F(y+m3, u+k3, x+h)

    y += (m1 + 2*m2 + 2*m3 + m4)/6
    u += (k1 + 2*k2 + 2*k3 + k4)/6
plt.title("Intergration of Friedmann Function") 
plt.xlabel("t") 
plt.ylabel("a") 
plt.plot(tpoints, apoints)
plt.show()