# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:14:45 2024

@author: ligia
"""

import numpy as np
#import matplotlib.pyplot as plt
#import math as mt

#%%
#Eksempel fra boka (8.1)

A = np.array([5, 10, 15, 20])
k = 0

for E in A:
    print('k =', k)
    k += 1 
    print('E =', E)
    print('-----------------')

print('Dette er foerste kodelinje etter for-loekken.')

"""
- For-løkken itererer like mange ganger som det er elementer i arrayen A
- For hver iterasjon av løkken kan vi aksessere elementet (E) i arrayen (A). I eksempelet over brukes print
til å vise verdien av E i konsollen
"""

#%%
# Meg som tester ut for og while løkker

for e in range (0,5): #Dette programmet vil kun kjøre 5 ganger
    print("dette er", e, ". gangen programmet kjører")
    
b = float(input("SKriv inn et tall:\n"))

while b > 12:
    print("Dette programmet vil fortsette til bruker endrer verdien til b til noe som gir et usant utslag")
    b = float(input("Skriv inn ny verdi for b:\n"))
    
#Gotta love python omd, alt bare gir mening

#%%
#Oppgave 8.1

for f in range (5,36):
    print(f)
    
    
#%%
#Oppgave 8.2

for l in range(105,37, -1):
    print(l)
    
#%%
#Oppgave 8.3

svar = 0

for p in range (14, 109, +2):
    svar += p
    
print("totalt sum av alle partallene =", svar)

#%%
#Oppgave 8.4

for g in range (5, 36):
    if g == 24:
        print("Tjuefire")
    else:
        print(g)

#%%
#Oppgave 8.5

arr = np.zeros(31)

for a in range (5,36):
    arr[a-5] = 1/a

    
print("arr =", arr)

#%%
#Oppgave 8.6

def f(x):
    return np.sin(x)

A = np.linspace(0, np.pi, 20)

for b in A :
    print ("b =", round(b,2), "og f(b) =", round(f(b), 2))
    
#%%
# Oppgave 8.7

def my_linspace(start,stopp):
    if start < stopp:
        antall = 50
        dx = (stopp-start)/(antall-1)
        x1 = start
        arr = np.zeros(antall)

        for i in range(0, antall):
            arr[i] = x1
            x1 = x1+dx
    else:
        print("Du må skrive inn en verdi som gjør at start < stopp")
        
    
    return arr

print('fasit =', np.linspace(1, 7))
print('my_linspace =', my_linspace(1, 7))

#%%
# Oppgave 8.8
# del-oppgave A

def funk(x):
    return (x**2)+1

for b in range (-2,2):
    print("svaret er", funk(b))

# del-oppgave B (svaret var nei men jeg kopierte fasiten)

def f(x):
    return (x**2)+1

dx = 0.1 
x_array = np.arrange 

    