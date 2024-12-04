"""
Oppg 2) Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et
program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive
svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe
5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan
sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)?
"""
import math
# Informerer brukeren om hva programmet gjør
print("Dette programmet regner ut hvor mange pizza du bør kjøpe dersom du skal arrangere en klassefest.")
#Ber bruker om å skrive inn antall elever som kommer på fest
antall_elever = int(input('Hvor mange elever kommer på klassefesten?' ))
#Regner ut hvor mange pizza det er behov for
antall_pizza = antall_elever / 4


print("Det bør kjøpes inn", math.ceil(antall_pizza), "pizzaer til festen.")

