"""
Du skal her lage et program som regner ut avstand mellom to punkter i planet. Gitt de to
punktene A = (2.3, 8.1) og B = (7.4, –13.5). Definer variablene xA = 2,3, yA = 8,1, xB =
7,4 og yB = −13,5. Bruk formel for Euklidsk avstand, og skriv svaret til skjerm p ̊a
10-er-eksponentform med 3 tall etter desimalskilletegnet (punktum).

"""
# Euklidisk avstand med numphy
# Importerer Numpy
import numpy as np
import math
import matplotlib.pyplot as plt

# Punkter
A = np.array([2.3, 8.1])
B = np.array([7.4, -13.5])

d1 = np.linalg.norm(A - B)
print("Euklidisk avstand med numpy:", "{:.3e}".format(d1))

# Euklidisk avstand med math
# Variabler
xA = 2.3
yA = 8.1
xB = 7.4
yB = -13.5

d2 = math.sqrt((xA - xB)**2 + (yA - yB)**2)
print("Euklidisk avstand med math:", "{:.3e}".format(d2))

plt.plot(A, B)
plt.show()