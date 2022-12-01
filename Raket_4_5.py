# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:14:08 2022

@author: LindaLi
"""

import matplotlib.pyplot as plt  
#importera bibliotek som ingar plot-funktion

import numpy as np               
#importera bibliotek som igar nummer osv

constants = {}                # skapa en tom dictionary

constants['G'] = 6.673e-11         #gravitationskonstant i Newtons law of universal gravatation
constants['M'] =5.972e24           #jordens massa
constants['r'] =6.371e6            #jordens radie          

G = constants['G']
M = constants['M']
r_0=constants['r']

                          #mata in ett heltal mellan 0 och 60



def bränsleacceleration(v_br):
    return v_br/1
    

def bränslekraft(delta_m_br,a_br):
    return delta_m_br*a_br
   

   

def raketsmassa(m_0,delta_m_b,t):
    return m_0-delta_m_br*t
       

def raket_acceleration(f_bränsle,r,m_raket):
    return (f_bränsle-m_raket*G*M/r**2)/m_raket
    
    
def raket_höjden_acceleration(a_raket,t):         #under acceleration i t (tid) har raketen åkt så lång 
    return 0.5*a_raket*t**2

def raket_fart_acceleration(a_raket,t):           #raketens fart har ökat så mycket under t (tid) med acceleration
    return a_raket*t


#input 
            
m_0=90000                          #fulltankad raket väger 90 ton = 90 000 kg
delta_m_br=1000                    #varje sekund antänds och slungas 1 ton = 1000 kg bränsle
v_br=3000                          #bränslens relativ hastighet i förhålland till raketen
v_raket=0                          #rekets fart vid starten är noll                                       
h_raket=0                            #vid starten, rakethöjden är noll

g=9.82

t=1
a_range = np.arange(0,59.1,t)        #första minut, alltså 60 sekunder, med t interval 
#print(a_range)

totalITarray = []
aArray =[]
for i in a_range:
     
    f_br=bränslekraft(delta_m_br,v_br)
    m_raket=raketsmassa(m_0,delta_m_br,i)    #rekets massa, den minskas 1000 kg per sekund
    f_g=m_raket*g                            #raketens tygdkraft från jorden
    a_raket=(f_br-f_g)/m_raket               #rakets acceleration=kraften som orsaker rakets acceleration dividerar rakets massa (tillsammans med bränsle)
                                
    v_raket=v_raket+raket_fart_acceleration(a_raket,t)    #reketens fart v_raket=reketens hastighet(befintlig fart) + a_raket*1 (accelererad fart under 1 s)
    v_raket_kmh=v_raket*3.6                               #raketens fart i km/h
    
    h_raket=h_raket+v_raket*t+raket_höjden_acceleration(a_raket,t)          
    #raketens höjden i förhålland till jorden, dvs. så hög som raketen har skjutit upp
    
    h_raket_km=h_raket/1000                  #raketens höjden i km
    
    r=r_0+h_raket                            #reketens avståndet från jordens kärna
    g=G*M/r**2                               #tygdacceleration
    f_raket=f_br-f_g                         #kraften som orsakar raketens accleleration
    
    totalITarray.append(i+t)
    aArray.append(a_raket)
    #print(f'tygdacceleration efter {i+t} s är: {round(g,2)} m/s^2')
    #print(i+t)
    #print(g)
    #print(type(g))
    #print(type([1,2,3]))

    #for i in min(i+t):
    #    print(i)
        

   
    #plt.xlabel("tid (s)")
    #plt.ylabel("g (m/s^2)")
    print (f'raketens höjd efter {i+t} s är: {round(h_raket)} m')
    print(f'raketens acceleration efter {i+t} s är: {round(a_raket,2)} m/s^2')
    print(f'raketens fart efter {i+t}s är: {round(v_raket,2)} m/s')
    
    
    
plt.plot(totalITarray,aArray, color='b')