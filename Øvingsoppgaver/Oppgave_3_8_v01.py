"""
Oppgave 3.8 Tuppel
Opprett en tuppel med navn odd som inneholder de 7 første oddetallene og en Tuppel
≪primes≫ som inneholder de 6 første primtallene. Definer deretter mix = odd + primes.
Finn s ̊a antall ganger tallet 11 er representert i ≪mix≫ og om tallet 14 er representert i
≪mix≫. Svarene skrives til skjerm.
"""
#Definerer de to tuplene
odd = (1,3,5,7,9,11,13)
primes = (2,3,5,7,11,13)
mix = odd + primes

#Sjekker hvor mange ganger tallet 11 er representert i mix og skriver resultatet til konsollen
antall_11 = mix.count(11)

print("Tupelen inneholder følgende tall", mix)

print("Tallet 11 er representert",antall_11,"ganger i mix")

#Sjekker om tallet 14 er representert i mix og skriver resultatet til konsollen
if 14 in mix:
    print("Tallet 14 finnes i tupelen")
else:
    print("Tallet 14 finnes ikke i tupelen")
