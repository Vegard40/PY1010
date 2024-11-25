"""
Oppgave 3.12 Liste med navn og nummer
Opprett følgende lister: navn = [’Eli’, ’Ola’, ’Ali’, ’Ela’] og tlf = [9423234, 9223001,
4756001, 9592676]. Navn og tlelefonnumer st ̊ar oppført i samme posisjon i de to listene.
Skriv et program som tar et navn fra kommandolinjen (konsollen) som input og skriver ut
personens telefonnummer. Hint: navn.index().
"""

navn = ["Eli", "Ola", "Ali", "Ela"]
tlf = [9423234, 9223001, 4756001, 9592676]

print(navn.index(0, tlf))
