
import numpy as np
import math
import random
from graphics import *

#---------------------------------------------------------
TotalPoints=5000
#---------------------------------------------------------
PointsInCirclen=0
#---------------------------------------------------------
xPointIn=[]   # ASCISSE CASUALI
yPointIn=[]   # ORDINATE CASUALI --- SOTTO IL GRAFICO
xPointOut=[]  # ASCISSE CASUALI
yPointOut=[]  # ORDINATE CASUALI --- SOPRA IL GRAFICO
#---------------------------------------------------------
for p in range(TotalPoints):
    x = (random.random() * 2) - 1
    y = (random.random() * 2) - 1
    if(x**2+y**2 <= 1):
        PointsInCirclen+=1
        xPointIn.append(x)  # punto sotto
        yPointIn.append(y)        
    else:
        xPointOut.append(x)  # punto sopra
        yPointOut.append(y)
        
EstimatePI=4*PointsInCirclen/TotalPoints
Error = abs(math.pi-EstimatePI)

#---------------------------------------------------------
print("Total points=%d, Points in circle=%d, PI=%.5f, Error=%.5f" %(TotalPoints,PointsInCirclen,EstimatePI,Error))

#---------------------------------------------------------
drawCircle("Método Montecarlo", xPointIn, yPointIn, xPointOut, yPointOut);
