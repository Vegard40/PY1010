#Importerer pandas, matplotlib, timedelta, og numpy for blant annet å kunne lese inn kildefil og lage plot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Del a

# Leser inn kildefilen, Excel-filen som er vedlagt oppgaven
kildefil = "support_uke_24.xlsx"
kundedata = pd.read_excel(kildefil)

# Test av "kundedata"
#print(kundedata)

# Henter ut kolonner fra kildefilen, og lagrer dem som variabler (Arrays)
u_dag = kundedata.iloc[:, 0].to_numpy()
kl_slett = kundedata.iloc[:, 1].to_numpy()
varighet = kundedata.iloc[:, 2].to_numpy()
score = kundedata.iloc[:, 3].to_numpy()

# Skriv ut NumPy-arrayene
#print("u_dag:", u_dag)
#print("kl_slett:", kl_slett)
#print("varighet:", varighet)
#print("score:", score)

# Slutt del a
##################################################################################################

# Del b:
# Skriv et program som finner antall henvendelser for hver de 5 ukedagene. Resultatet
# visualiseres ved bruk av et søylediagram (stolpediagram)

# Konverter varighet til timedelta objekter
varighet_timedelta = np.array([timedelta(hours=int(t.split(':')[0]), minutes=int(t.split(':')[1]), seconds=int(t.split(':')[2])) for t in varighet])

# Filtrer varigheter større enn 00:00:00
filter = varighet_timedelta > timedelta(0)
u_dag_filtrert = u_dag[filter]
varighet_filtrert = varighet_timedelta[filter]

# Tell antall henvendelser per dag
unike_dager, antall_henvendelser = np.unique(u_dag_filtrert, return_counts=True)

# Sorter ukedagene i ønsket rekkefølge
rekkefolge = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
rekkefolge_dict = {dag: i for i, dag in enumerate(rekkefolge)}
indekser = [rekkefolge_dict[dag] for dag in unike_dager]
sorterte_indekser = np.argsort(indekser)

unike_dager_sortert = unike_dager[sorterte_indekser]
antall_henvendelser_sortert = antall_henvendelser[sorterte_indekser]

# Lag stolpediagram
plt.bar(unike_dager_sortert, antall_henvendelser_sortert)
plt.xlabel("Ukedag")
plt.ylabel("Antall henvendelser")
plt.title("Antall henvendelser per dag (varighet > 00:00:00)")
plt.show()

# Slutt del b
###################################################################################################

# Del c
# Skriv et program som finner minste og lengste samtaletid som er loggført for uke 24.
# Svaret skrives til skjerm med informativ tekst.

# Finn lengste og korteste samtaletid og tilhørende ukedag
lengste_samtale_index = np.argmax(varighet_filtrert)
korteste_samtale_index = np.argmin(varighet_filtrert)
lengste_samtale = varighet_filtrert[lengste_samtale_index]
korteste_samtale = varighet_filtrert[korteste_samtale_index]
dag_lengste_samtale = u_dag_filtrert[lengste_samtale_index]
dag_korteste_samtale = u_dag_filtrert[korteste_samtale_index]

# Skriv ut lengste og korteste samtaletid med tilhørende ukedag
print("Lengste samtaletid:", lengste_samtale, "på", dag_lengste_samtale)
print("Korteste samtaletid:", korteste_samtale, "på", dag_korteste_samtale)

# Slutt del c
###################################################################################################
# Del d (Denne er ikke ferdig)
# Skriv et program som regner ut gjennomsnittlig samtaletid basert på alle
# henvendelser i uke 24.

# Konverterer tidsstrenger til timedelta objekter
time_deltas = [datetime.strptime(time, "%H:%M:%S") - datetime(1900, 1, 1) for time in varighet]

# Beregner total tid
total_time = sum(time_deltas, timedelta())

# Beregner gjennomsnittlig tid
average_time = total_time / len(time_deltas)

# Formaterer gjennomsnittlig tid tilbake til HH:MM:SS format
average_time_str = str(average_time)
print("Gjennomsnittlig tid:",average_time_str)

#Slutt del d
###################################################################################################
# Del e




#Slutt del e
###################################################################################################
# Del f




#Slutt del f
###################################################################################################