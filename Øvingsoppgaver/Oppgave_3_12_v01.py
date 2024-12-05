"""
Oppgave 3.12 Liste med navn og nummer
Opprett følgende lister: navn = [’Eli’, ’Ola’, ’Ali’, ’Ela’] og tlf = [9423234, 9223001,
4756001, 9592676]. Navn og tlelefonnumer st ̊ar oppført i samme posisjon i de to listene.
Skriv et program som tar et navn fra kommandolinjen (konsollen) som input og skriver ut
personens telefonnummer. Hint: navn.index().
"""
#Definerer lister
navn = ["Eli", "Ola", "Ali", "Ela"]
tlf = [9423234, 9223001, 4756001, 9592676]
#Ber bruker om å skrive inn et navn
navninput = input("Hvilket navn vil du ha telefonnummeret til?: ")
#Sjekker om navnet som er skrevet inn er i listen
if navninput in navn:
    navninputindex = navn.index(navninput)
    print("Telefonnummeret til", navninput, "er", tlf[navninputindex])
#Dersom navnet ikke er i listen får brukeren beskjed om det
else:
    print("Navnet du har skrevet er ikke i telefonlista")
