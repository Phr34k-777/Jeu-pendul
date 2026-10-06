"""
Ce fichier contient le jeu du pendu.
Il s'appuie sur les fichiers :
-donnes.py
-fonctions.py
"""

from donnees import *
from fonctiones import *

# On récupère les scores de la partie
scores = récupérer_scores()

# On récupère un nom d'utilisateur
utilisateur = récupérer_nom_utilisateur()

# Si l'utilisateur n'a pas encore de score, on l'ajoute
if utilisateur not in scores.keys():
    scores[utilisateur] = 0 # 0 point pour commencer
    
# Notre variable pour savoir quand arrêterr la partie
continuer_partie = 'o'

while continuer_partie != 'n':
    print(f"Joueur {utilisateur}: {scores[utilisateur]} point(s)")
    mot_à_trouver = choisir_mot()
    lettres_trouvées = set()
    mot_trouvé = récupérer_mot_masqué(mot_à_trouver, lettres_trouvées)
    nb_chances = NB_COUPS
    while mot_à_trouver != mot_trouvé and nb_chances > 0:
        print(f"Mot à trouver {mot_trouvé} (encore {nb_chances} chances)")
        lettre = récupérer_lettre()
        if lettre in lettres_trouvées: # La lettre a déjà été choisie
            print("Vous avez déjà choisi cette lettre.")
        elif lettre in mot_à_trouver: # La lettre est dans le mot à trouver
            print("Bien joué")
        else:
            nb_chances -= 1
            print("... non, cette lettre ne se trouve pas dans le mot...")
            lettres_trouvées.add(lettre)
            mot_trouvé = récupérer_mot_masqué(mot_à_trouver, lettres_trouvées)
        
    # A-t-on trouvé le mot ? nos chances sont-elles épuisées ?
    if mot_à_trouver == mot_trouvé:
        print(f"Félicitations ! Vous avez trouvé le mot {mot_à_trouver}.")
    else:
        print("PERDU !!! Vous avez perdu.")
            
    # On met à jour le score de l'utilisateur
    scores[utilisateur] += nb_chances
    continuer_partie = input("Souhaitez-vous continuer la partie (O/N) ? ") 
    continuer_partie = continuer_partie.lower()

# La partie est finie, on enregistre les scores
enregistrer_scores(scores)

# On affiche les scores de l'utilisateur
print(f"Vous finissez la partie avec {scores[utilisateur]} points.")        
                           