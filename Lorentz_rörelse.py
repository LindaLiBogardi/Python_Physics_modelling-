# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:17:35 2022

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
    
    Fx = -q*vy*B  #magnetisk kraft, riktning av kraften är enligt högerhandsregeln
    Fy = -q*vx*B  #magnetisk kraft 
    
    
    return Fx, Fy

'''inbedad värde anges: 
    strömen I (1:a arg),i A
    ladning q (2:a arg),i C
    hastighet vx och vy (3:e resp. 4:e arg) i m/s 
    partikelns massa (5:e arg) i kg, 
    partikelns position x och y (6:e resp. 7:e arg) i meter
    och sista arg är x0=0 som är ledares position'''

Fx, Fy = beräkna_magnetisk_kraft(0.3, e, 3, 2, m_p, -3e-6, 4e-6, x0=0)

#Fx, Fy = beräkna_magnetisk_kraft(0.3, e, 3, 2, m_p, -3e-6, 4e-6, x0=0)
#testa om Fx och Fy är beroende av partikelns mass. De bör ej beror på massa 

#Fx, Fy = beräkna_magnetisk_kraft(0.3, e, 3, 2, m_p, -3e-6, 24e-6, x0=0)
#testa om Fx och Fy är beroende av partikelns position i y-led. De bör ej beror på det 

#Fx, Fy = beräkna_magnetisk_kraft(0.3, e, -3, 2, m_e, -3e-6, 4e-6, x0=0)
#Fx, Fy = beräkna_magnetisk_kraft(0.3, -e, 3, 2, m_e, -3e-6, 4e-6, x0=0)
#testa med Fx, Fy riktningar

#print(f'elektron mass är {m_e} kg')
#print(f'elemental laddning är {e} C')
print(f'Fx är {Fx} N')
print(f'Fy är {Fy} N')

#rita en koordinatsystem med x, y-axlar, gränsvärde är -6 och 6
nx = 10
ny = 11
x_axel = np.linspace(-8, 8, nx)    
y_axel = np.linspace(-8, 8, ny)
'''se till att partikeln befinner sig mellan/in i gränsvärde
   enheterna i x och y-led är anpassad till partikelns position i förhålland till ledaren
   i vårt fall befinner partikeln i (-3e-6, 4e-6) är x_axel och y_axel i mikrometer''' 

'''nu startar vi plot sektionen'''

#loopen som ritar magnetisk fält
for x in x_axel:
    for y in y_axel:
        #print(f'{x},{y}')
        
        if x != 0:
            marker =  'o' if x < 0 else 'x'
            plt.plot(x, y, color = 'b', marker = marker)

#rita ledare som en vertikel linje i x = 0
plt.axvline(x=0, linestyle='--',color = 'r')


#rita strömens riktning som en pil
plt.arrow(0, 0, 0, 1, width = 0.08, head_width = 0.4, head_length = 0.4, color = 'r')

#rita partikelns postion i magnetisk fält 
plt.plot(-3, 4, color = 'r', marker = 'p')


'''Vi antar att Lorentzkraften är den enda relevanta kraften som verkar på partikeln, 
dvs. tyngdkraft, luftmotstånd etc kan försummas'''
#beräkna nya värden på partikelns hastighet och position
'''partikelns start positin är (x0, y0)'''
x = -3e-6                     # m
y = 4e-6                      # m 

nt = 10                      #antal tidsintervall                    

vx = 3                      # m/s
vy = 2                      # m/s

m = m_p                     #partikeln är en proton 

def beräkna_hastigheter_och_position (x, y, vx, vy, Fx, Fy, nt, m):
    '''x och y är partikelns läge
    dt är tidsinterval 
    '''
    
    t0 = 0     #start tid
    
    for i in range(nt):
        ax = Fx/m         #acceleration i x-led
        ay = Fy/m         #acceleration i y-led
        
        
        dt = np.linspace(0,4,nt)    #tidsintervall, vid t = 0 befinner partikeln i (x0, y0), enhet: s
        t = t0 + dt[i]
        
        x = x + vx*t    #nya position efter dt, 
        y = y + vy*t
        
        vx = vx + ax*t   #nya hastigheter
        vy = vy + ay*t
        
        Fx, Fy = beräkna_magnetisk_kraft(0.3, e, vx, vy, m_p, x, y, x0=0)
        
    
        
    return x, y, Fx, Fy, vx, vy
        
        
x, y, Fx, Fy, vx, vy = beräkna_hastigheter_och_position(x, y, -3, 2, Fx, Fy, nt, m_p)
print(f'partikelns nya position är: ({x},{y}), hastigheter är vx ={vx}, vy = {vy}')   
    













