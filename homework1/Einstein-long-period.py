import math
from numpy import arange
from matplotlib import pyplot as plt 
from scipy import integrate
def F(a):
    return math.sqrt(1.5*0.0001/(a**2)+1/a)*67.66*365*24*60*60/(3.26*9.46*((10)**(12))) #simplified Friedmann Function

sta = 1 #starting time
en = 2*((10)**(10)) #ending time
N =50000#step number
h = (en-sta)/N

tpoints = arange(sta,en,h) 
apoints = []

for x in tpoints: 
    v, err = integrate.quad(F, sta, x) #intergration
    apoints.append(v)

plt.title("Intergration of Friedmann Function") 
plt.xlabel("t") 
plt.ylabel("a") 
plt.plot(tpoints, apoints)
plt.show()
