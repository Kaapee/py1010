# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:39:18 2025

@author: Karl Peter Fjørtoft

Arbeidskrav 2 - Oppgave 5 - Beregne dimensjoner
"""
import numpy as np


dimA = 3 #float(input("Skriv inn diameter A:"))
dimB = 5 #float(input("Skriv inn lengde B:"))

radius = dimA / 2

    # Beregner arealet av halvsirkel. Tar formelen for sirkel og ganger med 0.5 pga halvsirkel:
arealHalvSirkel = 0.5 * (np.pi * (radius ** 2))

# print (f"Arealet til halvsirkelen er: {arealHalvSirkel:.2f}")

    # Beregner omkrets av halvsirkel: (fjerner gange med 2 siden vi kun har med halvparten)
omkretsHalvSirkel = (np.pi * radius)

# print (f"Omkretsen til halvsirkelen er: {omkretsHalvSirkel:.2f}")

    # Beregner arealet av trekanten:
arealTrekant = (dimA * dimB) * 0.5

# print (f"Arealet av trekanten er: {arealTrekant:.2f}")

    # Finner hypotenusen til trekanten:
hypotenus = np.hypot(dimA, dimB)

# print (f"Hypotenusen er: {hypotenus:.2f}")


omkretsTrekant = dimB + hypotenus
# print (f"Omkretsen av trekanten er: {omkretsTrekant:.2f}")

totOmkrets = omkretsHalvSirkel + omkretsTrekant
print (f"Omkretsen er: {totOmkrets:.2f}")

totAreal = arealHalvSirkel + arealTrekant
print (f"Arealet er: {totAreal:.2f}")