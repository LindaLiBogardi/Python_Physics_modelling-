# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 21:54:08 2022

@author: LindaLi
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import mu_0, m_e, m_p, e

#mu_0 är magnetic constant (permeabiliteten) mu_0 = 4*np.pi*1e-7 = 1.2566 Vs/Am 
#m_e är elektron mass
#m_p är proton mass
#e är elemental laddning 

#konstanter
k = mu_0/(2*np.pi)  #konstant i magnetiska flödet B

#Funktioner
 
def beräkna_magnetisk_kraft (I, q, vx, vy, m, x, y, x0=0):
    """Beräkna kraften som partikeln med laddningen q känner från ledare med strömmen I. 
    q. Partikeln befinner sig i punkten (x,y). Ledare I är vertikel och har 
    strömen I. I har koordinat x0 = 0, dvs. I är på y-led och går genom origo. vx är partikelns 
    hastighet i x-led. vy är partikelns hastighet i y-led. m är partikelns massa"""
    
    a = x - x0  #avståndet mellan strömledare I (liljal) och partikeln q (punkt)
    B = k*I/a   #Magnetiska flödestätheten, Tesla
    
    Fx = q*vy*B  #magnetisk kraft, riktning av kraften är enligt högerhandsregeln
    Fy = q*vx*B  #magnetisk kraft 
    
    
    return Fx, Fy

'''inbedad värde anges: 
    strömen I (1:a arg),i A
    ladning q (2:a arg),i C
    hastighet vx och vy (3:e resp. 4:e arg) i m/s 
    partikelns massa (5:e arg) i kg, 
    partikelns position x och y (6:e resp. 7:e arg) i meter
    och sista arg är x0=0 som är ledares position'''

Fx, Fy = beräkna_magnetisk_kraft(0.3, e, 3, 2, m_e, -0.03, 0.04, x0=0)

#Fx, Fy = beräkna_magnetisk_kraft(0.3, e, 3, 2, m_p, -0.03, 0.04, x0=0)
#testa om Fx och Fy är beroende av partikelns mass. De bör ej beror på massa 

#Fx, Fy = beräkna_magnetisk_kraft(0.3, e, 3, 2, m_p, -0.03, 0.24, x0=0)
#testa om Fx och Fy är beroende av partikelns position i y-led. De bör ej beror på det 

#Fx, Fy = beräkna_magnetisk_kraft(0.3, e, -3, 2, m_e, -0.03, 0.04, x0=0)
#Fx, Fy = beräkna_magnetisk_kraft(0.3, -e, 3, 2, m_e, -0.03, 0.04, x0=0)
#testa med Fx, Fy riktningar

#print(f'elektron mass är {m_e} kg')
#print(f'elemental laddning är {e} C')
print(f'Fx är {Fx} N')
print(f'Fy är {Fy} N')

