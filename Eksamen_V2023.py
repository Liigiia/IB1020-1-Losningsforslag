#%% Eksamen vår 2023
import numpy as np
import matplotlib.pyplot as plt
import random as ra
#%%
# Oppgave 1 a)

def bremselengde(v):
    x = 0.1 * v
    b1 = ((x*x)/2)
    b2 = 2 * x * x
    return b1, b2

# Oppgave 1 b)

def bremselengde2(v,føret):
    
    sommer,vinter = (bremselengde(v))
    
    if (føret == "Sommer"):
        return sommer
    
    elif (føret == "Vinter"): 
        return vinter


føre = "Sommer"
p = 45

print(bremselengde2(p, føre))

# Oppgave 1 c)

føre = "Vinter"
fart = 10

while bremselengde2(fart, føre) <= 122:
    fart += 1 
    
    if bremselengde2(fart, føre) >= 122:
        print("ved fart på", fart, "km/t vil bremselengden bli tilmærmet 122")
        
#%%
# Oppgave 2 a)

regnr = np.array(["EL 12945", "EL 567778", "HY 11045", "NV 44821"])
antallEL = 0
antallHY = 0

for i in range(0,len(regnr)):
    bokstaver = regnr[i].split()
    print(bokstaver[0])

    if (bokstaver[0] == "EL"):
        antallEL += 1
    
    elif (bokstaver[0] == "HY"):
        antallHY += 1 


print("Det var", antallEL, "EL- biler og", antallHY, "HY-biler som passerte bommen")

# Oppgave 2 b)

plt.bar(antallEL, height = antallEL, width=0.5, color = ("magenta"))
plt.bar(antallHY, height = antallHY, width=0.5, color = ("magenta"))
plt.show()

#%%
# Oppgave 2 c)

mellom = 0

arr1 = np.zeros(len(regnr))

for i in range(0, len(regnr)):
    bokstaver = regnr[i].split()
    print (bokstaver[0])
    
    if (bokstaver[0] == "EL"):
        arr1[i] = 1
    
    elif (bokstaver[0] == "HY"):
        arr1[i] = 2
        
    for c in range(0, len(arr1)-2):
        if arr1[c] == arr1[c + 2] and arr1[c + 1] == 2:
            mellom += 1
            
print(mellom)
print(arr1)


            
#%%
# Oppgave 3 

n = 10000
gunstig = 0

for _ in range(n):
    a = ra.randint(1,6)
    b = ra.randint(1,6)
    c = ra.randint(1,6)
    
    tall = a + b + c

for _ in range(n):
    d = ra.randint(1,6)
    e = ra.randint(1,6)
    f = ra.randint(1,6)
    g = ra.randint(1,6)
    
    tall2 = d + e + f + g
    

if (tall2 > 18 or tall2 < tall):
    gunstig += 1
        
sannsynelighet = gunstig/n

print(sannsynelighet)
    
#%%
# Oppgave 4 

strøm = np.array([0.017, 0.021, 0.019, 0.019, 0.018])

summen = 0
minutter = 0

for p in range(len(strøm)):
    summen += strøm[p]
    minutter += 1
    
    if summen >= 2:
        print (minutter)
    
    

        
   
    



        
        
        
    
    