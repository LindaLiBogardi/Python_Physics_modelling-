# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 22:07:59 2022

@author: LindaLi
"""

#Stirlingmotorn
#pV-diagram

import Termodynamik_4 as Td      
#importera en tidgares programm som ink. b.a. funktionen: beräkna_arbete

import numpy as np
import matplotlib.pyplot as plt  

R=8.31451         # Gaskonstanten (J/mol/K)
n=0.1             #mol 
M=4               #molmassa till helium, enheten är g/mol
V_1=1             #gasens volym före expansion i dm^3
V_2=5             #gasens volym efter expansion i dm^3
T_0=273.15        # 0 grader Celsius i Kelvin
T1=650+T_0        #gasens temperatur under expansion
T2=100+T_0        #gasens temperatur efter värmeöverföring till deplacementkolven
antal_steg=30     #antal punkten data 

#delprocess A: gas expansion med konstant hög temperatur 
#och volym ökar fråm V_1 till V_2 

T=np.zeros(antal_steg)
T_A=T+T1
V_A=np.linspace(V_1,V_2,antal_steg)
p_A=n*R*T_A/V_A
#print (V_A)
#print(T_A)
#plt.plot(V_A,dp_A,color='b')          #test delplot

#delprocess B: konstant (stor) volym, värmebortförsel från gasen till deplacementkolven

V=np.zeros(antal_steg)
V_B=V+V_2         #gasens volym är konstant, och stor
T_B=np.linspace(T1,T2,antal_steg)
p_B=n*R*T_B/V_B

#plt.plot(V_B, p_B, color='r')         #test delplot

#delprocess C: kompression, vid konstant (låg) temperatur

T=np.zeros(antal_steg)
T_C=T+T2           #konstant låg temperatur
V_C=np.linspace(V_2,V_1,antal_steg)
p_C=n*R*T_C/V_C

#print(V_C)

#delprocess D: konstant (liten) volymen, värmetillförsel (från deplacementskolven till gasen)

V_D=V+V_1           #gasens volym är konstant, och liten
T_D=np.linspace(T2,T1,antal_steg)  #värme ökar från låg till hög: värmetillförsel
p_D=n*R*T_D/V_D

#plot

#fig, axs = plt.subplots(4)
#fig.suptitle('gasens tryck-volym (pV) subplots')
#axs[0].plot(dp_A,V_A, color='b')
#axs[1].plot(p_B, V_B, color='r')
#axs[2].plot(p_C, V_C, color='k')
#axs[3].plot(p_D, V_D, color='y')
    

fig, axs = plt.subplots(2, 2, figsize=(15, 8), sharex=False, sharey=False)
axs[0, 0].plot(p_A,V_A)
axs[0, 0].set_title(f'A: expansion, T = {T1} K')
axs[0, 0].set_xlabel('tryck/Pa')
axs[0, 0].set_ylabel('volym/dm^3')

axs[0, 1].plot(p_B, V_B, 'tab:orange')
axs[0, 1].set_title(f'B: värmebortförsel,V = {V_2} dm^3 ')
axs[0, 1].set_xlabel('tryck/Pa')
axs[0, 1].set_ylabel('volym/dm^3')

axs[1, 0].plot(p_C, V_C, 'tab:green')
axs[1, 0].set_title(f'C: kompression, T = {T2} K')
axs[1, 0].set_xlabel('tryck/Pa')
axs[1, 0].set_ylabel('volym/dm^3')

axs[1, 1].plot(p_D, V_D, 'tab:red')
axs[1, 1].set_title(f'D: värmetillförsel, V = {V_1} dm^3')
axs[1, 1].set_xlabel('tryck/Pa')
axs[1, 1].set_ylabel('volym/dm^3')

fig.tight_layout()



W_A=Td.beräkna_arbete(p_A,V_A)
print(f'arbete i process A är {W_A} J')


W_B=Td.beräkna_arbete(p_B,V_B)
print(f'arbete i process B är {W_B} J')


W_C=Td.beräkna_arbete(p_C,V_C)
print(f'arbete i process C är {W_C} J')


W_D=Td.beräkna_arbete(p_D,V_D)
print(f'arbete i process D är {W_D} J')

