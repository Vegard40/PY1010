"""
Oppgave 2.2 Lag et program i Spyder som regner om fra F til C
Lag et program i Spyder som regner om en temperatur gitt i grader fahrenheit til grader
celsius. Brukeren skal skrive inn fahrenheit-verdien i programmet (selve programkoden), og
b ̊ade fahrenheit-verdien og celsius-verdien skal vises i konsollen (vha. print-funksjonen).
Finn selv fram til funksjonssammenhengen mellom grader celsius og grader fahrenheit.
Bruk programmet til  ̊a regne om 0 grader farenheit til grader celsius.
57
"""
#Deklarerer F som variabel med funksjonen "input", Brukeren kan selv velge grader F
F = float(input("Skriv inn temperatur i Farenheit:"))
#Deklarerer C med en beregning
C = (F - 32.0) / 1.8
#Skriver ut verdien i C og F
print("Temperaturen er",F,"grader Farenheit")
print("Temperaturen er",C,"grader Celsius")