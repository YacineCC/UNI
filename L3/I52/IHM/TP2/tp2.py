from tkinter import filedialog
import tkinter as tk

x = 0
y = 0
CoordsLigne = []
idligne = 0

"""Définition de fonctions"""

def Quitter(event=None):
    root.destroy()
def dessine_ligne(event=None):
    global x,y,CoordsLigne, idligne
    x = event.x
    y = event.y
    CoordsLigne += [x,y]
    if(len(CoordsLigne) > 2):
        paintCanv.create_line(tk._flatten(CoordsLigne),width = 10,joinstyle = tk.ROUND, tags=("ligne",idligne))
        idligne = idligne +1
    print(idligne)
def change_couleur(event=None):
    ident = paintCanv.find_withtag("current")

    paintCanv.itemconfig(ident, fill="red")
def bouge(event = None):
    ident = paintCanv.find_withtag("current")

    paintCanv.moveto(ident,event.x,event.y)#event.x, event.y)


def get_origin(event=None):
    global x,y
    x = eventorigin.x
    y = eventorigin.y


"""________________________"""





#test = filedialog.askopenfilename()




"""Création d'une root de petite taille pour pas qu'elle gêne"""
root = tk.Tk()
root.title("ROOT")
root.geometry("10x10+10+10")
root.minsize(10,10)
root.maxsize(10,10)


"""Création d'une toplevel"""
paint = tk.Toplevel(root)
paint.title("Paint")
paint.geometry("700x500+300+300")
paint.minsize(500,500)


"""Création de la frame qui englobe le Canvas et le label"""
paintFrame = tk.Frame(paint, width = "5m", relief = "ridge", borderwidth = 2)


"""Création du canvas dans """
paintCanv = tk.Canvas(paintFrame, width = paint.winfo_reqwidth(), height = paint.winfo_reqheight(), bg = "white")

paintCanv.configure(width = paint.winfo_reqwidth())

"""Création du label"""
ch = "test"
lab = tk.StringVar(paintCanv, ch)
paintLabel = tk.Label(paintFrame, textvariable = lab)


"""Affichage de la frame contenant le Canvas et le label"""
paintCanv.pack(expand=True, fill="both")
paintLabel.pack(side="bottom")
paintFrame.pack(expand=True, fill = "both")

"""Binds"""
root.bind_all("<Control-c>", Quitter)

"""______"""

paintCanv.bind("<Control Button 1>", dessine_ligne)
paintCanv.bind("<Button 1>", change_couleur)
paintCanv.bind("<B3-Motion>", bouge)


def motion(event=None):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

paintCanv.bind("<Button 3>", motion)

if __name__=="__main__":
    root.mainloop()
