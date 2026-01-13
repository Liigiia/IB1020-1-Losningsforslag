import numpy as np
import math as mt
import random as ra
import matplotlib.pyplot as plt
#%%

#Opp1 a)

def cosh(x):
    return (np.exp(x) + np.exp(-x))/2

#Opp1 b)

v = 0.4
x_verdier = np.linspace(-2,3)
y_verdier = v*cosh((x_verdier)/v)

plt.close("all")
plt.figure(1)
plt.plot(x_verdier,y_verdier, "m-")
plt.grid()
plt.show()

#Opp1 c)

iterasjonsNr = 0

for a in range (7,40,2):
    
    y = a*cosh(4/a)
    print(f"Funksjonserdien til y(a) er {y} når verdien til a er {a}\n")
    print(f"Dette er iterasjonNr; {iterasjonsNr}")
    
    iterasjonsNr += 1
#%%

def primtall(x):
    # Håndter tilfeller der x er mindre enn 2 (ingen primtall)
    if x < 2:
        return False
    # Sjekk om x er delelig med noen tall fra 2 til kvadratroten av x
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False  # x er ikke et primtall
    return True  # x er et primtall

#Opp2 a)

def antall_primtall(x_start,x_stop):
    primtallteller = 0
    for b in range(x_start,x_stop+1): #+1 for å ha med x_stop
        if primtall(b): # antar at primtall gir true/false utslag
            primtallteller += 1
    
    return primtallteller

#Opp2 b)

def fem_primtall(x_start):
    primtallteller = 0
    fortsett = x_start
    
    while primtallteller <= 5:
        if primtall(fortsett):
            primtallteller +=1
            print(f"{fortsett}")
            if primtallteller == 5:
                return ("Fem primtall har blitt funnet!")
                break
    fortsett += 1

#Opp2 c)

def primtvilling(x_start,x_stop):
    primtvillingsjekker = False
    
    for p in range (x_start, x_stop):
        if primtall(p) and primtall(p+2):
            primtvillingsjekker = True
            
            if primtvillingsjekker:
                return ("Det finnes primtallstvillinger på intervallet!!\n")
            else:
                return ("Det finnes IKKE primtallstvillinger på intervallet :(\n")
      
#%%

#Opp3 
def f(x):
    return (x**2)-(4*x)+3

def g(x):
    return (2*x)+1

def h(x):
    return -(x-2)*(x-10)

n = 10000
gunstige_utfall = 0

for t in range (1,n):
    x_koor = 6*np.random.rand()
    
    if f(x_koor) < g(x_koor) and g(x_koor) < h(x_koor):
        gunstige_utfall += 1
        
Sanns = gunstige_utfall/n 

print("Sannsynligheten for at f(x) < g(x) OG g(x) < h(x)", round(Sanns,2))
    
#%%        

#Opp4  

def f(x):
    return (x**2)-(4*x)+3

def g(x):
    return (2*x)+1

x_verdier = np.linspace(0,6,61)
funkf = f(0)
funkg = g(0)
størst_avstand = abs(funkf - funkg)


for i in x_verdier:
    avstand = abs((f(i)) - (g(i)))
    
    if avstand > størst_avstand:
        størst_avstand = avstand
        
print("Største vertikale avstand er", størst_avstand)   
