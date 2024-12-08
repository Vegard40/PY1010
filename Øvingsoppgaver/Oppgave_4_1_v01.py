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

#Import of packages
import numpy as np
import matplotlib.pyplot as plt

#Define variables with numbers
month = np.array([1, 2, 3, 4, 5, 6,
                7, 8, 9, 10, 11, 12])  # [month]
temp = np.array([-3, -2, 2, 7, 11, 15,
                 17, 16, 12, 6, 2, -3])  # [deg. C]

# Calculation of mean value:
mean_temp = np.mean(temp)
print(f'Mean Value = {mean_temp:.1f}')

#Plotting temperatures
plt.close('all')
plt.figure(1)
plt.plot(month, temp, 'bo-', label='temperature')
plt.plot(month, temp*0 + mean_temp, 'g', label='Mean Value')
plt.legend()
plt.title('Month mean temperature at Skien, year 2005-2015')
plt.xlabel('Month no.')
plt.ylabel('Degree C')
plt.xlim(0, 13)
plt.ylim(-5, 20)
plt.grid()
plt.show()