# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:11:50 2024

@author: ligia
"""
#Alle oppgaver i kap 5

import numpy as np
import matplotlib.pyplot as plt

#%%
#Oppgave 5.1 s. 179 i bok

def hemmelig(g,h):
    A = (g*h)/2
    return A
print (hemmelig (4.5,4))

#%%
#Oppgave 5.2 Areal av rektangel

def rektangel (l,b):
    Svar = l*b
    return Svar
print(rektangel(6,9))

#%%
#Oppgave 5.3 Valutakurs

def kurs(x):
    dollar = x*1.19
    kroner = x*10.42
    return dollar, kroner
print (kurs(45))

x = 45

dollar = x*1.19
kroner = x*10.42

print(x, 'Euro er det samme som', dollar, 'amerikanske dollar og', kroner, 'norske kroner')

#%%
#Oppgave 5.4

def katet(b,a):
    k = np.sqrt(a**2-b**2)
    return k

katet1 = float(input("lengden av lille katet = "))
hypo = float(input("Lengden av hypotenusen = "))

storeK = katet(katet1, hypo)
print ("store katetet har lengde", storeK)

#%%
#Oppgave 5.5

x = 10

def myfun():
    print(x)

myfun()

#Programmet funker fordi det ikke er satt inn noe lokalvariabel så det blir litt som en funksjon i c
# henter ut den globale variabelen x 

#%%
#Oppgave 5.6

b = 10

def myfun():
   # b = b + 1
    print(b)

myfun()

"""
Inne i funksjonen prøver du å endre verdien av b ved å bruke uttrykket b = b + 1. 
Python tolker dette som at du prøver å bruke en lokal variabel b
(fordi når du tilordner til b i funksjonen, antar Python at det er en lokal variabel).
"""
#%%
#Oppgave 5.7

def k_energi(m,v):
    Ek = 1/2*m*(v**2)
    return Ek

masse = 80
fart = 12

K_energi = k_energi(masse, fart)

print("Svaret er", K_energi)

#%%
#Oppgave 5.8 & 5.9 
#forskjellen er at i oppgave 5.8 bruker vi ikke standardargument (at g = 9.81)

def høyde(e, m):
    g = 9.81 #i oppgave 5.9 byttes dette til g = 1.6
    h = e/(m*g)
    return h

Ep = 34.37
Masse = 0.48

Høyden = høyde(Ep, Masse)

print ("x står", round(Høyden,3), "m over bakken")

#%%
#Oppgave 5.10

def f(x):
    F = (x**2)+3
    return F

def g(x):
    G = 3*x - 1
    return G

x2 = np.linspace(0, 15)

# 0 = start, 15 = stop, 100 = antall tall du vil ha mellom start og slutt har ingenting å si her

plt.close("all")
plt.figure("Oppgave 5.10")
plt.grid()
plt.plot(x2, f(x2), "m-", label = "funksjonen f(x)" )
plt.plot(x2, g(x2), "c-", label = "funksjonen g(x)")
plt.legend()
plt.xlim(0,15)
plt.ylim(0,300)
plt.show()


#%%
# Oppgave 5.11

def A(x):
    return x**2 + 3

def B(x):
    return 3*x - 1

abx = np.linspace(-2, 3)

plt.close("all")
plt.figure("Oppgave 5.11") #Dersom du vil ha dette i et pop-up vindu må du definere figsize inni plt.figure (f.eks figsize = (12,9))
plt.grid()
plt.plot(abx, A(B(abx)), "m-", label = "funksjonen F(G(x))")
plt.plot(abx, B(A(abx)), "g-", label = "funksjonen G(F(x))")
plt.legend()
plt.title("Funksjon av funksjon")
plt.ylabel("Learning by doing")
plt.xlabel("Doing before learning")
plt.xlim(-2,3)
plt.ylim(0,15)
plt.show()

#%%
# Oppgave 5.12

def FinnElement(a):
    Antall = len(a)
    StørstTall = np.amax(a)
    return Antall, StørstTall

p = np.array([99,34,65,32,78,9,4,2,5,7,46,87,7,5,4335,767,7,3,78])

(Mengde, Max) = FinnElement(p)

print("Mengden med tall i arrayen =", Mengde,"\nMens det største tallet i arrayen er", Max)

#%%
#oppgave 5.13

def fartberegn(s,t):
    gjennomsnitt = sum(s)/len(s)
    V = gjennomsnitt/t
    return V, gjennomsnitt
    
S = np.array([1.05, 1.30, 1.10, 0.94, 1.21])  

tid = 2 #[tid i sekunder]

farten, distanse = fartberegn(S, tid)

print("Gjennomsnittfarten er", farten, "m/s mens gjenommsnitt-distansen = " , distanse)


#%%
# Oppgave 5.14

def nullpunkt(a,b):
    return -b/a

def areal(b, npunkt):
    return (npunkt*b/2)

a_val = float(input("skriv inn en verdi for a:"))
b_val = float(input("Skriv inn en verdi for b:"))

nullpkt = nullpunkt(a_val, b_val)
areal = areal (b_val, nullpkt)

print("Areal =", areal)

# Hvorfor er det at man må gange med nullpunktet for å finne areal?
"""
Svar: vi finner Høyden til trekanten (det vil alltid bli en trekant) ved å ta bruke kontstantleddet til likningen
(y= ax+b), her en konstantleddet det bruker setter som b, og grunnlinjen blir der y = 0 så dermed trenger vi nullpunktet for
å regne arealet av trekanten (fordi y-og-x-aksen står rett på hverandre er dette en rettvinklet trekant)
"""

#%%
# Oppgave 5.15


# den ene siden er konstantleddet som = bruker input (b)
# den andre siden er lengden fra origo til nullpunkt for y
# den tredje siden er lengden fra konstantledd til nullpunkt for y

def nullpunktet(a,b):
    return -b/a

averdi = float(input("Skriv inn en verdi for a:"))
bverdi = float(input("skriv inn en verdi for b:"))

funk_null = nullpunktet(averdi, bverdi)

xorigo = 0.0
yorigo = 0.0

avstand = np.sqrt(((funk_null)-xorigo)**2 + (0-yorigo)**2)
# dette er avstanden fra origo til nullpunkt for y

avstand2 = np.sqrt((0- funk_null)**2 + (bverdi-0)**2)
# regner avstand fra konstantledd (0,bverdi) til (-bverdi/averdi, 0)

omkretsen = bverdi + avstand + avstand2

print("Omkretsen til figuren = ", "%.2f" % omkretsen)

#%%
# Oppgave 5.16

from min_første_modul import stigende_rekke as sr #Spør Leo på torsdag eller onsdag idk

A = 45
B = 60
C = 90

tall = sr(A, B, C)
print(tall)    


#%%
# oppgave 5.17

def funk(a,b):
    c = np.sqrt(a**2 + b**2)
    omk = a + b + c
    return omk

side = 3
side2 = 4

omkrets = funk(side, side2)
print("Omkretsen til trekanten er", omkrets)

omkrets1 = lambda x, y: np.sqrt(x**2 + y**2) + x + y

resultat = omkrets1(3,4)
print("Omkretsen til trekanten er", resultat)

    