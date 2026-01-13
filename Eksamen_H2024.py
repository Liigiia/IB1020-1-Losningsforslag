 #%% HØST 2024
import numpy as np
import matplotlib.pyplot as plt
import random as ra
#%%

#Opp1 a)

def sirkel(x,r):
    y_upper = np.sqrt((r**2)-(x**2))
    y_lower = np.sqrt((r**2)-(x**2))*(-1)
    return y_upper, y_lower

svar1,svar2 = sirkel(1,2)

print("verdien til y_upper er:",svar1 , "verdien til y_lower er:",svar2)

#Opp1 b)

X = np.linspace(-2, 2, 100)

upper, lower = sirkel(X,2)

plt.close("all")
plt.figure(2)
plt.plot(X,upper, "m-")
plt.title("graf til y_upper definert fra -2 til 2")
plt.show()


plt.close("all")
plt.figure(3)
plt.plot(X,lower, "m-")
plt.title("graf til y_lower definert fra -2 til 2")
plt.show()

#Opp1 c)

x_verdier = np.linspace(-2,2,100)

for t in range (0,100):
    p = x_verdier[t]
    upper, lower = sirkel(p,2)
    
    if t < 49: #fordi t teller fra 0 og opp
        print (f"x = {p} og y = {upper}\n")
    
    else:
        print(f"x = {p} og y = {lower}\n")
        
#%%

#Opp2 a)


def lag_array(i):
    array_a = np.zeros(i)
    
    if i <= 1:
        return ("vennligst skriv inn et heltall som er større enn 1")
        
    else:
        for p in (len(array_a)):
            tall = ra.randint(2,8)
            array_a[p] = tall
            
    return array_a 

#Opp2 b)

def finn_nabo(array, j):
    
    if j < 100:
        for t in (0,j):
            
            if array[t] == array[0]:
                print("Ingen nabo til venstre!")
                print(array[t],"sin nabo til høyre er",array[t+1])
                return array[t+1]
                 
            elif array[t] == array[j]:
                print("Nabo til venstre for", array[t], "er",array[t-1])
                print ("Ingen nabo til høyre")
                return array[t-1]
            
            else:
                print("Nabo til venstre er:", array[t-1])
                print("Nabo til høyre er:", array[t+1])
                return array[t-1], array[t+1]
    else:
        return("arrayet er ikke langt nok, må ha indeksering der j<100")

#Opp2 c)

def finn_antall(array,j):
    if j > 100:
        return "Array må oppfylle følgende krav: indeksering(j) < 100"
    
    else:
        summen = 0
        indeks = 0
        
        while summen < 25:
            indeks += 1
            summen = array[indeks]
            
            if summen >= 25:
                print("antall elementer som inngikk i utregningen var", indeks)
                return indeks
            
            elif indeks == (len(array)) and summen < 25:
                print ("Med de antall elementer som nå var til rådighet ble ikke summen 25 oppnådd")
                break
        
#%% 

#Opp3

utfall = [1,2,3,4,5,6]

n = 10000
gunstig = 0

for i in range (n):
    terninger = np.random.choice(utfall,3)
    if 2 not in terninger and 4 not in terninger and 6 not in terninger:
        gunstig += 1
        
sanns = gunstig/n

print("sannsynligheter for at alle 3 terninger viser oddetall er", sanns)

#%% 

#opp3 l�sning nr 2

n = 10000
gunstig = 0

for i in range(n):
    svar = [ra.randint(1,6) for _ in range(3)]  # Trekker 3 terninger
    if np.all(np.array(svar) % 2 != 0):  # Sjekker om alle er oddetall
        gunstig += 1

sanns = gunstig / n

print("Sannsynligheten for at alle 3 terninger viser oddetall er", sanns)

#%%
      
#Opp4

def avstand(x,y):
    avstanden = np.sqrt(((x-2)**2) + ((y-(3/2))**2))
    return avstanden

def sirkel(x,r):
    y_upper = np.sqrt((r**2)-(x**2))
    y_lower = np.sqrt((r**2)-(x**2))*(-1)
    return y_upper, y_lower

minste_avstand = np.inf
verdier = np.linspace(-2,2, 100)

for i in verdier:

    Upper, Lower = sirkel(i,2)
    avstand_u = avstand(i,Upper)
    avstand_l = avstand(i,Lower)
    
    if avstand_u < avstand_l and avstand_u < minste_avstand:
        minste_avstand = avstand_u
        
    if avstand_l < avstand_u and avstand_l < minste_avstand:
        minste_avstand = avstand_l
        
print("Den minste avstanden er", minste_avstand)
        


  