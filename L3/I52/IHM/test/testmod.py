from tkinter import filedialog
import tkinter as tk

coords_lignes = []

def quitter(event=None):
    root.destroy()

def dessine_ligne(event=None):
    coords_lignes.append([])  
    coords_lignes[-1].extend([event.x, event.y])
    creer_ligne(coords_lignes)

def change_couleur(event=None):
    ident = paint_canv.find_withtag("current")
    paint_canv.itemconfig(ident, fill="red")

def bouge(event=None):
    if coords_lignes:
        ident = paint_canv.find_withtag("ligne")
        x1, y1, x2, y2 = paint_canv.coords(ident)
        delta_x = event.x - (x1 + x2) / 2
        delta_y = event.y - (y1 + y2) / 2
        paint_canv.move(ident, delta_x, delta_y)

def motion(event=None):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

def creer_ligne(coords):
    if len(coords) > 2:
        paint_canv.create_line(tk._flatten(coords), width=2, joinstyle=tk.ROUND, tags=("ligne"))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ROOT")
    root.geometry("10x10+10+10")
    root.minsize(10, 10)
    root.maxsize(10, 10)

    paint = tk.Toplevel(root)
    paint.title("Paint")
    paint.geometry("700x500+300+300")
    paint.minsize(500, 500)

    paint_frame = tk.Frame(paint, width="5m", relief="ridge", borderwidth=2)
    paint_canv = tk.Canvas(paint_frame, width=paint.winfo_reqwidth(), height=paint.winfo_reqheight(), bg="white")
    paint_canv.configure(width=paint.winfo_reqwidth())
    paint_label = tk.Label(paint_frame, text="")

    paint_canv.pack(expand=True, fill="both")
    paint_label.pack(side="bottom")
    paint_frame.pack(expand=True, fill="both")

    root.bind_all("<Control-c>", quitter)

    paint_canv.bind("<Control Button-1>", dessine_ligne)
    paint_canv.bind("<Button-1>", change_couleur)
    paint_canv.bind("<Button-3>", bouge)
    paint_canv.bind("<Button-2>", motion)

    root.mainloop()

