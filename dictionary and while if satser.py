# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 17:57:45 2022

@author: LindaLi
"""

constants = {}                # skapa en tom dictionary
constants['pi'] = 3.141
constants['e'] = 1.602e-19
constants['g'] = 9.82
constants['c'] = 3e8
constants['G'] = 6.673e-11
constants['M'] =5.972e24

print(constants)

#def gravitation(m,M,r):
    #return dict('-1')*m*M/r**2

M = constants['M']
print(M)

#F_G=gravitation(90000,dict('M'),1000)

#print(F_G)


i=None
t_interval=None
while i!='':
    i=input ('Skriv en siffra mellan 0 och 60 (lämna blanket för att avsluta):')
    i = np.float32(i)
    i = i.item()
    if 0<=i<=60:
        
        t_interval=input ('Skriv tidsinterval, ex. 0.5 (0.5 sekunder): obs! tidsintervalen ska vara mindre än i')
                
        t_interval=np.float32(t_interval)
        t_interval=t_interval.item()
        
        #print(i,t_interval)                  #kolla om det är rätt
        #print(type(i),type(t_interval))      
        
        if t_interval>=i:
            print('välj ett tal mindre än',i)
            
        elif t_interval=='':
            t_interval=input ('Skriv tidsinterval, ex. 0.5 (0.5 sekunder): obs! tidsintervalen ska vara mindre än i')
                    
            t_interval=np.float32(t_interval)
            t_interval=t_interval.item()
            print('tja')
        elif t_interval<i:
