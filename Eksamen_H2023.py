import numpy as np

#%%
#Oppgave 1 a)

def midtpunkt(a,b):
    return (a+b)/2

print("Midtpunktet mellom a, og b er", midtpunkt(2,4))

#Oppgave 1 b)

def vektetPunkt (a,b,c): #Unødvendig med if og elif, leste ikke oppgaven nøye nok
    if c == 0:
        x = a
    
    elif c == 1:
        x = b
        
    else:
        x = a*(1-c)+ b*c
    
    return x

t = np.random.rand()

print("lineærkombinasjonen av tallene a og b er", round(vektetPunkt(1,t,5),2))

#%%
#Oppgave 1 c)

for t in range (0, 101):
    a = 4
    b = 9 
    
    if t == 0:
        c = t
    else:
        c += 0.01
        
    print(vektetPunkt(a,b,c))
    
#print(np.linspace(0,1,101))
    
#%%
# Oppgave 2 a)

arr1 = np.random.rand(100)

def finnAntall(array):
    teller = 0
    
    for r in range(0,len(array)):
        if array[r] >= 0.4 and array[r] <= 0.5 :
            teller += 1 
    return teller

print(finnAntall(arr1))

#%%
# Oppgave 2 b)

def finnIndex(array):
    for r in range(0, len(array)):
        if array[r] > array[r + 1]:
            print("indeksen", r, "i arrayet, der array[indeks] =", array[r],"er større enn array[indeks + 1] som =", array[r + 1])
        return

finnIndex(arr1)

#%%
# Oppgave 2 c)

def finnAntallElement(array):
    summen = 0 
    teller = 0
    
    while summen < 25 and teller <= len(array):
        summen += array[teller]
        teller += 1
        if summen >= 25:
            print("antall elementer som førte til at summen ble tilnærmet 25 =", teller)
            return teller

print(finnAntallElement(arr1))

#%%
# Oppgave 3 

sans = 0
sans2 = 0
antall = 10000

for f in range(antall):
    
    y = 3*["F"] + 19*["L"]
    svar = np.random.choice(y,2, False)
    if np.all(svar == "L"):
        sans += 1
    
sannsynelighet = sans/antall

# måte nr 2  å gjøre det på

for t in range(antall):
    y = 3*[0] + 19*[1]
    svar = np.random.choice(y,2, False)
    if sum(svar) >= 2:
        sans2 += 1
        
sannsynelighet2 = sans2/antall

# Begge viser ca samme verdi 
print(sannsynelighet)
print(sannsynelighet2)
 



#%%
# Oppgave 4

def ligning(h,r):
    K = np.sqrt(4*(2*h*R-(h**2)))
    return K

R = 123.9
K = 135
H = 0.0

while ligning(H, R) < K:
    H += 0.1
    
    if ligning(H, R) >= K:
        print(H)




    
    
    


    
    


        
    
