# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 21:11:26 2022

@author: LindaLi
"""

#raketens acceleration, raketens kraft, bränslens kraft under den första sekunden


import numpy as np 


i=5                          #ett antal bränsleshastighet mellan 0 och 3000 m/s
v_br=np.linspace(0,3000,i)   #skapa en array av bränsleshastighet
print ('bränslens hastigheten är: ' ,v_br, 'm/s')
m_i=np.zeros(i)        #skapa en array i samma dimension som antal bränsleshastigheten
m_noll=m_i+90000       #fulltankad raket 90 ton, dvs. 90000 kg
print('fulltankad raket väger:',m_noll, 'kg')

m_br=np.zeros(i)      #skapa en array i samma dimension som antalet bränsleshastigheten
delta_br=m_br+1000    #bränsle antänds och slungas 1 ton, dvs. 1000 kg per sekund
print('bränslen antänds och slungas:',delta_br,'kg per sekund')

g=9.82                #tydgacceleration på jordens yta, dvs. när raketen tänds


def Newton3(F,m):
    return F/m

def raketens_massa (t):
    return m_noll-delta_br*t

def br_acceleration(v_br):
    return v_br/1


a_br=br_acceleration(v_br)        #bränslens acceleration 
m_ra=raketens_massa(1)            #raketens massa efter 1 sekund

print('raketens massa efter 1 sekund är:', m_ra, 'kg')

def br_kraft(delta_br,a_br):
    return delta_br*a_br

f_br=br_kraft(delta_br,a_br)

print('bränslens kraft är:',f_br,'N')

def raketens_kraft(delta_br,a_br):
    return f_br-m_ra*g

f_raket=raketens_kraft(delta_br, a_br)

print('raketens kraft är:',f_raket,'N')

def raketens_acceleration(f_raket,m_ra):
    return Newton3(f_raket,m_ra)

a_raket=raketens_acceleration(f_raket,m_ra)

print('raketens acceleration är:',a_raket,'m/s^2')


