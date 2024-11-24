"""
Finn informasjon om numpy-funksjonene ceil og floor. Skriv en kort forklaring, og vis ved et
kort kodeeksempel hva disse funksjonen gjør.

Numpy Ceil og floor er funksjoner for å avrunde verdier henholdsvis opp og ned.

"""
import numpy as np
# En tilfeldig tallverdi
tallverdi = 56.45

# Avrunder opp
res_opp = np.ceil(tallverdi)
print(res_opp)

#avrunder ned
res_ned = np.floor(tallverdi)
print(res_ned)
