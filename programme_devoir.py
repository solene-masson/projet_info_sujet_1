import csv
fichier = open('EIVP_KM_new.csv')
f = csv.reader(fichier)
L=[]
L2=[]
for ligne in f:
    L.append(ligne)
for x in L[1:]:
    L2.append(x[0].split(";"))
# print(L2)
fichier.close()
print()


# Pour le capteur 1

Temp1=[]
Temps1=[]
Noise1=[]
Humidity1=[]
Lumex1=[]
CO2_1=[]
for x in L2:
    if float(x[1])==1:
        Temp1.append(float(x[3]))
        Temps1.append(x[8].split(":"))
        Noise1.append(float(x[2]))
        Humidity1.append(float(x[4]))
        Lumex1.append(float(x[5]))
        CO2_1.append(float(x[6]))
# print(Temp1)
# print(Temps1)
# print()

heure1=[]
minute1=[]
seconde1=[]
for x in Temps1:
    heure1.append(int(x[0]))
    minute1.append(int(x[1]))
    seconde1.append(int(x[2]))
# print(heure)
# print()
# print(minute)
# print()
# print(seconde)
# print()

intervalle_temps1=[0]
var=heure1[0]*3600+minute1[0]*60+seconde1[0]
for i in range(1,len(heure1)-1):
    if heure1[i] <= heure1[i+1] :
        intervalle_temps1.append(abs((heure1[i]*3600+minute1[i]*60+seconde1[i])-var))
        var=heure1[i]*3600+minute1[i]*60+seconde1[i]
    elif heure1[i] > heure1[i+1]:
        heure1[i+1]=heure1[i+1]+24 #problème lorsqu'on passe à un autre jour, il faudrait ajouter 24*jour
        intervalle_temps1.append(abs((heure1[i]*3600+minute1[i]*60+seconde1[i])-var))
        var=heure1[i]*3600+minute1[i]*60+seconde1[i]
intervalle_temps1.append((heure1[-1]*3600+minute1[-1]*60+seconde1[-1])-(heure1[-2]*3600+minute1[-2]*60+seconde1[-2]))
# print(intervalle_temps)
# print()

temps1=[]
var=0
for i in range(len(intervalle_temps1)):
    var+=intervalle_temps1[i]
    temps1.append(var/3600)
# print(temps1)
# print()


import matplotlib.pyplot as plt
plt.figure("Courbe de la température en fonction du temps") #on créé une figure
plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
plt.ylim(20,30)                                         #on choisit l'échelle des ordonnées
plt.plot(temps1,Temp1, color='magenta')
plt.grid()
plt.xlabel('Temps (heure)')                               
plt.ylabel('Température (°C)')
plt.title('Graphique de la température en fonction du temps', color='b')
plt.savefig('capteur1_temperature.pdf')
plt.show()

# plt.figure("Courbe du bruit en fonction du temps") #on créé une figure
# plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
# plt.ylim(20,60)                                         #on choisit l'échelle des ordonnées
# plt.plot(temps1, Noise1, color='magenta')
# plt.grid()
# plt.xlabel('Temps (heure)')                               
# plt.ylabel('Bruit (dB)')
# plt.title('Graphique du bruit en fonction du temps', color='b')
# plt.savefig('capteur1_bruit.pdf')
# plt.show()

# plt.figure("Courbe de l'humidité en fonction du temps") #on créé une figure
# plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
# plt.ylim(-5,80)                                         #on choisit l'échelle des ordonnées
# plt.plot(temps1, Humidity1, color='magenta')
# plt.grid()
# plt.xlabel('Temps (heure)')                               
# plt.ylabel('Humidité')
# plt.title("Graphique de l'humidité en fonction du temps", color='b')
# plt.savefig('capteur1_humidite.pdf')
# plt.show()

# plt.figure("Courbe de la luminosité en fonction du temps") #on créé une figure
# plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
# plt.ylim(-5,900)                                         #on choisit l'échelle des ordonnées
# plt.plot(temps1, Lumex1, color='magenta')
# plt.grid()
# plt.xlabel('Temps (heure)')                               
# plt.ylabel('Luminosité')
# plt.title('Graphique de la luminosité en fonction du temps', color='b')
# plt.savefig('capteur1_luminosite.pdf')
# plt.show()

# plt.figure("Courbe du taux de CO2 en fonction du temps") #on créé une figure
# plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
# plt.ylim(375,700)                                         #on choisit l'échelle des ordonnées
# plt.plot(temps1, CO2_1, color='magenta')
# plt.grid()
# plt.xlabel('Temps (heure)')                               
# plt.ylabel('CO2')
# plt.title('Graphique du taux de CO2 en fonction du temps', color='b')
# plt.savefig('capteur1_co2.pdf')
# plt.show()


# Pour le capteur 2

Temp2=[]
Temps2=[]
Noise2=[]
Humidity2=[]
Lumex2=[]
CO2_2=[]
for x in L2:
    if float(x[1])==2:
        Temp2.append(float(x[3]))
        Temps2.append(x[8].split(":"))
        Noise2.append(float(x[2]))
        Humidity2.append(float(x[4]))
        Lumex2.append(float(x[5]))
        CO2_2.append(float(x[6]))
# print(Temp1)
# print(Temps1)
# print()

heure2=[]
minute2=[]
seconde2=[]
for x in Temps2:
    heure2.append(int(x[0]))
    minute2.append(int(x[1]))
    seconde2.append(int(x[2]))
# print(heure)
# print()
# print(minute)
# print()
# print(seconde)
# print()

intervalle_temps2=[0]
var=heure2[0]*3600+minute2[0]*60+seconde2[0]
for i in range(1,len(heure2)-1):
    if heure2[i] <= heure2[i+1] :
        intervalle_temps2.append(abs((heure2[i]*3600+minute2[i]*60+seconde2[i])-var))
        var=heure2[i]*3600+minute2[i]*60+seconde2[i]
    elif heure2[i] > heure2[i+1]:
        heure2[i+1]=heure2[i+1]+24 #problème lorsqu'on passe à un autre jour, il faudrait ajouter 24*jour
        intervalle_temps2.append(abs((heure2[i]*3600+minute2[i]*60+seconde2[i])-var))
        var=heure2[i]*3600+minute2[i]*60+seconde2[i]
intervalle_temps2.append((heure2[-1]*3600+minute2[-1]*60+seconde2[-1])-(heure2[-2]*3600+minute2[-2]*60+seconde2[-2]))
# print(intervalle_temps)
# print()

temps2=[]
var=0
for i in range(len(intervalle_temps2)):
    var+=intervalle_temps2[i]
    temps2.append(var/3600)
# print(temps1)
# print()



# import matplotlib.pyplot as plt
# plt.figure("Courbe de la température en fonction du temps") #on créé une figure
# plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
# plt.ylim(20,30)                                         #on choisit l'échelle des ordonnées
# plt.plot(temps2,Temp2, color='magenta')
# # plt.plot(temps1,Temp1, color='black')
# plt.grid()
# plt.xlabel('Temps (heure)')                               
# plt.ylabel('Température (°C)')
# plt.title('Graphique de la température en fonction du temps', color='b')
# plt.savefig('capteur2_temperature.pdf')
# plt.show()

# plt.figure("Courbe du bruit en fonction du temps") #on créé une figure
# plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
# plt.ylim(20,60)                                         #on choisit l'échelle des ordonnées
# plt.plot(temps2, Noise2, color='magenta')
# plt.grid()
# plt.xlabel('Temps (heure)')                               
# plt.ylabel('Bruit (dB)')
# plt.title('Graphique du bruit en fonction du temps', color='b')
# plt.savefig('capteur2_bruit.pdf')
# plt.show()

# plt.figure("Courbe de l'humidité en fonction du temps") #on créé une figure
# plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
# plt.ylim(-5,80)                                         #on choisit l'échelle des ordonnées
# plt.plot(temps2, Humidity2, color='magenta')
# plt.grid()
# plt.xlabel('Temps (heure)')                               
# plt.ylabel('Humidité')
# plt.title("Graphique de l'humidité en fonction du temps", color='b')
# plt.savefig('capteur2_humidite.pdf')
# plt.show()

# plt.figure("Courbe de la luminosité en fonction du temps") #on créé une figure
# plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
# plt.ylim(-5,900)                                         #on choisit l'échelle des ordonnées
# plt.plot(temps2, Lumex2, color='magenta')
# plt.grid()
# plt.xlabel('Temps (heure)')                               
# plt.ylabel('Luminosité')
# plt.title('Graphique de la luminosité en fonction du temps', color='b')
# plt.savefig('capteur2_luminosite.pdf')
# plt.show()

# plt.figure("Courbe du taux de CO2 en fonction du temps") #on créé une figure
# plt.xlim(-10,645)                                  #on choisit l'échelle des abscisses
# plt.ylim(375,700)                                         #on choisit l'échelle des ordonnées
# plt.plot(temps2, CO2_2, color='magenta')
# plt.grid()
# plt.xlabel('Temps (heure)')                               
# plt.ylabel('CO2')
# plt.title('Graphique du taux de CO2 en fonction du temps', color='b')
# plt.savefig('capteur2_co2.pdf')
# plt.show()






# Fonctionnalités demandées :

noise,temp,humidity,lum,co2=2,3,4,5,6  # associe la colonne correspondante
date=[]
for x in L2:
    date.append(x[9])


# def trouver_indice(liste,element_recherche):
#     for i in range(len(liste)):
#         if liste[i]==element_recherche:
#             return i


import matplotlib.pyplot as plt
def evolution_fonction_temps(variable,start_date,end_date,capteur):
    Variable=[]
    temps=[]
    debut=date.index(start_date) #fonctionne pour le capteur 1 car renvoie l'indice de la première correspondance
    fin=date.index(end_date)
    id_variable=variable #problème si la variable n'est pas écrite pareil
    for x in L2:
        if float(x[1])==capteur:
            for i in range(debut,fin+1):
                Variable.append(float(L2[i][id_variable]))
                temps.append(L2[i][8])
    plt.figure("Courbe variable en fonction du temps") 
    # plt.xlim(-10,645)                                  
    # plt.ylim(375,700)                                         
    plt.plot(temps, Variable, color='b')
    plt.grid()
    plt.savefig('courbe_test.pdf')
    plt.show()

#print(evolution_fonction_temps(temp,'2019-08-12','2019-08-16',1))


# Fonctions statistiques

def Min(L):
    var=L[0]
    for x in L:
        if x<var:
            var=x
    return var

def Max(L):
    var=L[0]
    for x in L:
        if x>var:
            var=x
    return var

def moyenne(L):
    s=0
    n=len(L)
    for x in L:
        s+=x
    return s/n
    
def variance(L):
    m=moyenne(L)
    return moyenne([(x-m)**2 for x in L])

def ecart_type(L):
    return variance(L)**0.5

def Fusion(L1,L2) :
    LF=[ ]
    while len(L1)>0 and len(L2)>0 :
        if L1[0]<L2[0] :
            LF.append(L1.pop(0))
        else :
            LF.append(L2.pop(0))
    return LF+L1+L2

def TriFusion(L) :
    if len(L)<=1 :
        return L
    else :
        n=len(L)//2
        L1=TriFusion(L[0 : n])
        L2=TriFusion(L[n : len(L)])
        return Fusion(L1,L2)

def mediane(L):
    L = TriFusion(L)
    n= len(L)
    if n < 1:
        return None
    if n % 2 == 0 :
        return ( L[(n-1)//2] + L[(n+1)//2] ) / 2.0
    else:
        return L[(n-1)//2]


def valeurs_statistiques(L):
    return (Min(L), Max(L), ecart_type(L), moyenne(L), variance(L), mediane(L))

# import numpy as np

def partie_entiere(nombre):
    nb=nombre-int(nombre)
    if nb<0.5:
        return int(nombre)
    else:
        return int(nombre)+1

def humidex(temperature,humidity):
    return partie_entiere((temperature+(5/9)*((6.112)*10**(7.5*(temperature/(237.7+temperature)))*(humidity/100)-10)))
