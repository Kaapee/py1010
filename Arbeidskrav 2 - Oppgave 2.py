# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:06:15 2025

@author: Karl Peter Fjørtoft

Arbeidskrav 2 - Oppgave 2 - Antall pizzaer

"""
import numpy as np

    # Ber om antallet elever:
antall_elever = int(input('Skriv inn antall elever:' ))

    # Setter antallet pizza per elev som 1/4, da går det an å utvikle programmet vidare med forskjellige størrelse pizza:
antall_pizza_per_elev = 0.25

    # Beregner nøyaktig antall pizzaer med desimaler:
antall_pizza_desimal = antall_elever * antall_pizza_per_elev

    # Numpy ceil funksjonen runder opp til nermeste heltall. Siden beregningen står inne i int() unngår en desimaler som heltall:
antall_pizza = int(np.ceil(antall_pizza_desimal))

    # Printer ut antall pizza som må bestilles:
print("Det må bestilles" , antall_pizza)
