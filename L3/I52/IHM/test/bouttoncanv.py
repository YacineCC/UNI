import tkinter as tk

def commencer_jeu():
    nom_joueur = nom_entry.get()
    difficulte = difficulte_var.get()
    print(f"Nom du joueur : {nom_joueur}, Difficulté choisie : {difficulte}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Écran d'Accueil")

# Frame
frame = tk.Frame(fenetre)
frame.pack()

# Canvas inside the Frame
canvas = tk.Canvas(frame, width=400, height=300, bg="red")
canvas.pack()

# Champ pour entrer le nom du joueur
nom_label = tk.Label(canvas, text="Nom du Joueur:")
nom_label.pack()
nom_entry = tk.Entry(canvas)
nom_entry.pack(pady=5)

# Radio boutons pour la difficulté
difficulte_label = tk.Label(canvas, text="Choisissez la difficulté:")
difficulte_label.pack()

difficulte_var = tk.StringVar()
difficulte_facile = tk.Radiobutton(canvas, text="Facile", variable=difficulte_var, value="Facile")
difficulte_moyen = tk.Radiobutton(canvas, text="Moyen", variable=difficulte_var, value="Moyen")
difficulte_difficile = tk.Radiobutton(canvas, text="Difficile", variable=difficulte_var, value="Difficile")

difficulte_facile.pack()
difficulte_moyen.pack()
difficulte_difficile.pack()

# Bouton Commencer inside the Canvas
commencer_bouton = tk.Button(canvas, text="Commencer", command=commencer_jeu)
# Placer le bouton dans le canvas à la position spécifiée (100, 200)
canvas.create_window(100, 200, window=commencer_bouton)

# Lancer la boucle principale Tkinter
fenetre.mainloop()

