"""
Lag et program for følgende beregninger p ̊a en rettvinklet trekant iht. følgende
spesifikasjoner:
• Brukeren skal oppgi ‘lille katet’ og hypotenusen i konsollen.
• Programmet skal regne ut store katet og skrive resultatet til skjerm.
• Programmet skal regne ut omkretsen og arealet av trekanten og skrive resultatet til
skjerm.
"""
import numpy as np

print("Dette programmet beregner store katet i en rettvinklet trekant.") #Informasjon til bruker om funksjonen til programmet
a = int(input("Skriv inn verdien for lille katet i cm: " )) #Brukerinput av lille katet i cm
c = int(input("Skriv inn verdien for hypotenus i cm: ")) #Brukerinput av hypotenus i cm

b = np.sqrt(a**2 + c**2) #Regner ut store katet

O = a + b + c # Regner ut omkretsen av trekanten

A = (a * b) / 2 #Regner ut arealet av trekanten

print("Omkretsen av trekanten er:",O,"cm") #Skriver ut omkretsen i konsollen

print("Arealet av trekanten er:",A,"cm2") #Skriver ut Arealet i konsollen
