"""
Lag et program som tar r (radius) for ei kule som input fra kommandolinjen og regner ut
overflaten og volumet til kula. Svaret skrives til skjerm. (Vi antar at du finner fram til
formelen for overflate og volum til ei kule.)

"""

import numpy as np
from numpy.ma.core import floor

r = int(input("Hva er radiusen av kula i cm? "))
V = floor((4 / 3) * 3.14 * r**3)
print("Volumet av kula er",V,"cm3")

A = floor(4 * 3.14 * r**2)
print("Arealet av kula er",A,"cm2")
