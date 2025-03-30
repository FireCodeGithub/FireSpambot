import sys
import time
from pynput.keyboard import Controller
from pynput.keyboard import Key

# Gestion des erreurs : vérifie si les arguments sont présents
if len(sys.argv) < 4:
    print("Usage : python backend.py <texte> <delai> <répétitions> [<vitesse_ecriture>] [<retour_ligne>]")
    print("        <texte>: Le texte à écrire.")
    print("        <delai>: Le délai initial avant de commencer à écrire (en secondes).")
    print("        <répétitions>: Le nombre de fois que le texte sera répété.")
    print("        <vitesse_ecriture>: (Optionnel) Le délai entre chaque caractère (en secondes, par défaut 0.03).")
    print("        <retour_ligne>: (Optionnel) Indique si un retour à la ligne doit être ajouté après chaque répétition (1 pour Oui, 0 pour Non, par défaut 0).")
    sys.exit(1)

texte = sys.argv[1]
try:
    delai = float(sys.argv[2])
except ValueError:
    print("Erreur : Le délai doit être un nombre.")
    sys.exit(1)
try:
    repetitions = int(sys.argv[3])
except ValueError:
    print("Erreur : Le nombre de répétitions doit être un entier.")
    sys.exit(1)

vitesse_ecriture = 0.03
if len(sys.argv) > 4:
    try:
        vitesse_ecriture = float(sys.argv[4])
    except ValueError:
        print("Erreur : La vitesse d'écriture doit être un nombre.")
        sys.exit(1)

retour_ligne = 0
if len(sys.argv) > 5:
    try:
        retour_ligne = int(sys.argv[5])
        if retour_ligne not in (0, 1):
            print("Erreur : Le retour à la ligne doit être 0 ou 1.")
            sys.exit(1)
    except ValueError:
        print("Erreur : Le retour à la ligne doit être 0 ou 1.")
        sys.exit(1)

keyboard = Controller()

time.sleep(delai)
total_caracteres = len(texte) * repetitions
caracteres_ecrits = 0
while repetitions > 0:
    for char in texte:
        keyboard.type(char)
        time.sleep(vitesse_ecriture)
        caracteres_ecrits += 1
        progression = int((caracteres_ecrits / total_caracteres) * 100)
        print(f"PROGRESS:{progression}")  # Envoie la progression à la sortie standard
        sys.stdout.flush()
    if retour_ligne == 1:
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    repetitions -= 1
