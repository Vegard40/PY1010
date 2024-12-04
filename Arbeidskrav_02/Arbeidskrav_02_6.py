"""
Oppg 6) Skriv en kode som plotter funksjonen 𝑓(𝑥) = −𝑥2 − 5, for x på intervallet [-10,10].
Hint: np.linspace(-10, 10, 200) gir en array med 200 punkter jevnt fordelt på intervallet
[-10,10].
"""
#Importerer biblioteker som skal brukes
import numpy as np
import matplotlib.pyplot as plt

#Definerer x som en array med np.linspace
x = np.linspace(-10,10,200)

#Definerer funksjonen som skal plottes
def f(x):
    return (-x*2) - 5

#Regner ut punktene med alle definerte verdier for x
y = f(x)

#Plotter linjen
plt.plot(x, y, label= "f(x)")
#Legger til en tittel i plottet
plt.title("Plott av funksjonen f(x)= -2x -5")
#Legger til verdier på x aksen
plt.xlabel("x")
#Legger til verdier på y aksen
plt.ylabel("f(x)")
#legger til rutenett i plottet
plt.grid(True)
#Legger til grafens "label" i plottet
plt.legend()
#Viser plottet
plt.show()