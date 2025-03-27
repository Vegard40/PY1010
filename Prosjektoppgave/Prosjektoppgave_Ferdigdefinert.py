#Importerer pandas, matplotlib, timedelta, og numpy for blant annet å kunne lese inn kildefil og lage plot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Del a
# Oppgavetekst:
#Skriv et program som leser inn filen ‘support_uke_24.xlsx’ og lagrer data fra kolonne 1
#i en array med variablenavn ‘u_dag’, dataen i kolonne 2 lagres i arrayen ‘kl_slett’, data i
#kolonne 3 lagres i arrayen ‘varighet’ og dataen i kolonne 4 lagres i arrayen ‘score’. Merk:
#filen ‘support_uke_24.xlsx’ må ligge i samme mappe som Python-programmet ditt.

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
# Oppgavetekst:
# Skriv et program som finner antall henvendelser for hver de 5 ukedagene. Resultatet
# visualiseres ved bruk av et søylediagram (stolpediagram)

# Konverter varighet til timedelta objekter
varighet_timedelta = np.array([timedelta(hours=int(t.split(':')[0]), minutes=int(t.split(':')[1]), seconds=int(t.split(':')[2])) for t in varighet])

# Filtrerer varigheter større enn 00:00:00
filter = varighet_timedelta > timedelta(0)
u_dag_filtrert = u_dag[filter]
varighet_filtrert = varighet_timedelta[filter]

# Teller antall henvendelser per dag
unike_dager, antall_henvendelser = np.unique(u_dag_filtrert, return_counts=True)

# Sorter ukedagene i ønsket rekkefølge
rekkefolge = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
rekkefolge_dict = {dag: i for i, dag in enumerate(rekkefolge)}
indekser = [rekkefolge_dict[dag] for dag in unike_dager]
sorterte_indekser = np.argsort(indekser)

unike_dager_sortert = unike_dager[sorterte_indekser]
antall_henvendelser_sortert = antall_henvendelser[sorterte_indekser]

# Lager et stolpediagram
plt.bar(unike_dager_sortert, antall_henvendelser_sortert)
plt.xlabel("Ukedag")
plt.ylabel("Antall henvendelser")
plt.title("Antall henvendelser per dag (varighet > 00:00:00)")
plt.show()

# Slutt del b
###################################################################################################

# Del c
# Oppgavetekst:
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
print("Lengste samtaletid for inneværende uke er klokka", lengste_samtale, "på", dag_lengste_samtale)
print("Korteste samtaletid for inneværende uke er klokka", korteste_samtale, "på", dag_korteste_samtale)

# Slutt del c
###################################################################################################
# Del d
# Oppgavetekst:
# Skriv et program som regner ut gjennomsnittlig samtaletid basert på alle
# henvendelser i uke 24.

# Leser Excel-filen og antar at den første raden er kolonnenavn
df = pd.read_excel(kildefil)

# Konverter "Varighet"-kolonnen til timedelta
df["Varighet"] = pd.to_timedelta(df["Varighet"])

# Beregne gjennomsnittlig varighet, og begrenser oppløsning til å vise hele sekunder (.round('s'))
gjennomsnitt_varighet = df["Varighet"].mean().round('s')

# Konverter gjennomsnittet til lesbart format (HH:MM:SS)
gjennomsnitt_tid = str(gjennomsnitt_varighet).split()[2]

# Vise resultat
print("Gjennomsnittlig varighet for samtaletid inneværende uke er", gjennomsnitt_tid)

#Slutt del d
###################################################################################################
# Del e
# Oppgavetekst:
# Supportvaktene i MORSE er delt inn i 2-timers bolker: kl 08-10, kl 10-12, kl 12-14 og kl
# 14-16. Skriv et program som finner det totale antall henvendelser supportavdelingen mottok
# for hver av tidsrommene 08-10, 10-12, 12-14 og 14-16 for uke 24. Resultatet visualiseres ved
# bruk av et sektordiagram (kakediagram).

# Konverter kolonne Klokkeslett til datetime-format
df['Klokkeslett'] = pd.to_datetime(df['Klokkeslett'], format='%H:%M:%S').dt.time

# Definer tidsrommene
tidsrom = {
    '08-10': (pd.to_datetime('08:00:00').time(), pd.to_datetime('10:00:00').time()),
    '10-12': (pd.to_datetime('10:00:00').time(), pd.to_datetime('12:00:00').time()),
    '12-14': (pd.to_datetime('12:00:00').time(), pd.to_datetime('14:00:00').time()),
    '14-16': (pd.to_datetime('14:00:00').time(), pd.to_datetime('16:00:00').time())
}

# Teller antall hendelser i hvert tidsrom
hendelser = {}
for key, (start, end) in tidsrom.items():
    hendelser[key] = df[(df['Klokkeslett'] >= start) & (df['Klokkeslett'] < end)].shape[0]

# Visualiserer resultatet med et kakediagram
labels1 = hendelser.keys()
sizes1 = hendelser.values()
colors1 = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode1 = (0.1, 0, 0, 0)  # uthever første tidsrommet

plt.pie(sizes1, explode=explode1, labels=labels1, colors=colors1, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.axis('equal')  # Like forhold mellom aksene
plt.title('Antall hendelser per tidsrom')
plt.show()

#Slutt del e
###################################################################################################
# Del f
# Oppgavetekst:
# Kundens tilfredshet loggføres som tall fra 1-10 hvor 1 indikerer svært misfornøyd og
# 10 indikerer svært fornøyd. Disse tilbakemeldingene skal så overføres til NPS-systemet (Net
# Promoter Score).
# NPS-systemet er konstruert på følgende måte:
# Score 1-6 oppfattes som at kunden er negativ (vil trolig ikke anbefale MORSE til andre).Score 7-8 oppfattes som et nøytralt svar.
# Score 9-10 oppfattes som at kunden er positiv (vil trolig anbefale MORSE til andre).
# Supportavdelingens NPS beregnes som et tall, prosentandelen positive kunder minus
# prosentandelen negative kunder. Ved en formel kan dette gis slik:
# NPS = % positive kunder - % negative kunder
# Lag et program som regner ut supportavdelings NPS og skriver svaret til skjerm. Merk:
# Kunder som ikke har gitt tilbakemelding på tilfredshet, skal utelates fra utregningene.

# Fjern rader med manglende tilfredshetsverdier
tilfr_het = df.dropna(subset=['Tilfredshet']).copy()

# Konverter kolonne Klokkeslett til datetime-format
tilfr_het['Klokkeslett'] = pd.to_datetime(tilfr_het['Klokkeslett'], format='%H:%M:%S').dt.time

# Funksjon for å tolke tilfredshetsverdier
def tolk_tilfredshet(verdi):
    if 1 <= verdi <= 6:
        return 'Negativ'
    elif 7 <= verdi <= 8:
        return 'Nøytral'
    elif 9 <= verdi <= 10:
        return 'Positiv'
    else:
        return 'Ukjent'

# Bruk funksjonen på kolonnen Tilfredshet
tilfr_het['Tolket'] = tilfr_het['Tilfredshet'].apply(tolk_tilfredshet)

# Tell totalt antall positive og negative hendelser
positive = tilfr_het[tilfr_het['Tolket'] == 'Positiv'].shape[0]
nøytrale = tilfr_het[tilfr_het['Tolket'] == 'Nøytral'].shape[0]
negative = tilfr_het[tilfr_het['Tolket'] == 'Negativ'].shape[0]
total = tilfr_het.shape[0]

# Beregn den totale NPS verdien
nps = ((positive / total) - (negative / total)) * 100 if total > 0 else 0

# Skriv ut resultatet til skjermen
print(f"NPS for inneværende uke er {nps:.2f}")

# Beregn total NPS
nps = ((positive - negative) / total) * 100 if total > 0 else 0

# Lager et kakediagram likt det som er presentert på blueprnt.com
labels2 = ['Positiv', 'Nøytral', 'Negativ']
sizes2 = [positive, nøytrale, negative]
colors2 = ['#4CAF50', '#FFC107', '#F44336']  # Grønn, gul og rød
explode2 = (0.1, 0, 0)

# Opprett kakediagrammet
plt.pie(sizes2, explode=explode2, labels=labels2, colors=colors2, autopct='%1.1f%%',
        shadow=True, startangle=90)

# Legg total NPS som tekst i midten
plt.text(0, 0, f'NPS\n{nps:.1f}%', ha='center', va='center', fontsize=16, fontweight='bold', zorder=11)

# Vis diagrammet
plt.title('Net Promoter Score', fontsize=20, fontweight='bold')
plt.show()

#Slutt del f
###################################################################################################
