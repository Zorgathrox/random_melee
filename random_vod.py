import os
import sys
#import time
#import datetime
import requests
import random


numero_page = random.randint(0,95)
#Nombre max de pages de match de Marth. 
#On devrait ameliorer ça pour que ça soit dynamique en fonction des criteres
numero_vod = random.randint(0,59)
#Nombre max de vods par page.
#Voir si on peut moduler

#%22 = "
r = requests.get("https://vods.co/view/records?json={%22gameId%22:%224419%22,%22selectionId%22:%2226%22,%22page%22:"+str(numero_page)+",%22hideSpoilers%22:false}")

page_vod = str(r.text.encode("utf-8"))

page_vod = page_vod.replace('\\r\\n','')
page_vod = page_vod.strip('b\'')

#Position de la première occurrence dans la string
premiere_occurrence = page_vod.find(' <span class="match-record-side')

#Strip tout avant la string.
page_vod=page_vod[premiere_occurrence+1:]

liste_vods = page_vod.split('<span class="match-record-side-a')
liste_vods.pop(0)

for i in range(1,len(liste_vods)) :
    liste_vods[i] = '<span class="match-record-side-a' + liste_vods[i]

#Premiere occurence du lien
placement = numero_vod

position_lien = liste_vods[placement].find('href')
lien_vod = liste_vods[placement][position_lien:]

#Fin du lien
position_lien = lien_vod.find('>')
lien_vod = lien_vod[0:position_lien]

lien_vod = lien_vod.replace('href=','href=https://vods.co/')

lien_vod = "<a " + lien_vod + '>Vod random</a>'

#Donner l'option de generer fichier ou non.
print(lien_vod.replace('<a href=','').replace('>Vod random</a>',''))

###
#f = open("page_vod.html", "w")
#f.write(lien_vod) #Donner les informations du set.
#f.close()

#Proposer plusieurs vods ?

