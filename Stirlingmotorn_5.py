# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:25:11 2022

@author: LindaLi
"""



import numpy as np
import matplotlib.pyplot as plt  

antal_intervall=10 
R=np.zeros(antal_intervall)+8.31451         # Gaskonstanten (J/mol/K)
n=np.zeros(antal_intervall)+0.1             #mol 
V_1=1             #gasens volym före expansion i dm^3
V_2=5             #gasens volym efter expansion i dm^3

T_0=273.15
T_H1=200+T_0           #max temp start 
T_H2=650+T_0          #max temp slut 
               

T_H=np.linspace(T_H1, T_H2,antal_intervall)  #max temp array

T_L=np.zeros(antal_intervall)+100+T_0    #minsta temp array

V_A=np.linspace(V_1,V_2,antal_intervall)
p_A=n*R*T_H/V_A

#print(W_A)
#print(p_A)

V_C=np.linspace(V_2,V_1,antal_intervall)
p_C=n*R*T_L/V_C

#print(V_C)
#print(p_C)

def beräkna_arbete(p,V):
    return p*V

W_A=beräkna_arbete(p_A,V_A)
W_C=beräkna_arbete(p_C,V_C)

W_ut=W_A     #W_ut är arbetet som utförs vid expansionen
W_in=W_C   #W_in är arbetet som krävs för kompressionen
Q_in=W_ut          #Q_in är den värmemängd som tillförs vid expansionen
                   #vid expansion, alltså process A, är temperaturen konatan
                   #då U=0, och W=Q

#print(W_C)                   

def beräkna_verkningsgrad(W_ut, W_in, Q_in):
    return (W_ut-W_in)/Q_in

eta=beräkna_verkningsgrad(W_ut, W_in, Q_in)

print(f'verkningsgrader är: {eta}')



def beräkna_verkningsgrad_max(T_H, T_L):
    return (T_H-T_L)/T_H

eta_max=beräkna_verkningsgrad_max(T_H, T_L)

print(f'maximal verkningsgrader är: {eta_max}')

plt.plot(T_H,eta,color='r',linestyle='-', label='eta')
plt.plot(T_H,eta_max,color='b',linestyle=':', label='max eta')
plt.xlabel("högsta temp")
plt.ylabel("verkningsgrad eta")

print(f'p_A är:{p_A} Pa')
print(f'V_A är: {V_A} dm^3')
print(f'arbetet i A (isotor) är:{W_A} J')

print(f'p_C är:{p_C} Pa')
print(f'V_C är: {V_C} dm^3')
print(f'arbetet i C (isotor) är: {W_C} J')