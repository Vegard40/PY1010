"""
Oppgave 4.2 Plott av flere kurver i samme diagram
Lag et program som gjør følgende med utgangspunkt i arrayen x som har følgende
elementer: 0, 1, 2, 3, 4, 5.
• Beregner y = x og z = kvadratroten av x.
•  ̊Apner et figurvindu som skal være ca. 12 cm bredt og ca. 9 cm høyt.
• Plotter (i figurvinduet) y vs. x i rødt og z vs. x i bl ̊att som linjeplott i ett og samme
diagram. Funksjonsverdiene (x, y) skal merkes med stjerner, funksjonsverdiene (x, z)
skal merkes med sirkler.
• Diagrammet skal ha kurvebeskrivelse (legend).
• Abscisseaksen skal ha merke ’x [s]’. Ordinataksen skal ha merke ’[m]’.
• Diagrammet skal ha rutenett.
• Figurvinduet skrives til pdf-fil med filnavn plott1.pdf.
"""
#Import av pakker
import numpy as np
from matplotlib import pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = x
z = np.sqrt(x)

plt.close('all')
plt.figure(1)
plt.plot(y, x, linestyle="-", color="red", label='y vs x')
plt.scatter(x, y, marker="*", color='blue')
plt.plot(x, z, linestyle="-", color="blue", label='x vs z')
plt.scatter(x, z, marker="o", color='blue')
plt.title('x vs y, og x vs z')
plt.legend()
plt.grid()
plt.xlabel("x[s]")
plt.ylabel('[m]')

plt.xlim(0, 12)
plt.ylim(0, 9)
plt.savefig("kurve.pdf", format="pdf")

plt.show()
plt.close()
