# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:50:51 2022

@author: LindaLi
"""

import matplotlib.pyplot as plt
import numpy as np


# Konstanter
R = 8.31451                     # Gaskonstanten (J/mol/K)
T0 = 273.15                     # 0 grader Celsius i Kelvin
M_N2 = 2*14/1e3                 # Molmassa för kvävgas (kg/mol)
M_O2 = 2*16/1e3                 # Molmassa för syrgas (kg/mol)
M_luft = 0.8*M_N2 + 0.2*M_O2    # Molmassa för luft (kg/mol)


# Funktioner

def beräkna_arbete(p, V):
    """Beräkna volymändringsarbetet för en process när trycket p och 
    volymen V varierar enligt de givna arrayerna."""
    
    dV = V[1:] - V[:-1]
    p_mitt = (p[1:] + p[:-1]) / 2.0
    dW = p_mitt * dV
    W = np.sum(dW)
    
    return W

# Huvudprogram
# ------------

# Input
V_före = 1.0          # m**3
V_efter = 2.0         # m**3 
T = 20 + T0           # K
m = 5.0               # kg

antal_steg = 20

# Beräkna hur många mol luft vi har
n=m/M_luft

# Skapa p och V för den givna processen med hjälp av ideala gaslagen
V=np.linspace(V_före,V_efter,antal_steg)
p=n*R*T/V

# Beräkna volymändringsarbetet
W=beräkna_arbete(p,V)

# Skriv ut resultatet
#print(f'arbete är W/1e3')