"""
Oppgave 2.4 time-modulen
time er en modul i Python som inneholder en rekke funksjoner. time-modulen inneholder
bl.a. time-funksjonen og sleep-funksjonen.

Oppgave a
Finn fram til dokumentasjon av time-funksjonen og sleep-funksjonen p ̊a internett, og gi en
kort beskrivelse av hva de to funksjonene gjør.

Time:
Modulen tilbyr forskjellige tidsrelaterte funksjoner. Modulen er plattformbegrenset, da ikke alle funksjoner er
tilgjengelig i alle plattformer. epoken for time starter 1 januar klokka 00:00:00 i året 1970. som er
tidsreferansepunktet. Modulen må importeres med import time.
Den kan for eksempel brukes til å måle hvor lang tid en operasjon tar.

Sleep kan brukes til for eksempel å legge inn pauser i programmet



Oppgave b
Lag et (lite) Python-program der du bruker time og sleep (f.eks. kan programmet brukes til
 ̊a sjekke om sleep faktisk fungerer som forventet). Tips: Koden t0 = time.time() gir
variabelen t0 verdi lik antall sekunder som har g ̊att fra det s ̊akalte epoch-tidspunktet, som
er definert i dokumentasjonen for time-funksjonen. Obs: For  ̊a gjøre modulen time
tilgjengelig i dine programmer m ̊a du importere modulen
"""
import time

start = time.time()
for i in range(1000000):
    pass
slutt = time.time()
tid = time.ctime(slutt)
print("Venter 2 sekunder...")
time.sleep(2)
print("Ferdig!")
print(tid)
print(f"Operasjonen tok {slutt - start} sekunder.")