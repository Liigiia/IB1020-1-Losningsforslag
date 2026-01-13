#Eksamen Høst 2021

import numpy as np
import random as ra


#%%
# Oppgave 1a

def panteautomat(a,b):
    smbrus = 2*a
    stbrus = 3*b
    return smbrus, stbrus

# Oppgave 1b

for y in range (5,24,2): #fordi vi vil ha med 23 må det stå 24
    x = 12
    svar, svaret = panteautomat(x, y)
    print("Verdien for små brusflasker er lik", svar, "mens verdien for store brusflasker er", svaret)
    print ("Totalverdi panteverdi =", svar + svaret)
    
#%%
# Oppgave 2a

#denne delen hadde du ikke trengt å ta med til eksamen
b = float(input("Skriv inn et desimaltall:\n"))
c = float(input("skriv inn et desimaltall til:\n"))
# slutt på delen :D

arr1 = np.array([b,c])

def sorter(arr1):
   
    if arr1[0] < arr1[1]:
        
        temp = arr1[0]
        arr1[0] = arr1[1]
        arr1[1] = temp
        svar = arr1
        
        return svar #Kunne også bare returner arr1

    
    else:
        print("tallene er endten sortert fra før, eller holder samme verdi")
        return arr1
        


print(sorter(arr1))

#%% Oppgave 2b
import numpy as np

# Generer et array med 1000 tilfeldige desimaltall mellom 1.0 og 5.0
arr2 = np.random.uniform(1.0, 5.0, 1000)

# While-løkke for å summere tallene til summen overstiger 850
# løkka vil heller ikke overstige antall siffer i arrayet (som er 1000)
def regnut(array): #lager en funksjon for å unngå å bruke globale variabler
    summen = 0
    index = 0
    
    while summen <= 850 and index < len(arr2):
        summen += arr2[index]
        if summen > 850:
            print("Tall", index, "i arrayet, altså", round(arr2[index],2), "medførte at summen oversteg 850")
            return array[index]
            break #gjør at while-løkka avsluttes etter at verdien overstiger 850
        index += 1

svar = regnut(arr2)
print("svaret av arrayet er", svar)

#Oppgave 2c

def funk(x, array):
    teller = 0
    for k in range(len(arr2)):
        if arr2[k] != x:  # Sjekker om elementet IKKE er lik x
            teller += 1  # Teller opp når vi ikke finner et element som er lik x
        
        else:
            print("Element", k, "i arrayet har samme verdi som x")
            return arr2[k]

print(funk(2.55,arr2)) #Finnn ut av dette senere

#%% METODE 2

def funk2(x, array):
    indeks = 0
    for t in range (len(array)):
        if array[t] == x:
            indeks = t
            return indeks
        
        elif t == len(array) and array[t] != x:
            return f"Ingen element i arrayet er lik {x}"

print(funk2(2.55,arr2))

#%%
#Oppgave 3

#sample_space = np.array([0,1,2,3,4])
#tall = np.random.choice (sample_space)

vinnere = 0

for b in range (0,10000):
    
    tall = ra.randint(0, 4)
    tall1 = ra.randint(0, 4)
    tall2 = ra.randint(0, 4)    

    san = tall + tall1 + tall2

    if san == 0:
        vinnere += 1
        
        
sannsynelighet = vinnere/10000
print("Sannsnyneligheten for å vinne er", round(sannsynelighet,6))

#%% METODE 2

n = 10000
gunstig = 0
sample_space = np.array([0,1,2,3,4])

for i in range(n):
    tall = np.random.choice(sample_space,3)
    
    if sum(tall) == 0:
        gunstig += 1

sanns = gunstig/n  

print(sanns)

#%%
#Oppgave 4

def funksjon(t):
    a = t
    begrensning_A = a + (20/a) + np.sqrt(a**2 + (20/a)**2)
    return begrensning_A

a_vals = np.linspace(0.01, 2000, 100000)
minste_omkrets = np.inf
beste_a = 0

for a in a_vals:
    omkrets = funksjon(a)
    
    if (omkrets < minste_omkrets):
        minste_omkrets = omkrets
        beste_a = a

print("Minste omkrets er", round(minste_omkrets,4), "når a er", round(beste_a, 4) , "og b er", round (20/beste_a, 4))

#%% METODE 2

def Omkrets(a):
    omkretsen = a + (20/a) + np.sqrt(a**2 + (20/a)**2)
    return omkretsen

def Areal(a):
    Arealet = (a*(20/a))/2
    return Arealet

A = np.linspace(0.01,2000,100000)
minst_o = np.inf
best_a = 0

for i in A:
    omkretsen = omkrets(i)
    
    if (omkretsen < minst_o):
        minst_o = omkretsen
        best_a = i
        
        if Areal(best_a) == 10: #Trenger egt ikke denne sjekken siden vi vet at b må være lik 20/a for at arealet skal bli 10
            
            B = 20/best_a
            C = np.sqrt(best_a**2 + B**2)
        
print("Minste mulige omkrets =", minst_o ," gitt areal = 10 er når a =", best_a, "og b =", B, "og c =", C)

