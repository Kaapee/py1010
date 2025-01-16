# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:48:59 2025

@author: Karl Peter Fjørtoft

Arbeidskrav 2 - Oppgave 3 - Omregning fra grader til radianer

"""

import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))

v_rad = v_grad*np.pi/180

v_rad_3des = round(v_rad, 3)
    # Runder radian-vinkelen ned til 3 desimaler
    
print("Vinkelen er : " ,v_rad_3des, "rad")
