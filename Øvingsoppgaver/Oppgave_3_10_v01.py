"""
Oppgave 3.10 Liste
Opprett følgende liste i et program: navn = [’Geir’, ’Anne’, ’Tor’, ’Mari’]. Bruk denne listen
og f ̊a programmet til  ̊a skrive ut teksten: Torgeir og Marianne. Hint: navn[1].lower(), samt
at ordet ’og’ kan hardkodes i utskriftsstrengen.
"""

#Definerer listen
navn = ['geir', 'Anne', 'Tor', 'Mari']

#Skriver resultatet til konsollen
print(navn[2] + navn[0].lower(), "og", navn[3] + navn[1].lower())
