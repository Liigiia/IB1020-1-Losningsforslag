#Eksamen_NyH2021
import numpy as np
import matplotlib.pyplot as plt

#%%
# Oppgave 1 a)

def kule(r):
    Overflate = 4*np.pi*(r**2)
    Volum = (4/3)*np.pi*(r**3)
    return Overflate, Volum

# Oppgave 1 b)

for i in range(150, 0, -5):
    Overflaten,Volumet = kule(i)
    print("Når radius =", i, "er overflaten =", Overflaten, "og volumet =", Volumet)

#%%
# Oppgave 2 a)

arr1 = np.random.randint(1,4, size = 500)

for t in range(len(arr1)):
    if (arr1[t] == 3):
        print ("element i elementnummer", t, "er lik 3")
    
# Oppgave 2 b)

antall1 = 0
antall2 = 0
antall3 = 0

for l in range(len(arr1)):
    
    if (arr1[l] == 1):
        antall1 += 1 
        
    elif (arr1[l] == 2):
        antall2 += 1 
    
    elif (arr1[l] == 3):
        antall3 += 1 

print ("antall 1'ere i arrayet:", antall1)
print ("antall 2'ere i arrayet:", antall2)
print ("antall 3'ere i arrayet:", antall3)

# Oppgave 2 c)

navn = (["antall 1'ere", "antall 2'ere", "antall 3'ere"])
fordeling =([160,145,195])

plt.bar(navn, fordeling, width = 0.5, color = ("magenta", "blue", "black"))
plt.show()

# Oppgave 2 d)


def to_treere(arr1):
    
    bing = 0 
    bong = True
    bang = 0 
    
    while bang < 1 and bong:
        bing += 1 
        
        if (arr1[bing] == 3) and (arr1[bing + 1] == 3): 
            bang += 1
            bong = False 
            
    
    if bong == False: 
        print("I arr1 finnes det to påfølgende elementer som begge har verdi 3")
        
    else:
        print("I arr1 finnes det ikke to påfølgende elementer som begge har verdi 3")
        
        
to_treere(arr1)

#%%
# Oppgave 3

butt = np.linspace(1, 2178, 2178)
fuk = 10000
riverdale = 0

for u in range(fuk):
    cheeks = np.random.choice(butt, 2, False)
    if cheeks[0] >= 2000 and cheeks[1]>= 2000:
        riverdale += 1

hope = riverdale/fuk

print(hope)

#%%
# Oppgave 4

def funk(x):
    return np.log(x)

def funk2(x,y):
    b = np.sqrt((x**2) + (y**2))
    return b

sample = np.linspace(0.5, 4, 1000)
minste_avstand = np.inf
nærmeste_x = None

for t in range(len(sample)):
    x = sample[t]
    y = funk(x)
    avstand = funk2(x,y)
    
    if avstand < minste_avstand:
        minste_avstand = avstand
        nærmeste_x = x
        
print("Minste avstand =", minste_avstand, "ved x =", x)







    
    
    
    
    