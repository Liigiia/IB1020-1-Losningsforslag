#%% Eksamen_V2024
import numpy as np
import matplotlib.pyplot as plt

#%%  
# Oppgave 1 a)

def prosentvisEndring(c,d):
    return 100*((d-c)/c)

prosentvisEndring(1,1.5) 
# husk å skrive ut med passende tekst

# Oppgave 1 b)

def prosentvisEndring(c,d):
    X = 100*((d-c)/c)
    
    if c == 0:
        print("Ikke mulig å utføre deling med 0, vennligst skriv inn en verdi høyere enn 0")
    
    else:
        return X

#%%
# Oppgave 2 a)

def lagDatapunkt(x_stop):
    x1 = np.zeros(x_stop)
    x2 = np.zeros(x_stop)
    
    for k in range(len(x1)):
        x1[k] = k + 1
        x2[k] = k/(k + 1) 
    
    return x1, x2

print(lagDatapunkt(9))

#%%
# Oppgave 2 b)

x_verdier = np.arange(1,10)

y_verdier1, y_verdier2 = lagDatapunkt(len(x_verdier))

"""bruker lengden til arrayet slik at man får like mange y 
verdier som det er x verdier i arrayet"""

plt.close("all")
plt.figure(1)

plt.subplot(2,1,1) 
plt.plot(x_verdier, y_verdier1, "m*-")

plt.subplot(2,1,2)
plt.plot(x_verdier, y_verdier2, "b*-")

plt.show()

#%% oppgave 2b fasit-løsning
x_stop = 20
x_vals, y_vals = lagDatapunkt(x_stop)
plt.plot(x_vals, y_vals)

#%%
# Oppgave 3 a)

arr1 = np.random.uniform(-1, 1, 150)

def finnAntall(arr1):
    teller = 0
    for i in range(0,len(arr1)):
        if arr1[i] < 0:
            teller += 1
    return teller

print("antall tall i arrayet som er mindre enn 0 =", finnAntall(arr1))


# Oppgave 3 b)

def finnIndex(array):
    teller = 0 
    for i in range(0,len(arr1)):
        if arr1[i] < 0:
            teller += 1
            if teller == 10:
                print("det tiende negative taller er", arr1[i], "som ligger på indeks", i, "i arrayet")
                
                return i
        
finnIndex(arr1)

# Oppgave 3 c)

def finnPositivSum(arr1):
    summen = 0
    teller = 0
    for i in range (len(arr1)):
        if arr1[i] > 0:
            summen += arr1[i]
            teller += 1
            if summen >= 15:
               print("antall elementer som inngikk i at summen ble 15 =", teller) 
               return teller

print("antall elementer som inngikk i at summen ble 15 =", finnPositivSum(arr1))

#%%
# Oppgave 4
lim = np.linspace(0,np.sqrt(10))
y = abs(10 - lim**2)
x = max(np.sqrt(10-y))

print( max(x + y) )

#%% METODE 2

de minstX(Y):
    svaret = np.sqrt(10-Y)
    return svaret

størst_verdi = 0
Y = np.linspace(0,np.sqrt(10), 1000)

for i in Y:
    y = 10 - minstX(i)**2
    
    if (y + minstX(i)) > størst_verdi:
        størst_verdi = (y + minstX(i))
        
print (størst_verdi)

#%% Fasit

def finnMax():
    maks = 0
    x_vals = np.linspace(0, np.sqrt(10), 1000)
    for x in x_vals:
        y = 10-x**2
        if(x+y > maks):
            maks = x+y
            return maks
print("Den maksimale verdien for x+y er", finnMax())