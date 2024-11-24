"""
Gjenta oppgave 3.3, men programmet skal n ̊a motta koordinatene fra konsollen med
input-funksjonen.

"""

# Euklidisk avstand med numphy
# Importerer Numpy
import numpy as np
import math
import matplotlib.pyplot as plt


# Punkter
A = np.zeros(2)

for i in range(2):
    A[i] = float(input(f"Oppgi tall for A: {i + 1}: "))

B = np.zeros(2)
for i in range(2):
    B[i] = float(input(f"Oppgi tall for B: {i + 1}: "))

d1 = np.linalg.norm(A - B)
print("Euklidisk avstand med numpy:", "{:.3e}".format(d1))

plt.plot(A, B)
plt.show()
"""
# Euklidisk avstand med math
# Variabler
xA = float(input("Legg inn punkt xA: ")) #punktet skal være 2.3
yA = float(input("Legg inn punkt yA: ")) #punktet skal være 8.1
xB = float(input("Legg inn punkt xB: ")) #punktet skal være 7.4
yB = float(input("Legg inn punkt yB: ")) #punktet skal være -13.5

d2 = math.sqrt((xA - xB)**2 + (yA - yB)**2)
print("Euklidisk avstand med math:", "{:.3e}".format(d2))

"""