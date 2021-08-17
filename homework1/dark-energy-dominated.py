import math
from numpy import arange
from matplotlib import pyplot as plt
sta = 0 #starting time
en = 2*((10)**(5)) #ending time
N =5000 #step number
h = (en-sta)/N
tpoints = arange(sta,en,h) 
apoints = []
y = 0#a(sta)
for x in tpoints:
    y=math.exp(x*math.sqrt(0.6899)*67.66*365*24*60*60/(3.26*9.46*((10)**(12))))
    apoints.append(y)
plt.title("Intergration of Friedmann Function") 
plt.xlabel("t") 
plt.ylabel("a") 
plt.plot(tpoints, apoints)
plt.show()