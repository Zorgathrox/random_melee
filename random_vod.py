import os
import sys
import requests
import random

#------------------------------------------------------------------------------------------------------

#Fonction realisant la création de la requête
def buildRequest(perso1,perso2=-2) :

    base_url = "https://vods.co/view/records?json={"
    end_url = ", hideSpoilers :false}"

    gameId = "4419" #Id de Melee

    selectionId = perso1 # Personnage 1
    selection2Id = perso2 # Personnage 2

    if selection2Id == -2 :
        parametres = f"gameId :{gameId}, selectionId :{selectionId}"        
    else :
        parametres = f"gameId :{gameId}, selectionId :{selectionId}, selection2Id :{selection2Id}"

    url_nb_pages = base_url + parametres + ", page :0" + end_url

    r_nbpages = requests.get(url_nb_pages)
    nb_pages = numberOfPages(r_nbpages.text)

    numero_page = random.randint(0,nb_pages) #Page choisie aleatoirement

    url_requete = base_url + parametres + f", page :{numero_page}" + end_url

    return(url_requete)

#Fonction déterminant le nombre total de pages renvoyées par la requête initiale.
def numberOfPages(texte_requete) :
    index_occurrence = texte_requete.find('data-total-pages=')
    texte_requete=texte_requete[index_occurrence:]
    texte_requete=texte_requete[:texte_requete.find('>')]
    texte_requete=texte_requete[texte_requete.find('"'):]
    nbPages=texte_requete.strip('"')
    return(int(nbPages))

#------------------------------------------------------------------------------------------------------

    # Personnages et leur id :
    # Fox 13
    # Falco 51
    # Marth 26
    # Sheik 8
    # Captain Falcon 29
    # Peach 47
    # Jigglypuff 19
    # Ice Climbers 63
    # Samus 34
    # Pikachu 11
    # Luigi 24
    # Ganondorf 41
    # Yoshi 10
    # Doc 55
    # DK 42
    # Link 37
    # Mario 4
    # Young Link 64
    # GW 7
    # Roy 23
    # Zelda 22
    # Pichu 65
    # Ness 20
    # Bowser 14
    # Kirby 35
    # Mewtwo 25

r = requests.get(buildRequest(26)) 
#Modifier la valeur dans buildRequest pour personnaliser la recherche
# Une seule valeur = sets contenant le personnage
# Exemple : Tous les sets de Marth : buildRequest(26)
# Deux valeurs = sets contenant les deux personnages
# Exemple : Tous les sets Sheik vs Captain Falcon : buildRequest(8,29)

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
placement = random.randint(0,len(liste_vods)-1) #Prend une vod random sur la page choisie

position_lien = liste_vods[placement].find('href')
lien_vod = liste_vods[placement][position_lien:]

#Fin du lien
position_lien = lien_vod.find('>')
lien_vod = lien_vod[0:position_lien]

lien_vod = lien_vod.replace('href=','href=https://vods.co/')

lien_vod = "<a " + lien_vod + '>Vod random</a>'

#Donner l'option de generer fichier ou non.
print(lien_vod.replace('<a href=','').replace('>Vod random</a>',''))