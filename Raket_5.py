# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 14:52:07 2022

@author: LindaLi
"""

#raketens fart och höjd under den första minuten



constants = {}                # skapa en tom dictionary

constants['G'] = 6.673e-11
constants['M'] =5.972e24           #jordens massa
constants['r'] =6.371e6            #jordens radie          

M = constants['M']
G = constants['G']
r_0=constants['r']

                          #mata in ett heltal mellan 0 och 60



def bränsleacceleration(v_br):
    return v_br/1
    

def bränslekraft(delta_m_br,a_br):
    return delta_m_br*a_br
   

   

def raketsmassa(m_0,delta_m_b,t):
    return m_0-delta_m_br*t
       
    

def raket_acceleration(f_bränsle,m_raket):
    return (f_bränsle-m_0*G*M/r**2)/m_raket
    
    
def raket_höjden(a_raket,t):
    return 0.5*a_raket*t**2

def raket_fart(a_raket,t):
    return a_raket*t


#input 
            
m_0=90000                          #fulltankad raket väger 90 ton = 90 000 kg
delta_m_br=1000                    #varje sekund antänds och slungas 1 ton = 1000 kg bränsle
v_br=3000                          #bränslens relativ hastighet i förhålland till raketen
v_raket=0                          #rekets fart vid starten är noll                                       

g=9.82


t=60

for i in range (t+1):
     
    f_br=bränslekraft(delta_m_br,v_br)
    m_raket=raketsmassa(m_0,delta_m_br,i)    #rekets massa, den minskas 1000 kg per sekund
    f_g=m_raket*g                            #raketens tygdkraft från jorden
    a_raket=(f_br-f_g)/m_raket               #rakets acceleration=kraften som orsaker rakets acceleration dividerar rakets massa (tillsammans med bränsle)
                                
    v_raket=v_raket+raket_fart(a_raket,1)    #reketens fart v_raket=reketens hastighet(befintlig fart) + a_raket*1 (accelererad fart under 1 s)
    v_raket_kmh=v_raket*3.6                  #raketens fart i km/h
    h_raket=raket_höjden(a_raket,i)          #raketens höjden i förhålland till jorden, dvs. så hög som raketen har skjutit upp
    h_raket_km=h_raket/1000                  #raketens höjden i km
    r=r_0+h_raket                            #reketens avståndet från jordens kärna
    g=G*M/r**2                               #tygdacceleration
    f_raket=f_br-f_g                         #kraften som orsakar raketens accleleration
    
   
    
    #print(f'tygdacceleration efter {i} s är: {round(g,4)} m/s^2')
    
    #plt.plot(i,g)
    #plt.xlabel("tid (s)")
    #plt.ylabel("g (m/s^2)")
    print (f'raketens höjd efter {i} s är: {round(h_raket)} m')
    #print(f'raketens acceleration efter {i} s är: {round(a_raket,2)} m/s^2')
    print(f'raketens fart efter {i+1}s är: {round(v_raket_kmh,2)} km/h')
    #plt.plot(i,h_raket_km,color='k',markersize=30)
    #print(m_raket)
    #print(type(i))
    #print(i)
    
    



    

    
    


