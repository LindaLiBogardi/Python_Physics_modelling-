#kastparabal med en vis hojd och kastvinkel samt start hastighet. 
#markera med marken 

import matplotlib.pyplot as plt  
#importera bibliotek som ingar plot-funktion

import numpy as np               
#importera bibliotek som igår nummer osv

import math
#importera matematik som inkluderar b.a. trigonomitriska funktioner som sin och cos

from sympy import symbols, Eq, solve


x0=0
#startpunkten i horisontel riktningen 

y0=2
#startpunkten i vertikal riktning, dvs. starthoejden aer 2 meter över marknivån

y1=1
#startpunkten med hojden 1 m

v0=11
#utgaengsfarten aer 11 m/s

v1=12
#utgaengsfarten aer 12 m/s

pi=np.pi    #definiera pi
a0=pi/6
#utgaengsvinkel aer 30 grader, dvs. pi/6 i radien 
a1=pi/4
#utgaengsvinkel aer 45 grader
g=9.82
#tyngdaccelaration 

#losa ekvation da yt0, yt1 som funktion till tiden t sa att yt0=0 och yt1=0. dvs. tilden da foremalet nar marken
t = symbols('t')
eq0 = Eq(2+11*math.sin(a0)*t-(9.82*t**2)/2,0)
eq1 = Eq(1+12*math.sin(a1)*t-(9.82*t**2)/2,0)

solt0 = solve(eq0)
print('hej yt0 parabol nar marken vid tiden:')
print(solt0)

solt1 = solve(eq1)
print('hej yt1 parabol nar marken vid tiden:')
print(solt1)

for i in solt0:
    if i>0:
        print(i)
        t0max = np.float32(i)
        pyt0max = t0max.item()
        
        print(pyt0max)
        print(type(t0max))
    
        
for i in solt1:
    if i>0:
        t1max = np.float32(i)
        pyt1max = t1max.item()
        
        print(pyt1max)
        print(type(t1max))
       

#mata in tiden da foremalet nar marken i t0 och t1
t0=np.linspace(0,pyt0max,20)
t1=np.linspace(0,pyt1max,20)

xt0=x0+v0*math.cos(a0)*t0
yt0=y0+v0*math.sin(a0)*t0-(g*t0**2)/2
#kastlaengden xt0 och hojden yt0 som funktion till tiden t
xt1=x0+v1*math.cos(a1)*t1
yt1=y1+v1*math.sin(a1)*t1-(g*t1**2)/2
#kastlaengden xt1 och hojden yt1 som funktion till tiden t

#plota kasthojden som en funktion till kastl�ngden samt marken
plt.plot(xt0,yt0, color='b', label='2m, 11m/s,pi/6')
plt.plot(xt1,yt1,color='k', linestyle=':',label='1m, 12m/s, pi/4')
plt.xlabel("length (m)")
plt.ylabel("hight (m)")
plt.axhline(y=0, color='r', linestyle='-')  

plt.axis('equal')
plt.legend()