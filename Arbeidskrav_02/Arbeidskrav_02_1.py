"""
Oppg 1) Du skal her lage et program som skal starter med
alder = int(input('Hvilket år er du født? ') )
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive
svaret til skjerm med passende tekst.
"""
import time
import math
import numpy as np

#Spør brukeren om å skrive inn sin alder med input
alder = int(input("Hvilket år er du født? ") )
#Definerer epoch, for å definere presis tidsregning
epoch = time.time() / 60 / 60 / 24 / 365
#Regner ut personens alder, og runder av resultatet ned til nermeste heltall
personens_alder = math.floor(float(1970) + epoch - float(alder))
#Skriver alder i konsollen
print("Du er eller blir" ,personens_alder , "år i løpet av ",math.floor(epoch + 1970))