"""
Oppgave 3.9 Dictionary
Opprett en dictionary med navn pannekaker med følgende nøkler (keys): hvetemel, salt,
egg, melk og smør med følgende verdier henholdsvis: 3 dl, 0.5 ts, 4, 6 dl og 2 ss. Skriv
deretter alle verdiene og s ̊a alle nøklene til dictionary pannekaker til skjerm.
"""
#Oppretter dictionary:
pannekaker = dict(hvetemel = "3dl", salt = "0.5ts", egg = 4, melk = "6dl", smør = "2ss")

#Printer nøkler og verdier til konsollen
print(pannekaker.keys())
print(pannekaker.values())
print(pannekaker)
