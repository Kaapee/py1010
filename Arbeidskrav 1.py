# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:36:43 2024

@author: Karl Peter Fjørtoft

Første arbeidskrav i py1010
"""

# I dette programmet skal eg sammenligne kostnader mellom kjøp av elbil og bensinbil

# Steg 1 er å finne antall km kjørt per år. Antar 10.000km/år

kjoreLengde = 10000

# Skriver ut kjørelengden
print("Årlig kjørelengde er:", kjoreLengde,"km per år")

# Legger inn variabel for pris drivstoff per km, da er det enklere å evt endre seinare
ElDrivstoff =  0.2 * 2.0

BensinDrivstoff = 1.0

# Legger inn variabel for pris forsikringer
ElForsikring = 5000

BensinForsikring = 7500

# Legger inn variabler for pris bomavgift per km
ElBomKm = 0.1

BensinBomKm = 0.3

# Beregner pris per km for elbil:
# Gjør om tall til int (heltall) for å slippe desimaler
drivstoffEl = int(kjoreLengde *ElDrivstoff)
drivstoffBensin = int(kjoreLengde *BensinDrivstoff)

# Skriver ut drivstoffkostnader
print("")
print ("Drivstoffkostnader per år:")
print ("Pris elektrisitet:",drivstoffEl, "kr")
print ("Pris bensin: ",drivstoffBensin, "kr")

# Beregner årlig trafikkforsikringsavgift, felles for begge
trAvgift = int(365 * 8.38) 

# Skriver ut årlig trafikkforsikringsavgift
print("")
print("Årlig trafikkforsikringsavgift, felles for begge typer:", trAvgift, "kr")

# Beregner årlig bomavgift
ElBomTot = int(kjoreLengde * ElBomKm)

BensinBomTot = int(kjoreLengde * BensinBomKm)

# Skriver ut bompengepriser
print("")
print("Bompenger per år:")
print("Elbil:", ElBomTot,"kr")
print("Bensinbil:", BensinBomTot,"kr")

# Beregner totalpris per år

ElTotalKost = int(drivstoffEl + trAvgift + ElBomTot)

BensinTotalKost = int(drivstoffBensin + trAvgift + BensinBomTot)

# Skriver ut totalkostnad
print("")
print("Totalkostnad per år:")
print("Elbil:", ElTotalKost,"kr")
print("Bensinbil:", BensinTotalKost,"kr")

# Beregner prisdifferanse (bruke abs for å få absoluttverdi, uavhengig av hvilken som er størst)
prisDiff = abs(BensinTotalKost - ElTotalKost)

# Skriver ut prisdifferansen
print("")
print("Prisdifferansen er:", prisDiff,"kr")