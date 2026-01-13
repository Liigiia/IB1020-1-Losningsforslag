import numpy as np
import math as mt
import random as ra
import matplotlib.pyplot as plt
#%%
# Oppgave 1a)

def cosh(x):
    return (np.exp(x) + np.exp(-x))/2

# Oppgave 1b)


x_verdier = np.linspace(-2, 3)
y_verdier = 0.4*cosh(x_verdier/0.4)


plt.close("all")
plt.figure(3)
plt.plot(x_verdier, y_verdier, "m-")
plt.grid()
plt.xlim(0,-3)
plt.ylim(0,4)
plt.show()

# Oppgave 1c)

iterasjon = 1

for p in range (7, 40, 2):
    svar = p*cosh(4/p)
    iterasjon += 1
    
    print("dette er iterasjon nummer", iterasjon, "verdien a =", p, "funksjonsverdien y(a) = " , svar)
    
#%%
# Oppgave 2 a) kun det å lage funksjonen antall_primtall var en del av oppgaven, alt annet er for testing

def primtall(x):
    # Håndter tilfeller der x er mindre enn 2 (ingen primtall)
    if x < 2:
        return False
    # Sjekk om x er delelig med noen tall fra 2 til kvadratroten av x
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False  # x er ikke et primtall
    return True  # x er et primtall

a = int(input("Skirv inn et heltall:\n"))
b = int(input("Skriv inn et annet heltall:\n"))

def antall_primtall(x_start, x_stop):
    primtallteller = 0
    for t in range (x_start, x_stop + 1):
        if primtall(t):
            primtallteller += 1
            #print(t, "er et primtall")
            #print ("antall primtall mellom", x_start, "og", x_stop, "=", primtallteller)
        #else:
            #print("det finnes ingen primtall mellom", x_start, "og", x_stop)
    return primtallteller
            
print(antall_primtall(a,b))    

#%%
#Oppgave 2 b)

def fem_primtall(x_start):
    x = x_start
    iterasjon = 0
    prim = np.zeros(5)
    while iterasjon <= 5:
        if primtall(x):
            prim[iterasjon] = x
            iterasjon += 1
            x += 1
    return prim

#%%
#Oppgave 2 c) 

def primTvillinger(x_start, x_stop):
    
    tvilling = False

    for p in range(x_start, x_stop - 2):
        if primtall(p) and primtall(p + 2):
            tvilling = True
    
    if tvilling:
        print("Det finnes primtallstvillinger på intervallet")
    else:
        print("Det finnes IKKE primtallstvillinger på intervallet")


primTvillinger(18, 31)


#%% Oppgave 2c 

def primtvillinger (x_start, x_stop):
    x = x_start
    while x <= x_stop-2:
        if primtall(x) and primtall(x+2):
            print("Det finnes primtvillinger på intervallet")
            return
        x += 1
    print("Det finnes ikke primtvillinger på intervallet")
        
       
print(primtvillinger(18, 31))     

#%%
# Oppgave 3

def f(x):
    return (x**2)- 4*x + 3

def g(x):
    return 2*x + 1

def h(x):
    return -1*(x-2)*(x-10)
 
santeller = 0
      
for w in range (0,1000):
    x_koor = 6*np.random.rand()

    if f(x_koor) < g(x_koor) and g(x_koor) < h(x_koor):
        santeller += 1

print("Sannsyneligheten er =", santeller/1000)

#%%
# Oppgave 4

x_vals = np.linspace(0, 6, 61)
f_vals = f(x_vals)
g_vals = g(x_vals)
diff_vals = abs(f_vals-g_vals)
max_diff = max(diff_vals)
print("Største vertikale avstand er", max_diff)





    
    

        
        
    
