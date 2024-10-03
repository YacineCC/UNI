import tkinter as tk

def affiche_aide(event = None):
    aide.create_text(10, 10, text="Règles du jeu")

if __name__=="__main__":
    acceuil_root = tk.Tk()
    acceuil_root.title("En Garde !")
    acceuil_root.geometry("1000x1000+10+10")
    # acceuil_root.minsize(1000,1000)
    
    aide = tk.Button(acceuil_root, text = "Aide", command = affiche_aide).pack(side="top", anchor="nw", padx= 15)

    acceuil_frame_choix = tk.Frame(acceuil_root, width = "3m", relief = "ridge", borderwidth = 2)
    acceuil_choix_canv_height = 500 
    acceuil_choix_canv_width = 300 
    acceuil_choix_mode_canv = tk.Canvas(acceuil_frame_choix, width = acceuil_choix_canv_width, height = acceuil_choix_canv_height, bg = "red").pack(side = "left")
    acceuil_choix_nom_canv = tk.Canvas(acceuil_frame_choix, width = acceuil_choix_canv_width, height = acceuil_choix_canv_height, bg = "blue").pack(side = "right")

    acceuil_frame_commencer = tk.Frame(acceuil_root, width = "3m", relief = "ridge", borderwidth = 2)

    acceuil_commencer_canv = tk.Canvas(acceuil_frame_commencer, width = acceuil_choix_canv_width*2, height = acceuil_choix_canv_height//2, bg = "green").pack(side = "bottom")

    boutton_commencer = tk.Button(acceuil_commencer_canv, text = "Commencer").pack(side = "bottom", anchor = "center")

    acceuil_frame_choix.pack(side = "top", anchor = "center")
    acceuil_frame_commencer.pack(side = "top", anchor = "center")

    #menu_choix_mode = tk.Menu(
    #acceuil_frame_choix.add_radiobutton(label="Basique", value = "basique").pack()


    acceuil_root.mainloop()
