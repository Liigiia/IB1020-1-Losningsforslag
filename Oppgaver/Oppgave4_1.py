import matplotlib.pyplot as plt
import numpy as np

# %% Definisjon av variabler med tallverdier

mnd = np.array([1, 2, 3, 4, 5, 6, 
                7, 8, 9, 10, 11, 12])  # [mnd nr]
temp = np.array([-3, -2, 2, 7, 11, 15, 
                 17, 16, 12, 6, 2, -3])  # [grad C]

F = (temp*(9/5))+32 #gjør om alle grader celsius til grader fahrenheit

#%% Beregning av middelverdi (median)
mean_temp = np.mean(F)

print(f'Mean-Value = {mean_temp:.1f}')

#%% Plotting av temperaturene

plt.close('all')
plt.figure(1)
plt.plot(mnd, F, 'm*-', label='temperature')
plt.plot(mnd, F*0 + mean_temp, 'k', label='Mean-value') 
plt.legend()
plt.title('Average monthly tempurature in Skien 2005-2015')
plt.xlabel( 'Month')
plt.ylabel('Degrees Fahrenheit')
plt.xlim(0, 13)
plt.ylim(26, 62) #Endret også y-begrensingen basert på høyeste og laveste temp
plt.grid()
plt.show()

#%%
#Oppgave 4.2

x = np.array ([0,1,2,3,4,5])

y = x
z = np.sqrt(x)

plt.close("all")
plt.figure(2, figsize = (12,9))
plt.plot(x, y, "m*-", label = "Usikker") # *for å få stjerne og m for å få fargen magenta
plt.plot(x, z, "go-", label = "Vet ikke") # - for å at python skal tegne linjer mellom punktene, o for å ha "dotter"
plt.legend()
plt.xlabel("x [s]")
plt.ylabel("m")
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.grid()
plt.savefig("plott1.pdf")
plt.show()

#%%
#Oppgave 4.3
x = np.array ([0,1,2,3,4,5])

y = x
z = np.sqrt(x)

plt.close("all")
plt.figure(3, figsize = (12,9))

plt.subplot(2,1,1) #Husk at første siffer = #Rader, andre = #Kolonner, og tredje = #plott
plt.plot(x, y, "m*-", label = "y")
plt.legend()
plt.grid()
plt.xlabel("x [s]")
plt.ylabel("[m]")
plt.xlim(0, 5)
plt.ylim(0, 5)

plt.subplot(2,1,2)
plt.plot(x, z, "go-", label = "z")
plt.legend()
plt.grid()
plt.xlabel("x [s]")
plt.ylabel("[m]")
plt.xlim(0, 5)
plt.ylim(0, 5)

plt.savefig("plott2.pdf")
plt.show()

#%%
#Oppgave 4.4

x = ["firma A", "firma B", "firma C"]
y = np.array([1204,1119,998])

plt.close("all")
plt.figure(4)
plt.xlabel("Firmanavn")  
plt.ylabel("Salgstall")
plt.title("Stolpediagram")
plt.bar(x, y, width = 0.5 , color = ("magenta", "green", "black"))

Høyde_over_graf = 5

for k in range (0, len(x)):
    plt.text(x[k], y[k] + Høyde_over_graf, str(y[k]))
    
    
#%%
#Oppgave 4.5

y = ["firma A", "firma B", "firma C"]
x = np.array([1204,1119,998])

plt.close("all")
plt.figure(5)
plt.ylabel("Firmanavn")
plt.xlabel("Salgstall")
plt.title("Stolpediagram")
plt.barh(y, x, color = ("magenta", "magenta", "magenta"))

#%%
#Oppgave 4.6

data = np.array ([1204,1119,998])
data_norm = data/sum(data)
labels = [
          "Firma A:" + str(data[0]),
          "Firma B:" + str(data[1]),
          "Frima C:" + str(data[2]),
          ]

plt.close("all")
plt.figure(6)
plt.rc("font", size = 12) #rc står for run configuration
plt.pie(data_norm, labels = labels, autopct = "%.1f%%")
plt.title("Kakediagram")
plt.show()

#%%
#Oppgave 4.7

#eksmepel på OO

mnd = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # [mnd nr]
temp = np.array([-3, -2, 2, 7, 11, 15, 17, 16, 12, 6, 2, -3])  # [C]

fig = plt.figure()  # Lager et figure-objekt med navn fig.
ax = fig.subplots()  # Lager et axes-objekt med navn ax.
ax.plot(mnd, temp)  # Bruker plot-metoden til objektet ax.
ax.set_xlabel('Maaned nr.')
ax.set_ylabel('Grader C')
ax.grid()

plt.savefig('oppg_temp_skien_oo_plotting.pdf')
plt.show()  # Bruker show-funksjonen i Pyplot-modulen til aa vise plottet.




    




