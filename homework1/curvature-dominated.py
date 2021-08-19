import math
from numpy import arange
from matplotlib import pyplot as plt
sta = 0 #starting time
en = 5 #ending time
N =5000 #step number
h = (en-sta)/N
tpoints = arange(sta,en,h) 
apoints = []
for x in tpoints:
    y=x
    apoints.append(y)
plt.title("Intergration of Friedmann Function") 
plt.xlabel("t") 
plt.ylabel("a") 
plt.plot(tpoints, apoints)
plt.show()


    
