"""
Oppgave 3.7 Vinkler i trekant
Gjenta oppgave 3.6, men programmet skal n ̊a beregne og skrive ut vinklene i trekanten b ̊ade
i radianer og i grader. Programmet skal ogs ̊a sjekke at summen av vinklene er 180 grader.
Tips: Noen av disse numpy-funksjonene kan være nyttige: np.degrees, np.radians, np.arctan,
np.arccos, np.arcsin.
"""
import numpy as np

print("Dette programmet beregner vinklene i en rettvinklet trekant, og sjekker at summen av vinklene er 180 grader.") #Informasjon til bruker om funksjonen til programmet
a = int(input("Skriv inn verdien for lille katet i cm: " )) #Brukerinput av lille katet i cm
c = int(input("Skriv inn verdien for hypotenus i cm: ")) #Brukerinput av hypotenus i cm

#Finner vinkelen A
A = np.arcsin(a/c) #regner ut vinkelen mellom Hypotenus og store katet
A_grader = np.degrees(A)
A_rad = np.radians(A)
#Finner vinkelen B
B = np.arccos(a/c)
B_grader = np.degrees(B)
B_rad = np.radians(B)
#Vinkelen C = 90Grader
C_grader = 90.0
C_rad = np.radians(C_grader)
#Sjekker at vinklene til sammen er 180 grader
ABC_grader = A_grader + B_grader + C_grader


print("Vinkelen A er:", A_grader,"grader, og", A_rad,"Radianer")
print("Vinkelen B er:", B_grader,"grader, og", B_rad,"Radianer")
print("Vinkelen C er:", C_grader,"grader, og", C_rad,"Radianer")
print("Summen av vinklene er ", ABC_grader,"grader")


