"""
Oppgave 3.15 En reise i rommet
Oppgaven er lik oppgave 3.14, men oppgaven tar av litt, for n ̊a skal du reise i rommet! Du
skal ogs ̊a beregne ≪netto≫ avstand fra startpunktet (origo) til sluttpunktet – uten  ̊a ta
hensyn til ruten mellom disse punktene. Test programmet ditt med noen enkle datapunkter,
f.eks. en reise fra (0,0,0) → (1,1,0) → (1,1,1). Til info: Punkter i rommet er gitt ved
koordinatene (x, y, z).
"""
#Importerer pakker
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#lager to lister for henholdsvis x og y, og definerer origo
x = [0.0]
y = [0.0]
z = [0.0]

# Lager variabler for mellomlagring av tilbakelagt distanse, med startverdi 0
d1 = 0.0

#Ber bruker om å skrive inn koordinater for neste destinasjon
while True:
    valg = input("Vil du legge til en koordinat skriv 1 \nVil du avslutte skriv 2 ")

    if valg == "1":
        #Ber bruker om å skrive inn nye koordinater
        xend = float(input("Skriv inn x-koordinaten for neste destinasjon her: "))
        yend = float(input("Skriv inn y-koordinaten for neste destinasjon her: "))
        zend = float(input("Skriv inn z-koordinaten for neste destinasjon her: "))

        # Her må jeg regne ut den euklidiske avstanden
        d = math.sqrt((xend - x[-1]) ** 2 + (yend - y[-1]) ** 2 + (zend - z[-1]) ** 2)

        #Legger de nye koordinatene inn i listene
        x.append(xend)
        y.append(yend)
        z.append(zend)

        # Her må jeg mellomlagre d som d1
        d1 += d

        #informerer om distanse for nåværende reise
        print(f"Du har nå reist {d:.2f} km")
    elif valg == "2":
        break
    else:
        print("du har trykket feil, prøv igjen")

#Her informeres brukeren om totalt tilbakelagt distanse

#Utregning av netto distanse fra origo til siste punkt
dn = math.sqrt((xend - x[0]) ** 2 + (yend - y[0]) ** 2 + (zend - z[0]) ** 2)
print(f"Total tilbakelagt distanse på denne turen er: {d1:.2f} km")
print(f"Netto distanse fra origo til siste punkt er: {dn:.2f} km")

# Opprett 3D-aksene
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot hver vektor som en pil
ax.quiver(
    x[0], y[0], z[0],  # Startpunkter
    x[-1], y[-1], z[-1],  # Vektorkomponenter
    color="b", arrow_length_ratio=0.1
    )

# Juster visningen
ax.set_xlim([0, 20])
ax.set_ylim([0, 20])
ax.set_zlim([0, 20])

ax.set_xlabel("X-akse")
ax.set_ylabel("Y-akse")
ax.set_zlabel("Z-akse")

plt.title("3D-plot av vektorer")
plt.show()
