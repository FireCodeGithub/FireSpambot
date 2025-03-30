import tkinter as tk
import subprocess

def lancer_backend():
    """
    Lance le script backend.py avec les paramètres entrés par l'utilisateur.
    """
    texte = entree_texte.get()
    delai = entree_delai.get()
    repetitions = entree_repetitions.get()  # Nombre de répétitions
    retour_ligne = retour_ligne_var.get()  # Récupère la valeur de la case à cocher
    vitesse_ecriture = entree_vitesse_ecriture.get() #récupère la vitesse d'écriture

    # Lance le processus backend avec les paramètres
    try:
        if vitesse_ecriture: #vérifie si l'utilisateur a entré une vitesse d'écriture
            subprocess.Popen(
                ["python", "backend.py", texte, delai, repetitions, vitesse_ecriture, str(retour_ligne)]
            )
        else:
             subprocess.Popen(
                ["python", "backend.py", texte, delai, repetitions, str(retour_ligne)]
            )
    except FileNotFoundError:
        print(
            "Erreur : Le fichier backend.py est introuvable. Assurez-vous qu'il se trouve dans le même répertoire."
        )
        return
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
        return

fenetre = tk.Tk()
fenetre.title("Contrôle du clavier")

label_texte = tk.Label(fenetre, text="Texte à écrire :")
label_texte.pack()
entree_texte = tk.Entry(fenetre)
entree_texte.pack()

label_delai = tk.Label(fenetre, text="Délai (en secondes) :")
label_delai.pack()
entree_delai = tk.Entry(fenetre)
entree_delai.pack()

label_repetitions = tk.Label(fenetre, text="Répétitions :")
label_repetitions.pack()
entree_repetitions = tk.Entry(fenetre)
entree_repetitions.pack()

# Ajout de la case à cocher pour le retour à la ligne
retour_ligne_var = tk.IntVar()  # Variable pour stocker l'état de la case à cocher
case_retour_ligne = tk.Checkbutton(
    fenetre, text="Retour à la ligne", variable=retour_ligne_var
)
case_retour_ligne.pack()

label_vitesse_ecriture = tk.Label(fenetre, text="Vitesse d'écriture (secondes):")
label_vitesse_ecriture.pack()
entree_vitesse_ecriture = tk.Entry(fenetre)
entree_vitesse_ecriture.pack()

bouton_lancer = tk.Button(fenetre, text="Lancer", command=lancer_backend)
bouton_lancer.pack()

fenetre.mainloop()
