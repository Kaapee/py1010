# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:23:14 2025

@author: Kaapee
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:05:48 2025

@author: Karl Peter Fjørtoft

Arbeidskrav 2 - Oppgave 4c - Legge til data om nytt land
"""


data =      { 
           "Norge": ["Oslo", 0.634], 
           "England": ["London", 8.982], 
           "Frankrike": ["Paris", 2.161], 
           "Italia": ["Roma", 2.873]
            }

    # Ber om inputs til nytt land:
nyttLand = str (input('Skriv inn navn på nytt land: '))
nyHovedstad = str(input('Skriv inn hovedstad: '))
nyBefolkning = str(input('Skriv inn befolkningstall i millioner innbyggere: '))

    # Legger inn data for nytt land i dictionary "data" med data om det nye landet:
data[nyttLand] = [nyHovedstad, nyBefolkning]


    # For å printe ut innholdet kan en bruke en enkel print, men det ser litt rotete ut:
#   print(data)

    # For løkken henter ut dataen i dictionary, som har key(land) og value(info om hovedstad og befolkning i en tabell) og skriver disse ut med litt beskrivelse og linjebryting
for key, value in data.items():
    print (f" {key} \n Hovedstad: {value[0]} \n Innbyggere: {value[1]} millioner\n")