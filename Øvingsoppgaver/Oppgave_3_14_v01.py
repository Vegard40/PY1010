"""
Oppgave 3.14 Reisens lengde
Lag et program som regner ut tilbakelagt avstand p ̊a en ’reise’ fra punkt til punkt i planet
(2D). Anta at startpunktet er origo. Programmet skal starte med  ̊a motta koordinater (x, y)
for neste destinasjon ved bruk av følgende kode:
xend = float(input(’Skriv inn x-koordinaten for neste destinasjon her:’ ))
yend = float(input(’Skriv inn y-koordinaten for neste destinasjon her:’ ))

Programmet regner s ̊a ut tilbakelagt avstand og spør om neste destinasjon.
Du kan da bruke samme kode som ovenfor (men vi forventer ikke at du lager noen funksjon for
gjenbruk av kode; funksjoner er tema i et senere kapittel, nærmere bestemt kap. 5).

Husk: xend og yend fra kodelinjene over n ̊a skal utgjøre startpunktet for neste ’reise’.

Programmet regner s ̊a ut total tilbakelagt avstand fra startpunkt til sluttpunkt
og skriver svaret til skjerm med passende tekst.
"""
#Importerer pakker
import math
import numpy as np

#lager to lister for henholdsvis x og y, og definerer origo
x = [0.0]
y = [0.0]
#Lager en variabel for mellomlagring av tilbakelagt distanse, med startverdi 0
d1 = 0.0
#Ber bruker om å skrive inn koordinater for neste destinasjon
while True:
    valg = input("Vil du legge til en koordinat skriv 1 \nVil du avslutte skriv 2 ")
    if valg == "1":
        xend = float(input("Skriv inn x-koordinaten for neste destinasjon her: "))
        x.append(xend)
        yend = float(input("Skriv inn y-koordinaten for neste destinasjon her: "))
        y.append(yend)
    elif valg == "2":
        break
    else:
        print("du har trykket feil, prøv igjen")

#Her må jeg regne ut den euklidiske avstanden
d = math.sqrt((xend - x[0])**2 + (yend - y[0])**2)
print("tilbakelagt distanse på denne turen er: ", d)

#Her må jeg mellomlagre d som d1
d1 = d1 + d
print(x)
print(y)
print(d1)

