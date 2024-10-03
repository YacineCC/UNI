import tkinter as tk

"""Renvoie un dico[nomcouleur] = tupleRGB, lit le fichier ligne par ligne et le parse, gère les doublons /etc/X11/rgb.txt/"""
def lire_rgb():
    f = open("/etc/X11/rgb.txt", 'r')
    f.readline()
    dico = {}
    ligne = f.readline()    #Lit la premiere ligne pas utile

    while(ligne != ""): # Tant qu'il y a des lignes dans le fichier

        tmptab = ligne.lower().split()
        tmptuple = (tmptab[0], tmptab[1], tmptab[2])
        nomcoul = ""
        for c in tmptab[3:]:    #Dans le cas d'un nom de couleur composé
            nomcoul += c
        if(tmptuple not in dico.values()):  #Gestion des doublons
            dico[nomcoul] = tmptuple
        ligne = f.readline()

    dicolist = sorted(dico)
    return dicolist,dico

def dessine_carre(x, y, taille, couleur):

        tl1canv.create_rectangle(x, y, x + taille, j + taille, fill=couleur, tags=("carres", couleur)) 

def affiche_couleur(event=None):
    #selec = tl1canv.curselection()
    ident = tl1canv.find_withtag("current")
    test = tl1canv.gettags(ident)
    lab.set(str(test[1]) + str(dico[1][test[1]]))


def Quitter(event=None):
    root.destroy()

root = tk.Tk()  #Creation de root
root.title("Root")
root.geometry("100x10+10+10")
root.minsize(100,10)
root.maxsize(10,10)

tl1 = tk.Toplevel(root) #Creation de toplevel1
tl1.title("Toplevel1")
tl1.geometry("300x200+50+50")
tl1.minsize(150,100)


tl1frame = tk.Frame(tl1, width = "15m", relief = "ridge", borderwidth=4)
#Label
ch= "choix couleur"
lab = tk.StringVar(tl1frame, ch)

tl1label = tk.Label(tl1frame, textvariable = lab)
tl1label.pack(side="top",anchor="w")


#Frame
tl1bouttonframe = tk.Frame(tl1frame, width = "15m", relief = "ridge", borderwidth=4)

#Boutons Ok et Annuler
tk.Button(tl1bouttonframe, text="Ok", command=affiche_couleur).pack(side="left")
tk.Button(tl1bouttonframe, text="Annuler", command=Quitter).pack(side="left")
tl1bouttonframe.pack(side="bottom", padx="2m", pady="2m")

tl1canvframe = tk.Frame(tl1frame, width = "15m", relief = "ridge", borderwidth=4)
 

taille = 30
nbcarreaux = 7 #Nb de cases de couleurs par lignes
tl1canv = tk.Canvas(tl1canvframe, width = nbcarreaux*taille + 2 * nbcarreaux, height = nbcarreaux*taille, bg = "white")

dico = lire_rgb()


#for i in range(0,400,10):
#    for j in range(0,400,10):
#        tl1canv.create_rectangle(j, i, j+10, i+10, fill=tab[(i*j)%lendico], tags=("carres",tab[(i*j)%lendico]))
    
i = 1
j = 1
for key in dico[0]:
    if(i >= int(tl1canv.cget("width"))): #5 couleurs par lignes puis on passe à la ligne suivante
        i = 1
        j += 2+taille
    try: 
        dessine_carre(i, j, taille, key)
    except tk.TclError:
        continue

    i += 2+taille

#scrollbar 
sc = tk.Scrollbar(tl1canvframe, command=tl1canv.yview)
tl1canv.configure(yscrollcommand=sc.set)
tl1canv.configure(scrollregion = tl1canv.bbox("all"))
tl1canv.pack(side="left")
sc.pack(side="right", fill="y")
tl1canvframe.pack(side="top")
tl1frame.pack()

tl1canv.bind("<Button 1>", affiche_couleur)
tl1canv.tag_bind("couleur", "<1>", affiche_couleur)
root.bind_all("<Control-c>", Quitter)



if __name__=="__main__":
    root.mainloop()


