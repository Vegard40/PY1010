"""
Oppg 3) Lag et program med en funksjon som regner om fra grader til radianer.
Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180
Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....
"""
import numpy as np
#Informerer brukeren om hva programmet gjør
print("programmet regner om fra grader til radianer.")
#Ber brukeren om å skrive inn grader som skal regnes om
v_grad = float(input('Skriv inn gradtallet:' ))
#regner om fra grader til radianer
v_rad = v_grad*np.pi/180
#Skriver svaret i konsollen
print(v_grad, "grader", "er", v_rad, "radianer")