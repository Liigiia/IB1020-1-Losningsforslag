#%% EKSAMEN VÃ…R 2021
import numpy as np
import math as mt
import random as ra
import matplotlib.pyplot as plt
#%%

#Opp1 a)

def areal_skravert(r):
    sirkel_areal = mt.pi*(r**2)
    sidekant_areal = (r*2)**2
    areal = sidekant_areal - sirkel_areal
    return areal

#Opp1 b)

#Antar at jeg har tilgang pÃ¥ ligning fra forrige oppgave

summen = 100
radius = 1 #setter radius lik 1 slik at den blir 2 nÃ¥r lÃ¸kka starter

while areal_skravert(radius) < summen:
    radius += 1
    
    if areal_skravert(radius) >= summen:
        print (f"arealet av det skraverte omrÃ¥det er 100 nÃ¥r radius = {radius}")
        break
        
    # gÃ¥r ogsÃ¥ an Ã¥ sette radius lik 2 ogsÃ¥ sette Ã¸keren her nede
    
#%% 

#Opp2 a)

x = np.array([9,17,5,-3,2])
Sum = 0

for i in range(len(x)):
    
    Sum += x[i]
    
gjennomsnitt = Sum/len(x)

#Opp2 b)

def Varians(array,snitt):
    variansen = 0
    
    for i in range(len(array)):
        variansen += ((x[i]-snitt)**2)
    
    vx = variansen/len(array)
    
    return vx

#%%

#Opp3 

n = 10000
gunstige = 0


for i in range(n):
    arr = np.zeros(3)
    x0 = ra.randint(1,9)
    x1 = ra.randint(1,9)
    
    arr[0] = x0
    arr[2] = x1
    
    if arr[0] == arr[2]:
        gunstige += 1

sanns = gunstige/n

#%% METODE 2

#Opp3

N = 10000
gunstig = 0

for i in range(N):
    hundrere = ra.randint(1,9)
    #tar ikke med tiere her siden vi egentlig ikke får bruk for den
    enere = ra.randint(1,9)
    
    if hundrere == enere:
        gunstige += 1 
    
sannsynelighet = gunstig/N

#%%

#Opp4 a)

def Areal(x,y):
    arealet = x*y
    return arealet

X = 0.1
Y = 19.8
y_max = 0
x_max = 0

while X < 10: # kommer fra at Y = 20 - 2*X 
    if Areal(X,Y) > Areal(x_max,y_max):
        x_max = X
        y_max = Y
    X += 0.1
    Y -= 0.2

print(f"Verdien av x som gir stÃ¸rst areal = {x_max} mens y-verdien = {y_max}")

#Opp4 b)

x_verdier = np.linspace(0.1, 9.9, 99)
y_verdier = np.zeros(99)

for i in (len(y_verdier)):
    y_verdier[i] = Areal(x_verdier[i], 20-(2*x_verdier[i]))
    
plt.close("all")
plt.figure(1)
plt.plot(x_verdier, y_verdier, "m*-")
plt.grid()
plt.show()

#%% annen måte å løse opp4 a)

import numpy as np

# Initialiser variabler
x_max = 0
y_max = 0
maks_areal = 0

# Iterer gjennom mulige x-verdier fra 0.1 til 9.9 (siden x ikke kan være 10 eller mer)
for x in np.arange(0.1, 10, 0.1):  # Øker x trinnvis med 0.1
    y = 20 - 2*x  # Beregn y basert på gjerdebegrensningen
    areal = x * y  # Beregn arealet
    
    # Sjekk om dette arealet er større enn det vi har funnet tidligere
    if areal > maks_areal:
        maks_areal = areal
        x_max = x
        y_max = y

# Skriv ut resultatet
print(f"Maksimalt areal: {maks_areal:.2f} m²")
print(f"Optimal verdi for x: {x_max:.2f} m")
print(f"Optimal verdi for y: {y_max:.2f} m")

     
        