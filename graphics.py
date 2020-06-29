# graphics.py
import matplotlib.pyplot as plt
import numpy as np
import math

def f(x): return math.sqrt(1-x**2)

def drawCircle(xPointIn, yPointIn, xPointOut, yPointOut):
  #--------------------------------------------------------- Grafico
  X=np.linspace(0,1)
  yf=[]
  for x in X:
    yf.append(f(x))
#---------------------------------------------------------
  plt.axis   ("equal")                              # assi
  plt.grid   (which="major")                        # griglia
  plt.plot   (X , yf, color="blue" , linewidth="2") # Funzione
  plt.scatter(xPointIn, yPointIn, color="green", marker   =".") # Sotto...
  plt.scatter(xPointOut, yPointOut, color="red"  , marker   =".") # Sopra...
  plt.title  ("Método Montecarlo")

  plt.show()
