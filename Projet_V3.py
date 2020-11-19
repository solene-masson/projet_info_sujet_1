import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
from IPython.display import display

data = pd.read_excel(r'C:\Users\sosop\OneDrive\Documents\EIVP\Algo\projet_info\EIVP_KM_V2.xlsx')

data['sent_at'] = pd.to_datetime(data.sent_at)      #On change le type de la colonne

capteur_1 = data[data['id']==1]
capteur_2 = data[data['id']==2]
capteur_3 = data[data['id']==3]
capteur_4 = data[data['id']==4]
capteur_5 = data[data['id']==5]
capteur_6 = data[data['id']==6]

time1 = capteur_1.sent_at                       #Date et heure pour chaque capteur
time2 = capteur_2.sent_at
time3 = capteur_3.sent_at
time4 = capteur_4.sent_at
time5 = capteur_5.sent_at
time6 = capteur_6.sent_at


##FONCTIONS STATISTIQUES Début

def maximum(L):
    max = L[0]
    for k in range(1,len(L)):
        if L[k]>max:
           max = L[k]
    return(max)

def minimum(L):
    min = L[0]
    for k in range(1,len(L)):
        if L[k]<min:
            min = L[k]
    return(min)

def moyenne(L):
    s=0
    n=len(L)
    for k in range(n):
        s+=L[k]
    return(s/n)
    
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
    # L = L['colonneintéressante'].tolist()
    L = TriFusion(L)
    n= len(L)
    if n < 1:
        return None
    if n % 2 == 0 :
        return ( L[(n-1)//2] + L[(n+1)//2] ) / 2.0
    else:
        return L[(n-1)//2]
    
def covariance(X,Y):                    #fonctionne mais long
    L=[]
    for k in range(len(X)):
        L.append((X[k]-moyenne(X))*(Y[k]-moyenne(Y)))
    return moyenne(L)

def indice_corr(X,Y):                   #fonctionne mais long
    return (covariance(X,Y)/(ecart_type(X)*ecart_type(Y)))

def partie_entiere(nombre):
    nb=nombre-int(nombre)
    if nb<0.5:
        return int(nombre)
    else:
        return int(nombre)+1

def humidex(temperature,humidity):
    return partie_entiere((temperature+(5/9)*((6.112)*10**(7.5*(temperature/(237.7+temperature)))*(humidity/100)-10)))


##FONCTIONS STATISTIQUES Fin



##date min et max pour chaque capteur

mdate1,Mdate1 = minimum(time1.tolist()),maximum(time1.tolist())        
mdate2,Mdate2 = minimum(time2.tolist()),maximum(time2.tolist())        
mdate3,Mdate3 = minimum(time3.tolist()),maximum(time3.tolist())         
mdate4,Mdate4 = minimum(time4.tolist()),maximum(time4.tolist())      
mdate5,Mdate5 = minimum(time5.tolist()),maximum(time5.tolist())      
mdate6,Mdate6 = minimum(time6.tolist()),maximum(time6.tolist())   


##Courbes

def Courbe():
    variable = input('Choisir Température, Bruit, Luminosité, CO2 ou Humidité : ')
    
    if variable not in ['Température','Bruit','Luminosité', 'CO2', 'Humidité'] :
            return("La variable choisie n'existe pas...")
    
    
    numero = input('Saisir le numéro du capteur : ' )
    
    if (numero in ['1','2','3','4','5','6'])==True:
        time = []
        capteur_numero = []
        
        #Changer le UTC +02:00    J'ai mis Europe/Paris par défaut
        
        start_date = pd.to_datetime(input('Saisir date début AAAA-MM-JJ HH:MM : ')).tz_localize('CET')
        end_date = pd.to_datetime(input('Saisir date fin AAAA-MM-JJ HH:MM : ')).tz_localize('CET')
        
        #On choisit les dates et capteurs pertinents
        
        if numero == '1':  
            time,capteur_numero,date_max,date_min = time1,capteur_1,Mdate1,mdate1
        elif numero == '2':
            time,capteur_numero,date_max,date_min = time2,capteur_2,Mdate2,mdate2
        elif numero == '3':
            time,capteur_numero,date_max,date_min = time3,capteur_3,Mdate3,mdate3
        elif numero == '4':
            time,capteur_numero,date_max,date_min = time4,capteur_4,Mdate4,mdate4
        elif numero == '5':
            time,capteur_numero,date_max,date_min = time5,capteur_5,Mdate5,mdate5
        elif numero == '6':
            time,capteur_numero,date_max,date_min = time6,capteur_6,Mdate6,mdate6
        
       # Problème
        if start_date<date_min or end_date>date_max :
            return('Dates non valides')
        
            
        if variable == 'Température':
            df = capteur_numero.set_index(['sent_at'])
            selection = df.loc[ start_date : end_date ]
            L = selection.temp.tolist()
            
            plt.figure("Courbe de la température en fonction du temps")
            plt.gcf().subplots_adjust(left = 0.1, bottom = 0.5, right = 0.9, top = 0.95, wspace = 0, hspace = 0)
            plt.plot(time,capteur_numero.temp)
            
            plt.title('Température en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                       
            plt.ylabel('Température (°C)')

            plt.annotate('minimum :', xycoords = 'figure fraction', xy = (0.025, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(minimum(L), xycoords = 'figure fraction', xy = (0.15,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('maximum :', xycoords = 'figure fraction', xy = (0.025, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(maximum(L), xycoords = 'figure fraction', xy = (0.15,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('moyenne :', xycoords = 'figure fraction', xy = (0.27, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(moyenne(L), xycoords = 'figure fraction', xy = (0.37,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('mediane :', xycoords = 'figure fraction', xy = (0.27, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(mediane(L), xycoords = 'figure fraction', xy = (0.37,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('variance :', xycoords = 'figure fraction', xy = (0.65, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(variance(L), xycoords = 'figure fraction', xy = (0.76,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')  
            plt.annotate('ecart-type :', xycoords = 'figure fraction', xy = (0.65, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(ecart_type(L), xycoords = 'figure fraction', xy = (0.76,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')  
    
            plt.show()
            
        elif variable == 'Bruit' :
            df = capteur_numero.set_index(['sent_at'])
            selection = df.loc[ start_date : end_date ]
            L = selection.noise.tolist()
            
            plt.figure("Courbe du bruit en fonction du temps")
            plt.gcf().subplots_adjust(left = 0.1, bottom = 0.5, right = 0.9, top = 0.95, wspace = 0, hspace = 0)
            plt.plot(time,capteur_numero.noise)
            
            plt.title('Bruit en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                      
            plt.ylabel('Bruit (en dBA)')
            
            plt.annotate('minimum :', xycoords = 'figure fraction', xy = (0.025, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(minimum(L), xycoords = 'figure fraction', xy = (0.15,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('maximum :', xycoords = 'figure fraction', xy = (0.025, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(maximum(L), xycoords = 'figure fraction', xy = (0.15,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('moyenne :', xycoords = 'figure fraction', xy = (0.27, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(moyenne(L), xycoords = 'figure fraction', xy = (0.37,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('mediane :', xycoords = 'figure fraction', xy = (0.27, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(mediane(L), xycoords = 'figure fraction', xy = (0.37,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('variance :', xycoords = 'figure fraction', xy = (0.65, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(variance(L), xycoords = 'figure fraction', xy = (0.76,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')  
            plt.annotate('ecart-type :', xycoords = 'figure fraction', xy = (0.65, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(ecart_type(L), xycoords = 'figure fraction', xy = (0.76,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')     
            
            plt.show()
            
        elif variable == 'Luminosité' :
            df = capteur_numero.set_index(['sent_at'])
            selection = df.loc[ start_date : end_date ]
            L = selection.lum.tolist()
            
            plt.figure("Courbe de la luminosité en fonction du temps")
            plt.gcf().subplots_adjust(left = 0.1, bottom = 0.5, right = 0.9, top = 0.95, wspace = 0, hspace = 0)
            plt.plot(time,capteur_numero.lum)
            
            plt.title('Luminosité en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                       
            plt.ylabel('Luminosité (en lux)')
            
            plt.annotate('minimum :', xycoords = 'figure fraction', xy = (0.025, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(minimum(L), xycoords = 'figure fraction', xy = (0.15,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('maximum :', xycoords = 'figure fraction', xy = (0.025, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(maximum(L), xycoords = 'figure fraction', xy = (0.15,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('moyenne :', xycoords = 'figure fraction', xy = (0.27, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(moyenne(L), xycoords = 'figure fraction', xy = (0.37,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('mediane :', xycoords = 'figure fraction', xy = (0.27, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(mediane(L), xycoords = 'figure fraction', xy = (0.37,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('variance :', xycoords = 'figure fraction', xy = (0.65, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(variance(L), xycoords = 'figure fraction', xy = (0.76,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')  
            plt.annotate('ecart-type :', xycoords = 'figure fraction', xy = (0.65, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(ecart_type(L), xycoords = 'figure fraction', xy = (0.76,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            
            plt.show()
        
        elif variable == 'CO2' :
            df = capteur_numero.set_index(['sent_at'])
            selection = df.loc[ start_date : end_date ]
            L = selection.co2.tolist()
            
            plt.figure("Courbe de CO2 en fonction du temps")
            plt.gcf().subplots_adjust(left = 0.1, bottom = 0.5, right = 0.9, top = 0.95, wspace = 0, hspace = 0)
            plt.plot(time,capteur_numero.co2)
                
            plt.title('Teneur en CO2 en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                       
            plt.ylabel('Teneur en CO2 (ppm)')
            
            plt.annotate('minimum :', xycoords = 'figure fraction', xy = (0.025, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(minimum(L), xycoords = 'figure fraction', xy = (0.15,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('maximum :', xycoords = 'figure fraction', xy = (0.025, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(maximum(L), xycoords = 'figure fraction', xy = (0.15,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('moyenne :', xycoords = 'figure fraction', xy = (0.27, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(moyenne(L), xycoords = 'figure fraction', xy = (0.37,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('mediane :', xycoords = 'figure fraction', xy = (0.27, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(mediane(L), xycoords = 'figure fraction', xy = (0.37,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('variance :', xycoords = 'figure fraction', xy = (0.65, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(variance(L), xycoords = 'figure fraction', xy = (0.76,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')  
            plt.annotate('ecart-type :', xycoords = 'figure fraction', xy = (0.65, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(ecart_type(L), xycoords = 'figure fraction', xy = (0.76,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            
            plt.show()
        
        elif variable == 'Humidité' :
            df = capteur_numero.set_index(['sent_at'])
            selection = df.loc[ start_date : end_date ]
            L = selection.humidity.tolist()
            
            plt.figure("Courbe de l'humidité en fonction du temps")
            plt.gcf().subplots_adjust(left = 0.1, bottom = 0.5, right = 0.9, top = 0.95, wspace = 0, hspace = 0)
            plt.plot(time,capteur_numero.humidity)
            
            plt.title('Humidité relative en fonction du temps', color='r')
            plt.xlabel('Date')        
            plt.xticks(rotation='vertical') 
            plt.xlim(start_date, end_date)                       
            plt.ylabel('Humidité relative (en %)')
            
            plt.annotate('minimum :', xycoords = 'figure fraction', xy = (0.025, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(minimum(L), xycoords = 'figure fraction', xy = (0.15,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('maximum :', xycoords = 'figure fraction', xy = (0.025, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(maximum(L), xycoords = 'figure fraction', xy = (0.15,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('moyenne :', xycoords = 'figure fraction', xy = (0.27, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(moyenne(L), xycoords = 'figure fraction', xy = (0.37,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('mediane :', xycoords = 'figure fraction', xy = (0.27, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(mediane(L), xycoords = 'figure fraction', xy = (0.37,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')
            plt.annotate('variance :', xycoords = 'figure fraction', xy = (0.65, 0.09), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(variance(L), xycoords = 'figure fraction', xy = (0.76,0.09), fontsize=7, color = 'blue', backgroundcolor = 'white')  
            plt.annotate('ecart-type :', xycoords = 'figure fraction', xy = (0.65, 0.05), fontsize=7, color = 'g', backgroundcolor = 'white')
            plt.annotate(ecart_type(L), xycoords = 'figure fraction', xy = (0.76,0.05), fontsize=7, color = 'blue', backgroundcolor = 'white')

            plt.show()
            
        else :
            return("La variable choisie n'existe pas...")
    
    else :              #Mauvais capteur
        return('Capteur non existant')

