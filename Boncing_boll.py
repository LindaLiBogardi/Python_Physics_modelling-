# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:19:06 2022

@author: LindaLi
"""

'''define a function to calculate the height of bouncing boll'''

import math

g = 9.82                                      #gravity

#k = 0.85 is the air-resistance parameter 
'''input h is the starting height where you release the boll. 
obs. the height shoud be independent with the m-value '''
def bounce(h, m, k=0.85):
    i = 1
    while i<6: 
        Epot = m * g * h                       #potential energy
        v_before = math.sqrt(2*Epot/m)         #velocity before turning point (highest)
        v_after = k * v_before                 #velocity after
        Ekin = 1/2 * m * v_after**2            #kinetic energy
        h = Ekin/(m * g)                       #bouncing height 
        print(f'Höjden efter {i} studs är:{round(h,2)} m')
        i += 1
        
    return 

