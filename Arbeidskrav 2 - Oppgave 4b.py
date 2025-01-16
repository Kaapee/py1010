# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:05:48 2025

@author: Karl Peter Fjørtoft

Arbeidskrav 2 - Oppgave 4a - 
"""


data =      { 
           "Norge": ["Oslo", 0.634], 
           "England": ["London", 8.982], 
           "Frankrike": ["Paris", 2.161], 
           "Italia": ["Roma", 2.873]
            }
    # Ber om input fra brukeren om hvilket land en vil finne info om, og lagrer landet i Land:
Land = input('Skriv inn land:')

    # Skriver ut data om landet:
print( data[Land][0], "er hovedstaden i", Land, "og det er", data[Land][1], "mill. innbyggere i", data[Land][0])