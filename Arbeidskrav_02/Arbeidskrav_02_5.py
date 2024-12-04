"""
Oppg 5) Lag et program med en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet trekant og en
halvsirkel, se figuren under. Med «ytre» omkrets menes samlet lengde av de sorte strekene.
Funksjonen skal returnere arealet og «ytre» omkrets, som så skrives til skjerm med passende
tekst.
"""
import numpy as np
import matplotlib.pyplot as plt
#Ber bruker om lengde på lille og store katet
a = int(input("Dette programmet regner ut omkrets og areal \nfor en figur satt sammen av en rettvinklet trekant og en sirkel \nskriv inn lengden for lille katet a i cm: "))
b = int(input("Skriv inn lengden på store katet b i cm: "))
#Regner ut hypotenus
c = np.sqrt(a**2 + b**2)
#Regner ut sirkelens radius
r = a / 2.0
#Regner ut sirkelens areal
As = np.pi * r**2.0
#Regner ut sirkelens omkrets
Os = 2.0 * np.pi * r
#Regner ut trekantens areal
Atr = (a * b) / 2.0
#Regner ut trekantens omkrets
Otr = a + b + c
#Regner ut figurens ytre omkrets
Otot = (Os / 2.0) + a + c
#Regner ut figurens totale areal
Atot = (As / 2.0) + Atr
#Skriver forespurt informasjon ut i konsollen
#print("Arealet av sirkelen er:", As)
#print("Omkretsen av sirkelen er: ", Os)
#print("Arealet av trekanten er: ", Atr)
#print("Omkretsen av trekanten er: ", Otr)
print("Den totale omkretsen for figuren er: ", Otot, "cm")
print("Det totale arealet for figuren er: ", Atot, "cm2")