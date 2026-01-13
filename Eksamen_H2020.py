#%% Eksamen Høst 2020
import numpy as np
import random as ra

#%%
# oppgave 1 a)

def trapes(a,b,h):
    A = (h*(a+b))/2
    return A

# oppgave 1 b)

for B in range(3, 13):
    A = 5
    H = 7
    
    tall = trapes(A,B,H)
    
print("summen av figurene =", tall)

#%% 
# Oppgave 2 a)

def EkspoTilTo(n):
    
    if n > 0:
        arrayet = np.zeros(n +1) #Vil få med verdi n i arryaet
    
        for t in range(len(arrayet)):
            tall = 2**t
            arrayet[t] = tall
            p = sum(arrayet)
        
        c = p - 1 #tar -1 siden N>0 og et hvert tall opph�yd i 0 = 1
    
        return c
    
    else:
        return "vennligst Skriv et heltall der N > 0"

print(EkspoTilTo(3))

#%%
# Oppgave 2 b)

summen = 0
verdi = 0
minste_verdi = 0

while summen < 8000:
    verdi += 1
    svar = EkspoTilTo(verdi)
    
    if svar > 8000:
        summen = svar
        minste_verdi = verdi
        print(minste_verdi)

# Oppgave 2 c)

def EkspoTilA(a,n):
    
    arrayet = np.zeros(n + 1) #Vil få med verdi n i arryaet
    
    for t in range(len(arrayet)):
        tall = a**t
        arrayet[t] = tall
        p = sum(arrayet)
        
    c = p - 1 #En hver x^0 vil være = 1
    
    return c

#%%
# Oppgave 3

n = 10000
gunstig = 0

for t in range(n):
    LE = np.random.uniform(0,7.7)
    M = np.random.uniform(0, 6)
    J = np.random.uniform(0, 6)
    
    if (LE>M and M>J):
        gunstig += 1

sans = gunstig/n

print(sans)

#%%
# Oppgave 4

def f(x):
    y = x**2
    return y

def avstand(x, y):
    avstanden = np.sqrt(((x-0)**2) + ((y-2)**2))
    return avstanden

start = -1
stopp = 2.01

korteste_avstand = np.inf

for t in np.arange(start, stopp, 0.01):
    
    tall = f(t)
    avstand1 = avstand(t, tall)
    
    if avstand1 < korteste_avstand:
        
        korteste_avstand = avstand1
    
print (korteste_avstand)
    


        
