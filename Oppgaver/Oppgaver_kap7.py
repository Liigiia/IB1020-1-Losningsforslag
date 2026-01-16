# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:57:45 2024

@author: ligia
"""

import numpy as np
#import matplotlib.pyplot as plt
import math as mt

#%%
# Oppgave 7.1

print("skriv inn temperatur til H2O i grader\n")
vanntemp = float(input())

if vanntemp == 100:
    print("H20 koker, men er fortsatt i væskeform")
    
elif vanntemp > 100:
    print("H20 er i gassform")
    
elif vanntemp < 100 and vanntemp > 0:
    print("H20 er i væske-form")
 #idk hvorfor jeg skrev det med 0 bc så lenge vanntemp er under 100 så går det fint siden alt annet faller under "else"

else:
    print("H20 er i fast-form (fryst/blitt til is)")

#%%
# Oppgave 7.2

def sjekk_personnummer(personnummer):
    # Sjekk at personnummeret har 11 siffer
    # .isdigit er en innebygd Python-metode som brukes for å sjekke om alle tegn i en streng er tal
    if len(personnummer) != 11 or not personnummer.isdigit():
        
        return "Ugyldig personnummer. Må bestå av 11 sifre."

    # Henter  ut fødselsdato
    dag = personnummer[:2] #indeksering starter på 0 og tar ikke med det siste tallet (altså om du skriver 2:4)
    måned = personnummer[2:4] # og tallet er 310102 så vil den returnere (01)
    år = personnummer[4:6]

    # Sjekke kjønnet basert på det 9. sifferet
    kjønn_siffer = int(personnummer[8])
    kjønn = "gutt" if kjønn_siffer % 2 != 0 else "jente"

    # Bygg en tekst med fødselsdato og kjønn
    fødselsdato = f"{dag}.{måned}.{år}"
    return f"Fødselsdato: {fødselsdato}, Kjønn: {kjønn}"

# Eksempelbruk
personnummer = input("Skriv inn personnummer (11 siffer): ")
resultat = sjekk_personnummer(personnummer)
print(resultat)

#%%
# Oppgave 7.2 - løsning slik boka ønsker det

tall = int(input("Skriv inn the 9. sifferet i ditt personnummer\n"))

if tall % 2 == 0:
    print ("Du er en jente")

else: 
    print("Du er en gutt")

#%%
# Oppgave 7.3 

x = int(input("Skriv in x-koordinat\n"))
y = int(input("Skriv inn y-koordinat\n"))

if x > 0 and y > 0:
    print("Punktet ligger i 1. kvadrant")

elif x < 0 and y > 0:
    print("punktet ligger i 2. kvadrant")

elif x < 0 and y < 0:
    print("Punktet ligger i 3. kvadrant")
    
else:
    print ("Punkter ligger i 4. kvardant")
    
#%%
# Oppgave 7.4

fart = int(input("Hvor mange km over 60 kjørte du?\n"))

if fart < 0:
    print("Så flink du er!! du holdt deg innafor fartsgrensen!! : D")
    
elif fart >= 5 and fart < 10:
    print("Litt for raskt, det liker vi ikke : /\nDet blir 800kr i bot")
    
elif fart >= 10 and fart < 15:
    print("Dette er for raskt!\nDet blir 2100kr i bot")

elif fart >= 15 and fart < 20:
    print("litt av en råner du eller?\nDet blir 3800kr i bot")
    
elif fart >= 20 and fart < 25:
    print("Dette er ikke fast & furious >:( \nDet blir 5500kr i bot")

elif fart >= 25 and fart <26:
    print("Kan du ikke lese? fartsgrensen var 60!! Det blir for dumt å kjøre så raskt!!\nDet blir 8500kr i bot")

else:
    print("lappen kommer til å bli inndratt raskere enn du kjørte, smh")
    
#%%
# Oppgave 7.5

tid = input("Skriv inn tiden:")

[time, minutter] = tid.split(":")

time = int(time)
minutt = int(minutter)

if time == 0 or time < 12:
    print("tiden er", time, ":", minutter, "a.m")

else:
    print("tiden er", time, ":", minutter, "p.m")
    
#%%
# Oppgave 7.6 
# forskjellen var et her skulle man gjøre om programmet slik at f.eks 23:45 blir 11:45 (altså 12timers klokke)

tid = input("Skriv inn tiden:")

[time, minutter] = tid.split(":")

time = int(time)
minutt = int(minutter)

if time == 0 or time < 12:
    print("tiden er", time-12, ":", minutter, "a.m")

else:
    print("tiden er", time-12, ":", minutter, "p.m")
    

#%%
# Oppgave 7.7
# ikke jeg som skrev dette ofc, henta det fra nettsiden bc det var det oppgaven sa
# du skal bare gjette hvor mange ganger if-testen slår til før den kjører

arr1 = np.array([1, 2, 3, -5, 7, 0.1, -6])

if_slo_til = 0

if arr1[2] > np.sum(arr1):
    if_slo_til += 1

if np.size(arr1) == 6 and arr1[0] + arr1[3] < 0:
    if_slo_til += 1

if np.size(arr1) == 6 or arr1[0] + arr1[3] < 0:
    if_slo_til += 1

if arr1[1]*arr1[2] >= 2 and arr1[-1] < 0 or arr1[0]**2 == 4:
    if_slo_til += 1 
    
if  7 in arr1 and np.min(arr1) == -5:    
     if_slo_til += 1

print("Antall ganger if-testen slo til var", if_slo_til)

#%%
# Oppgave 7.8


def f(x):
    svar = mt.sin(x)
    return svar

x_koor = float(input("Skriv inn et x-koordinat:\n"))

if x_koor < 0 or x_koor > 4*np.pi:
    print ("x-koordinatet ligger utenfor intervallet")
    
elif x_koor < 4*np.pi and f(x_koor) > 1/2:
    print ("f(x) er større enn 0.5")
    
elif x_koor < 4*np.pi and f(x_koor) <= 1/2:
    print ("f(x) er mindre eller lik 0.5")

  

