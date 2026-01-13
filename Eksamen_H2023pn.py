#%% HØST 2023 PÅ NYTT
import numpy as np
import random as ra

#%%

#Opp1 a)

def midtpunkt(a,b):
    x = ((a+b)/2)
    return x

#Opp1 b)

def vektetPunkt(a,b,c):
    x = (a*(1-c))+ (b*c)
    return x

#Opp1 c)

kombo = 101

C = 0

for t in range(kombo):
    print(midtpunkt(4,9,C))
    C += 0.01
    
#%%

arr1 = np.random.rand(100)

#Opp2 a)

def finnAntall(array):
    
    teller = 0
    
    for t in range (len(array)):
        
        if array[t] > 0.4 and array[t] < 0.5:
            
            teller += 1
    
    return teller

print("antall elementer som ligger på intervallet [0.4,0.5] er", finnAntall(arr1))

#Opp2 b)

def finnIndex(array):
    
    for t in range (len(array)):
        
        if array[t] > array[t+1]:
            print ("indeks", t, "følger krav array[t] > array[t+1]")
        return

finnIndex(arr1)

#Opp2 c)

def finnAntallElement(array):
    teller = 0
    summen = 0
    
    while summen > 25:
        summen += array[teller]
        teller += 1
        
        if summen <= 25:
            print("Antall elementer som inngikk i utregningen er", teller)
            return teller

finnAntallElement(arr1)

#%% METODE 1

#Opp3 

n = 10000
gunstige = 0

y = 3*["F"] + 19*["L"]

for i in range(n): 
    svar = np.random.choice(y,2,False)
    
    if svar.tolist().count("L") == 2:
        gunstige += 1

sanns = gunstige/n 
        
#%% METODE 2

#Opp 3 

N = 10000
gunstig = 0

y = 3*[0] + 19*[1]

for t in range(N):
    svar = np.random.choice(y,2,False)    
    
    if sum(svar) >= 2:
        gunstig += 1

sanns2 = gunstig/N

#%% Denne versjonen var bedre

#Opp 4

def Korde(h,R):
    K = np.sqrt(4*(2*h*R-(h**2)))
    return K

Radius = 123.9
Korden = 135
Høyde = 0.0

while Korde(Høyde,Radius) < Korden:
    
    Høyde += 0.1
    
    if Korde(Høyde,Radius) >= Korden:
        print("Høyden er", Høyde)
        break
        
