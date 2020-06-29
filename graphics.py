# graphics.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math

def f(x): return math.sqrt(1-x**2)

def drawCircle(title, xPointIn, yPointIn, xPointOut, yPointOut):
  plt.axis("equal")
  plt.grid   (which="major")

  plt.scatter(xPointIn, yPointIn, color="green", marker   =".") # Sotto...
  plt.scatter(xPointOut, yPointOut, color="red"  , marker   =".") # Sopra...
  
  plt.title  (title)

  plt.show()
