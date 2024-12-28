"""
Oppgave 4.4 Stolpediagram
Gitt følgende salgstall (antall enheter solgt): Firma A: 1204, Firma B: 1119, Firma C: 998.
Visualiser dette datasettet ved bruk av et stolpediagram, hvor firmanavn vises langs
x-aksen og salgstallene langs y-aksen
"""
import numpy as np
import matplotlib.pyplot as plt

firma = np.array(["A", "B", "C"])
enheter = np.array([1204, 1119, 998])

plt.barh(firma, enheter)
plt.xlabel("Enheter")
plt.ylabel("Firma")

plt.show()
