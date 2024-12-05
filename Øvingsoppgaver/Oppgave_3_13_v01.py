"""
Oppgave 3.13 Fra tekst til liste til integer
Gitt tekststrengen s = ’Nedre grense for karakter E er 40 poeng.’. Skriv et program som
konverterer teksten til en liste, plukker s ̊a ut 40 fra listen, og konverterer 40 til datatypen
int. (Hint: split().)
"""
from os.path import split
#Definerer listen s
s = "Nedre grense for karakter E er 40 poeng."
#Gjør om tekststrengen til en liste
sl = s.split()
#Plukker ut 40, som er item 6 i lista
item6 = int(sl[6])
#printer item6 til konsollen
print(item6)

