import tkinter as tk

PARAMETRES_JEU = [-1]*4

def config_valide():
    flg = True
    if(PARAMETRES_JEU[1] == PARAMETRES_JEU[2]):
        flg = False
    for x in PARAMETRES_JEU:
        if x == -1:
            flg = False
    return flg

def affiche_aide(event = None):
    boutton_aide.create_text(10, 10, text="Règles du jeu")

def parametre_choix_joueur():
    PARAMETRES_JEU[3] = choix_joueur.get()
    
def parametre_choix_joueur1():
    PARAMETRES_JEU[1] = entry_choix_nom_joueur1.get()
    
def parametre_choix_joueur2():
    PARAMETRES_JEU[2] = entry_choix_nom_joueur2.get()

def parametre_choix_regles():
    PARAMETRES_JEU[0] = choix_regles.get()    

def commencer():
    if(config_valide()):
        print(PARAMETRES_JEU)
        root.withdraw()
        arene = tk.Toplevel(root, bg="yellow").pack()
        
    else:
        print("Config Non valide")

   

if __name__=="__main__":


    

    #Root
    #Création de la fenêtre d'acceuil.
    root = tk.Tk()
    root.title("En Garde !")
    root.geometry("1000x1000+10+10")
    root.maxsize(600, 800)

    #Variables
    #Choix des règles.
    choix_regles = tk.StringVar()
    #Qui commence.   
    choix_joueur = tk.IntVar()      
    
    #Frames
    #L'acceuil est en trois parties, deux rectangles bleu et rouge en longueur, et en dessous un rectangle vert en largeur.
    frame_root = tk.Frame(root, width = "3m", relief = "ridge", borderwidth = 2)
    frame_root_choix_regles = tk.Frame(frame_root, width = "3m", relief = "ridge", borderwidth = 2, bg="red")
    frame_root_choix_nom_joueur = tk.Frame(frame_root, width = "3m", relief = "ridge", borderwidth = 2, bg="blue")
    frame_root_commencer = tk.Frame(frame_root, width = "3m", relief = "ridge", borderwidth = 2, bg="green")

    
    
    #Bouttons
    #Boutton d'aide dans le coin supérieur gauche de l'acceuil.
    boutton_aide = tk.Button(root, text = "Aide", command = affiche_aide).pack(side="top", anchor="nw", padx= 15)

    #Bouttons qui servent a valider le nom des joueurs.
    boutton_choix_nom_joueur1 = tk.Button(frame_root_choix_nom_joueur,text="Valider",command=parametre_choix_joueur1)
    boutton_choix_nom_joueur2 = tk.Button(frame_root_choix_nom_joueur,text="Valider",command=parametre_choix_joueur2)
    #Boutton qui commence le jeu, les paramètres du jeux (règles, qui commence, nom joueurs) doivent tous être connus.
    boutton_commencer = tk.Button(frame_root_commencer, text = "Commencer", borderwidth=7, relief="sunken", height=2, width=10, command=commencer)


    #RadioBouttons
    #Choix des règles
    radio_regles_classique = tk.Radiobutton(frame_root_choix_regles, text="Classique", var=choix_regles, value ="classique", command=parametre_choix_regles)
    radio_regles_avancee = tk.Radiobutton(frame_root_choix_regles, text="Avancee", var = choix_regles, value = "avancee", command=parametre_choix_regles)
    radio_regles_basique = tk.Radiobutton(frame_root_choix_regles, text="Basique", var= choix_regles, value = "basique", command=parametre_choix_regles)
    #Qui commence.
    radio_choix_joueur1 = tk.Radiobutton(frame_root_commencer, text="Joueur 1", var=choix_joueur, value =1, command=parametre_choix_joueur)
    radio_choix_joueur2 = tk.Radiobutton(frame_root_commencer, text="Joueur 2", var=choix_joueur, value =2, command=parametre_choix_joueur)
    radio_choix_joueur_hasard = tk.Radiobutton(frame_root_commencer, text="Au hasard", var=choix_joueur, value =3, command=parametre_choix_joueur)

    #Labels
    label_choix_joueur = tk.Label(frame_root_commencer, text="Choix Joueur")
    label_regles = tk.Label(frame_root_choix_regles, text="Règles")
    label_choix_nom_joueur1 = tk.Label(frame_root_choix_nom_joueur,text="Joueur 1")
    label_choix_nom_joueur2 = tk.Label(frame_root_choix_nom_joueur,text="Joueur 2")

    #Entrys
    entry_choix_nom_joueur1 = tk.Entry(frame_root_choix_nom_joueur)
    entry_choix_nom_joueur2 = tk.Entry(frame_root_choix_nom_joueur)


    
    
    #Affichage
    
    frame_root.pack(fill="both", expand=True)
    #Il faut d'abord afficher la frame du bas.
    frame_root_commencer.pack(side = "bottom", fill = "both")
    #Puis les deux frames qui scindent la frame
    frame_root_choix_regles.pack(side = "left", expand = True, fill = "both")
    frame_root_choix_nom_joueur.pack(side = "right", expand = True, fill = "both")



    
    
    label_regles.pack()
    radio_regles_basique.pack()
    radio_regles_classique.pack()
    radio_regles_avancee.pack()

    label_choix_nom_joueur1.pack()
    entry_choix_nom_joueur1.pack()
    boutton_choix_nom_joueur1.pack()


    label_choix_nom_joueur2.pack()
    entry_choix_nom_joueur2.pack()
    boutton_choix_nom_joueur2.pack()

    label_choix_joueur.pack()
    radio_choix_joueur1.pack()
    radio_choix_joueur2.pack()
    radio_choix_joueur_hasard.pack()
    boutton_commencer.pack()
    

    root.mainloop()
