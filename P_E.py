# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:45:54 2022

@author: LindaLi
"""

import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

#input-parametrar 
Imax=4       #A
R=75         #Ohm
delta_t=0.1  #s
f=50.0       #frekvens i Hz

#generat an array of time intervall
t=np.linspace(0,delta_t,1000)  
I=Imax*np.sin(2*np.pi*f*t)

#beräkna effekt (W)
P=R*I**2

plt.figure()
plt.plot(t,P)
plt.xlabel('tid (s)')
plt.ylabel('effekt (W)')

#Energi är integral av effekt genom tiden
E=np.trapz(P,x=t)
print(f'energi (numeriskt) : {E:3e} (J)')

#jämför energin med det förväntade värdet 
P_medel=R*Imax**2/2.0
E_medel=P_medel*delta_t
print(f'energi (förväntad):{E_medel:.3e}(J)')
