"""
Et objekt forflytter seg langs en rett linje, og hvert andre sekund m ̊aler vi avstanden
objektet har forflyttet seg (siden forrige m ̊aling). Disse m ̊alingene ligger lagret i variabelen

S = np.array([1.05, 1.30, 1.10, 0.94, 1.21])

Hvert element i S gir strekningen objektet har forflyttet seg i løpet av to sekunder, dvs. de
to første sekundene forflyttet objektet seg 1,05 m, de neste to sekundene nye 1,30 m osv.
Ved konstant fart gjelder formelen v = s/t der s [m] er strekning og t [s] er tid.

Lag en funksjon som tar S og t som innargumenter, regner ut den gjennomsnittlige farten og
returnerer svaret som skrives til skjerm. Tenk gjennom hvilken verdi du vil gi variabelen t.
"""

