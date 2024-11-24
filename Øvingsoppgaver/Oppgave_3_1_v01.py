"""
Du f ̊ar renter p ̊a innskudd i bank. Opprett variabelen belop = 10 000, som representerer
innskuddet. Bankens rente er 1,85 %. Beløp etter ett  ̊ar er gitt ved formelen:

belop·(1 + 1,85/100) (3.5)

Lag et program som regner ut beløpet p ̊a konto etter 5  ̊ar. Skriv svaret til skjerm formatert
som et flyttall med 2 sifre etter desimalskilletegnet (punktum).

"""
# Startbeløp
belop = 10000.00
# Rente
rente = 0.0185
# Antall år det skal spares
ar = int(input("hvor mange år vil du spare? "))
# Starter løkken med startbeløp
tot_belop = belop
# Utregning
for i in range(ar):
    tot_belop += tot_belop * rente
# Utskrift resultat
print("Du startet med ",belop)
print(f"du har nå etter {ar} år spart: {tot_belop:.2f} kroner")

