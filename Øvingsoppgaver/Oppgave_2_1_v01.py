"""
Oppgave 2.1 Python som kalkulator
Anta at du har et forbruksl ̊an (L) p ̊a kr 100 000 med rentesats (r) 23,4 % pr  ̊ar. Hvis du
ikke betaler noe avdrag, hvor mye (kr) betaler du da i rente pr m ̊aned (R)? Finn svaret ved
 ̊a bruke Python som kalkulator, b ̊ade med beregning med bare tall og med beregning med
bruk av variable (bokstavsymboler).
"""
#Deklarerer L som variabel med datatype integer
L = 100000.0
#Deklarerer r som årlig rente
r = 23.4
#Regner ut rente per måned
R = L * r / 100.0 / 12
print("Du betaler",R,"kr/måned i rente")