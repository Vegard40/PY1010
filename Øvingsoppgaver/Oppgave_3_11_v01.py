"""
Oppgave 3.11 Tekststreng
Opprett følgende tekststreng i et program: setning = ’Hanne og Stine er snille’. Bruk sListe
= setning.split() til  ̊a konvertere setningen til en liste med ord. Bruk kommandoen
sListe.reverse(), og se hva som skrives til skjerm. Klarer du n ̊a  ̊a bruke dette resultatet til  ̊a
lage tekststrengen: SNILLE er Stine og Hanne? Husk: Stor bokstaver i ’SNILLE’.
"""
#Definerer tekststrengen
setning = "Hanne og Stine er snille"
#Genererer en liste
sListe = setning.split()
#Reverserer listen
sListe.reverse()
#Endrer plass 0 i lista til store bokstaver
sListe[0] = sListe[0].upper()
#Skriver innholdet i lista til skjerm
print(sListe)