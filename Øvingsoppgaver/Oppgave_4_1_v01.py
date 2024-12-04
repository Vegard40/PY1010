"""
Oppgave 4.1 Modifikasjon av programmet for temperaturplott
Ta utgangspunkt i Python-program 4.2 Modifiser programmet iht. følgende krav:
1. All tekst skal være p ̊a engelsk.
2. Programmet er laget av NN (n.n@usn.no).
3. De oppgitte temperaturverdiene, som er i celcius, skal regnes om fra celcius til
fahrenheit:
F = C∗(9/5) + 32 (4.1)
I Python kan du bruke arrayer direkte i slike formler. C i (4.1) kan alts ̊a være en
array, og F blir da ogs ̊a en array.
4. Kurven for temperaturene (fahrenheit) skal ha grønn farge, og punktene skal markeres
med grønne stjerner (*).
5. Kurven for middelverdien skal plottes i rødt.
6. x-aksen skal ha omr ̊ade [1, 12].
7. y-aksen skal settes automatisk av Python, hvilket oppn ̊as med  ̊a fjerne eller
≪kommentere bort≫ ylim-kommandoen.
"""

'''
Middeltemperaturer pr mnd i Skien 2005-2015

https://www.timeanddate.no/vaer/norge/skien/klima

'''

#Import av pakker
import numpy as np
import matplotlib.pyplot as plt

#Definisjon av variabler med tallverdier
mnd = np.array([1, 2, 3, 4, 5, 6,
                7, 8, 9, 10, 11, 12])  # [mnd nr]
temp = np.array([-3, -2, 2, 7, 11, 15,
                 17, 16, 12, 6, 2, -3])  # [grad C]

# Beregning av middelverdi:
mean_temp = np.mean(temp)
print(f'Middelverdi = {mean_temp:.1f}')

#Plotting av temperaturene
plt.close('all')
plt.figure(1)
plt.plot(mnd, temp, 'bo-', label='temperatur')
plt.plot(mnd, temp*0 + mean_temp, 'g', label='middelverdi')
plt.legend()
plt.title('Midlere maanedstemperatur i Skien 2005-2015')
plt.xlabel('Maaned nr.')
plt.ylabel('Grader C')
plt.xlim(0, 13)
plt.ylim(-5, 20)
plt.grid()
plt.show()