# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:24:06 2022

@author: LindaLi
"""

import matplotlib.pyplot as plt
import numpy as np

N=200    #antal varv i spole

t, phi=np.loadtxt('flöde_i_spole.txt', comments='#',unpack=True)
phi=phi/1e3

dphi_dt=np.gradient(phi, t)    #beräkna derivata 

U=-N*dphi_dt       #spänning i V

plt.close('all')
plt.plot(t,U)