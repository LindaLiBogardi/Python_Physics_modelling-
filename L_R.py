# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 14:11:16 2022

@author: LindaLi
"""

import matplotlib.pyplot as plt
import numpy as np

t, I=np.loadtxt('ström_i_spole.txt', comments='#',unpack=True)
t=t/1e3    #i s
I=I/1e3    #i A

#antal=len(I)
#print(antal)

#U=np.zeros(antal)+9    #Volt, skapa en array med lika lång element som t och I
#print(len(U))

U=9    #Volt
#U=-L*deltaI/delta_t

dI_dt=np.gradient(I, t)    #beräkna deltaI/delta_t
L=U/dI_dt[0]
R=U/I[-1]
print(f'Spolens induktans: {L:.3f} H')
print(f'Spolens resistans:{R:.3f} Ohm')

#beräkna hur mycket effekt som utvecklas i spolen 
P=U*I

#beräkna hur mycket energi som utvecklas genom att integrera P(t)
E=np.trapz(P,x=t)
print(f'utvecklad energi:{E:.3e} J')

#plota t-I 
plt.close('all')
plt.figure()
plt.plot(t,I)
plt.xlabel('tid(s)')
plt.ylabel('ström (A)')

#plot t- dI/dt
plt.figure()
plt.plot(t,dI_dt)
plt.xlabel('tid(s)')
plt.ylabel('dI/dt (A/S)')