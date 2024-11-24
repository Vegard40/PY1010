"""
Oppgavetekst:
    Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du
    ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med
    bensinbil.

    Lag et Python-program som beregner og presenterer (i konsollen) de årlige
    totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse
    basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se
    bort fra kostnader som renter på billån og verditap (du har da egentlig
    antatt at slike kostnader er like for elbil og bensinbil).

    Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan
    diskuteres, men ikke ifm. denne oppgaven :-)

        -Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk.
         Ev. (hvis du ikke har bil) kan du anta 10.000 km.
        -Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
        -Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
        -Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading):
         2.00 kr/kWh. Bensinbil: 1,0 kr/km.
        -Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

Created on Tue Oct 15 20:09:09 2024

@author: Vegard H. Tangen
"""
#Definerer kjørelengde som en input, bruker skriver inn årlig kjørelengde:
KjorelengdeKmPrAr = int(input("Oppgi Kjørelengde:"))
#Definerer forsikringskostnader:
ForsikringEl = 5000
ForsikringBensin = 7500
#Definerer trafikkforsikringsavgift til staten:
TFAvgiftPrAr = 8.38 * 365
#Definerer drivstoffkostnader per år:
DrivstoffKostElPrAr = 0.2 * 2 * KjorelengdeKmPrAr
DrivstoffKostBensinPrAr = 1 * KjorelengdeKmPrAr
#Definerer bompengeavgifter per år:
BomavgiftElPrAr = 0.1 * KjorelengdeKmPrAr
BomavgiftBensinPrAr = 0.3 * KjorelengdeKmPrAr
#Utregning av kostnader per år for elbil:
KostnadPrArEl = ForsikringEl + TFAvgiftPrAr + DrivstoffKostElPrAr + BomavgiftElPrAr
#Utregning av kostnad per år for bensinbil:
KostnadPrArBensin = ForsikringBensin + TFAvgiftPrAr + DrivstoffKostBensinPrAr + BomavgiftBensinPrAr
#Utregning av kostnadsdifferanse:
Differanse = KostnadPrArBensin - KostnadPrArEl
#Utskrift av resultat i konsoll:
print("Oppgitt Kjørelengde er:",KjorelengdeKmPrAr)
print("Elbil koster:",KostnadPrArEl)
print("Bensinbil koster",KostnadPrArBensin)
print("Det er",round(Differanse),"kroner billigere å kjøre elbil per år")
