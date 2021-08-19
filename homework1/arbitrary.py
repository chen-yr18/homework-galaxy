import math
from numpy import arange
from matplotlib import pyplot as plt 

def rho(a,t):
    return 1.5*0.0001/a**3+1/a**4

def k(a,t):
    return 0

def lam(a,t):
    return 0

def F(a,t):
    return math.sqrt((a**2)*8*math.pi*6.754*((10)**(-11))*rho(a,t)/3-k(a,t)+lam(a,t)*a*a/3)

sta = 0 #starting time
en = 5 #ending time
N =5000 #step number
h = (en-sta)/N

tpoints = arange(sta,en,h) 
apoints = []


y = 0.001#a(sta)


for x in tpoints: #Runge-Kutta
    apoints.append(y)

    k1 = h*F(y, x)  

    k2 = h*F(y+0.5*k1, x+0.5*h)

    k3 = h*F(y+0.5*k2, x+0.5*h)

    k4 = h*F(y+k3, x+h)

    y += (k1 + 2*k2 + 2*k3 + k4)/6
    
plt.title("Intergration of Friedmann Function") 
plt.xlabel("t") 
plt.ylabel("a") 
plt.plot(tpoints, apoints)
plt.show()
