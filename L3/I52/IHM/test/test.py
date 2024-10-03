import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter.ttk import *
root = tk.Tk()
"""
# configuration de la fenetre via le WM
root.geometry("500x375+10+10") # dimension et position par defaut
root.title("Une fenetre") # titre de la fenetre
root.minsize(400, 300) # taille minimum de la fenetre
root.maxsize(1024,768) # taille maximum de la fenetre
root.positionfrom("user") # placement manuel de la fenetre
root.sizefrom("user") # dimensionnement manuel de la fenetre
root.protocol("WM_DELETE_WINDOW", root.destroy) # evenement WM
# creation d’une fenetre toplevel de nom tl1
tl1 = tk.Toplevel(root)# une toplevel depend de la root window
tl1.geometry("300x300+10+10")
tl1.title("fils")
tl1.minsize(100,100)
tl1.maxsize(1000,1000)
tl2 = tk.Toplevel(tl1)



# on cree 5 cadres d’aspect different
fr = {}
for relief in ("raised", "sunken", "flat", "groove", "ridge"):
    # creation d’une frame fille de la fenetre principale root
    fr[relief] = tk.Frame(root, width="15m", height="10m", relief=relief, borderwidth=4)
    # chaque nouvelle frame est placee a droite de la precedente
    fr[relief].pack(side="left", padx="2m", pady="2m")
fr["flat"].configure(background="black")



for mesg in ("Ok", "Apply", "Cancel", "Help"):
    # chaque bouton est place a gauche (!) dans la zone
    # non occupee par le bouton precedent (a sa droite)
    tk.Button(text=mesg).pack(side="left")
vcb = {}
for txt in ("gras", "italique", "souligne"):
    vcb[txt] = tk.BooleanVar()
    tk.Checkbutton(text=txt.capitalize(), variable=vcb[txt],anchor="w").pack(side="top", fill="x")


police = tk.StringVar()
for txt in ("times", "helvetica", "courier", "symbol"):
    tk.Radiobutton(text=txt.capitalize(), variable=police,
    value=txt, anchor="w").pack(side="top", fill="x")
police.set("courier")


# menu bouton : lettre T soulignee et raccourci clavier Alt-t
mbtxt=tk.Menubutton(root, text="Texte", underline=0)
# menu associe
menu1=tk.Menu(mbtxt, tearoff=False)
m1cb = {}
for txt in ("gras", "italique", "souligne"):
    m1cb[txt] = tk.BooleanVar()
    menu1.add_checkbutton(label=txt.capitalize(), variable=m1cb[txt])
menu1.add_separator()
police=tk.StringVar()
menu1.add_radiobutton(label="Times", variable=police, value="times")
menu1.add_radiobutton(label="Symbol", variable=police, value="symbol")

#menu1.add_command(label="Marges et tabulations", command=Page)
mbtxt["menu"]=menu1 # options accessibles via un dico
mbtxt.pack()
tk.Message(width="8c", justify="left", relief="raised", bd=2,font="-Adobe-Helvetica-Medium-R-Normal--*-180-*",text="Tkinter est vraiment un outil formidable de developpement d’interface graphique").pack()
"""
lc=tk.Listbox(height=6)
sc=tk.Scrollbar(command=lc.yview)
sc.pack(side="right", fill="y")
lc.configure(yscrollcommand=sc.set)
lc.pack()
fd=open("/etc/X11/rgb.txt", 'r')
li=fd.readline() # on saute la 1ere ligne
li=fd.readline()
while li!='':
    lc.insert(tk.END,li.split('\t')[2].strip(" \n"))
    li=fd.readline()
fd.close()
def lc_bg_color(event=None):
    selec=lc.curselection()
    lc.configure(background=lc.get(selec[0]))
lc.bind('<Double-Button-1>', lc_bg_color)





tk.Label(text="Nom du fichier : ").pack(side="left", padx="1m",pady="2m")
nomfic=tk.StringVar()
tk.Entry(width=20, relief="sunken", bd=2, textvariable=nomfic).pack(side="left", padx="1m", pady="2m")



txt=tk.Text()
txt.pack(side="top", expand=True, fill="both")
fd=open("lorem.txt", 'r')
li=fd.readline()
while li!='':
    txt.insert(tk.END, li)
    li=fd.readline()
fd.close()
# configuration des styles de polices
txt.tag_config("pnom", font="Courier 12")
txt.tag_config("pbold", font="Courier 12 bold")
txt.tag_add("pbold", 4.9, 4.33)


# creation
canv=tk.Canvas(width=320, height=240, bg="white")
canv.pack()
# creation d’un rectangle rouge, defini par deux sommets
# la commande create retourne l’indice du rectangle dans le canvas
lobj=[]
lobj.append(canv.create_rectangle(10, 10, 200, 50, fill="red"))
# le rectangle devient bleu
canv.itemconfig(lobj[-1], fill="blue")

# dessin des carres de couleur
coul = ["purple", "blue", "green", "orange", "yellow"]
for i in range(101):
    for j in range(101):
        canv.create_rectangle(i, j, i+10, j+10, fill=coul[i%5], tags=("couleur", coul[i%5]))
        

def affiche_couleur(event=None):
    #nonlocal choixcoul
    id = canv.find_withtag("current")
    #choixcoul.set(canv.gettags(id)[1])
canv.tag_bind("couleur", "<1>", affiche_couleur)

def obj_get_centre(pid):
    """centre geometrique de l’objet pid en coordonnees entieres"""
    lcoord = canv.coords(pid)
# calcul de la somme des abscisses et des ordonnees
    #...
    n = len(lcoord)/2 # nombre de sommets
    return int(x/n), int(y/n)
tk.messagebox.askokcancel(title="test",message="test")
tk.filedialog.askopenfilename()
colorchooser.askcolor(color="#6A9662",title = "Palette a moi que j'ai")

style = tk.ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
l1 = tk.ttk.Label(text="Test", style="BW.TLabel")


canv=tk.Canvas(width=320, height=240, bg="white")
canv.pack()
canv.create_rectangle(50, 50, 200, 200, fill="red", tags="clic")
# rem : canv.addtag_withtag("clic", 1)
def Couleur(event):
    id = canv.find_withtag("current")
    
    canv.itemconfig(id, fill="blue")
canv.tag_bind("clic", "<1>", Couleur)
canv.tag_bind("clic", "<1>", Couleur)

root.wait_window(root)
