"""
Oppgave 4.6 Kakediagram
Gjenbruk dataen oppgitt i oppgave 4.4, men visualiser n ̊a datasettet ved bruk av et
kakediagram (sektordiagram). ≪Kakestykkene≫ fremst ̊ar her som forholdsvis like, s ̊a det er
ogs ̊a ønskelig  ̊a visualisere prosentandelen hvert kakestykke utgjør. Hint: autopct =
’%1.1f%%.
157
"""
import numpy as np
import matplotlib.pyplot as plt

firma = ["A", "B", "C"]
enheter = [1204, 1119, 998]

plt.pie(enheter, labels=firma, autopct='%1.1f%%')
plt.title("Firmaresultater")
plt.show()


