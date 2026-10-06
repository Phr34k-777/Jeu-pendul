"""
Ce fichier définit des fonctions utiles pour le programme
du pendu.On utilise les données du programme contenues dans donnees.py.
"""
from pathlib import Path
import pickle
from random import choice
from donnees import *
# Gestiondesscores

def récupérer_scores()-> dict[str,int]:
    
    """
    Cette fonction récupère les scores enregistrés si le
    fichier existe.
    Dans tous les cas,on renvoie un dictionnaire,soit l'objet dépicklé, soit un dictionnaire vide.
    On s'appuie sur NOM_FICHIER_SCORES défini dans donnees.py.

    """
    chemin_scores = Path(NOM_FICHIER_SCORES)
    if chemin_scores.exists(): # Le fichier existe
        # On le récupère
        with chemin_scores.open("rb") as fichier_scores:
            scores=pickle.load(fichier_scores)
    else: # Le fichier n'existe pas
        scores={}
    return scores  

def enregistrer_scores(scores: dict[str, int]):
    """
    Cette fonction se charge d'enregistrer les scores dans le fichier
    NOM_FICHIER_SCORES. Elle reçoit en paramètre le dictionnaire
    des scores à enregistrer.
    
    """   
    chemin_scores = Path(NOM_FICHIER_SCORES)
    with chemin_scores.open("wb") as fichier_scores: # On écrase les anciens scores
        pickle.dump(scores, fichier_scores)
        
# Fonctions gérant les éléments saisis par l'utilisateur

def récupérer_nom_utilisateur() -> str:
    """ Fonction chargée de récupérer le nom de l'utilisateur. 
        Il doit être composé de 4 caratères minimum,
        chiffres et lettres exclusivement.
        Si ce nom n'est pas valide, on appelle récursivement la fonction
        pour en obtenir un nouveau.
    """
    nom_utilisateur = input("Tapez votre nom :")
    # On met la première lettre en majuscule et les autres en minuscules 
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur) < 4:
        print("Ce nom est invalide.")
        # On appelle de nouveau la foncton pour avoir un autre nom
        return récupérer_nom_utilisateur()
    else:
        return nom_utilisateur
    
def récupérer_lettre() -> str:
    """
    Cette fonction récupère une lettre saisie par l'utilisateur.
    Si la chaîne récupérer n'est pas une lettre, on appelle récursivement
    la fonction jusqu'a obtenir une lettre.
    """    
    lettre = input("Tapez une lettre :")
    lettre = lettre.lower()
    if len(lettre) > 1 or not lettre.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return récupérer_lettre()
    else:
        return lettre
    
# Fonctions de jeu de pendu 

def choisir_mot() -> str:
    """
    Cette fonction renvoie le mot choisi dans LISTE_MOTS.
    On utilise la fonction choice du module random
    """
    return choice(LISTE_MOTS)

def récupérer_mot_masqué(mot_complet: str, lettres_trouvées: set[str]) -> str:
    """
    Cette fonction renvoie un mot masqué tout ou en partie,en fonction:
    - du mot d'origine (type str)
    - des lettres déjà trouvées (type list)
    On renvoie le mot d'origine avec des * remplaçant les lettres
    que l'on n'a pas encore trouvées.
    """
    mot_masqué = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvées:
            mot_masqué += lettre
        else:
             mot_masqué += "*"
    return mot_masqué             