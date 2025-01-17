# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:03:25 2025

@author: Karl Peter Fjørtoft

Arbeidskrav 2 - Oppgave 6 - Plotting av funksjon
"""

import matplotlib.pyplot as plt
import numpy as np

    # Setter området som skal plottes på x-aksen
x = np.linspace(-10, 10, 200)

    # Setter funksjonen som skal plottes
y = -𝑥*x-5

    # Plotter x og y
plt.plot(x, y)