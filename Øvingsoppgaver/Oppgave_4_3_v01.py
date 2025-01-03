"""
Oppgave 4.3 Subplott
Som oppgave 4.2, men n ̊a med subplott der y plottes i øverste subplott og z plottes i
nederste subplott. Filnavnet kan være plott2.pdf.
"""
#Import av pakker
import numpy as np
from matplotlib import pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = x
z = np.sqrt(x)

#Figur med subplot
#plt.subplot(figsize=(10, 6))

#Subplot 1
plt.subplot(2, 1, 1)
plt.plot(y, x, linestyle="-", color="red", label='y vs x')
plt.scatter(x, y, marker="*", color='blue')
plt.title('x vs y')
plt.legend()
plt.grid()
plt.xlabel("x[s]")
plt.ylabel('[m]')
plt.xlim(0, 6)
plt.ylim(0, 6)

plt.subplot(2, 1, 2)
plt.plot(x, z, linestyle="-", color="blue", label='x vs z')
plt.scatter(x, z, marker="o", color='blue')
plt.title('x vs z')
plt.legend()
plt.grid()
plt.xlabel("x[s]")
plt.ylabel('[m]')
plt.xlim(0, 6)
plt.ylim(0, 6)

#Genererer en .pdf fil av plottet
plt.savefig("plott2.pdf", format="pdf")

plt.show()
plt.close()