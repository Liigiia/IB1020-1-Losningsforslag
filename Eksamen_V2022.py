#%% Eksamen vår 2022
import numpy as np

#%% OPPGAVE 1

#(a)

def volum(r1,h1,r2,h2):
    v_syl = np.pi*(r1**2)*h1
    v_kjegle = (1/3)*np.pi*(r2**2)*h2
    return v_syl, v_kjegle

#(b)

svar1, svar2 = volum(7,18,7,12)

print ("volumet av sylinder =", svar1, "mens volumet av kjegle =", svar2)
print ("totalt volum =", (svar1+ svar2))

#%% OPPGAVE 2

resultat = np.array(["G","T","G","IG","G"])
std_nr = np.array([26255,26317,26389, 26711,27019])

#(a)

for i in range (0,5): #tester med 5 fordi arrayet er bare 5 elementer langt
    if resultat[i] == "IG":
        print ("indeks =", i)
        
#(b)

def idk (array1,array2):
    for i in range (0,len(array1)):
        if array1[i] == "T":
            print("vedkommes studentnr er", array2[i])
            
#(c)
b = 0
antall = 0

while b < len(resultat): 
    if resultat[b] == "G":
        if std_nr[b] < 27222:
            antall += 1
    b += 1
    
    print(antall)
    
#%% OPPGAVE 3 

#Programmet funker

#%% OPPGAVE 4

import random as ra

def tid(fart, avstand):
    return avstand/fart

n = 10000
fordel_rute_2 = 0
tid_rute_1 = tid(20,5)
tid_rute_2_a_b = tid(10,2)

for i in range(n):
    tid_rute_2_b_c = tid(ra.randrange(70,86), 4)
    if tid_rute_2_a_b + tid_rute_2_b_c < tid_rute_1:
        fordel_rute_2 += 1

print("Sansynligheten for at rute 2 lønner seg er", round(fordel_rute_2/n,2) )


            
        
        
