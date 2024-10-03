import tkinter as tk, point as poi, rectangle as rec, projection as pro


class Environement:
    """ Une classe qui contient une root, un canvas, une window et une viewport virtuelle
    pour éviter de passer pleins de paramètres ou avoir des variables globales"""

    def __init__(self, WindowCoor1 : poi.Point, WindowCoor2 : poi.Point, ViewportCoor1 : poi.Point, ViewportCoor2 : poi.Point):
        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        self.root_canvas = tk.Canvas(self.root, bg = "red")
        self.root.update()
        self.H_ecran = self.root.winfo_height()
        self.window = rec.Rectangle(WindowCoor1, WindowCoor2)

        self.viewport = rec.Rectangle(ViewportCoor1, ViewportCoor2)

        self.viewport_obj = creer_viewport(self.root_canvas, self.viewport, self.H_ecran) # création de la viewport virtuelle
        allume_pixel(self.root_canvas, pro.projection(self.window, self.viewport, poi.Point(50,50)), self.H_ecran)

        # Bindings
        self.root_canvas.bind("<Button 1>", lambda event: bouger(event, canv=self.root_canvas, window=self.window, viewport=self.viewport, H_ecran = self.H_ecran))#, liste_point=LISTE_POINTS))
        self.root_canvas.bind("<B1-Motion>", lambda event: bouger(event, canv=self.root_canvas, window=self.window, viewport=self.viewport, H_ecran = self.H_ecran))#, liste_point=LISTE_POINTS))

        self.root_canvas.pack(fill = "both", expand = True) # Affichage
        self.root.mainloop()

    #@property
    #def H_ecran(self):
    #    return self.__H_ecran

def init_window_viewport(WindowCoor1 : poi.Point, WindowCoor2 : poi.Point, ViewportCoor1 : poi.Point, ViewportCoor2 : poi.Point):
    """ Initialise l'affichage tkinter avec comme paramètre les coordonnées de la window
    et de la viewport"""
    root = tk.Tk()
    root.geometry("1000x1000")
    root_canvas = tk.Canvas(root, bg = "red")
    root.update()

    window = rec.Rectangle(WindowCoor1, WindowCoor2)

    viewport = rec.Rectangle(ViewportCoor1, ViewportCoor2)

    viewport_obj = creer_viewport(root_canvas, viewport, root.winfo_height()) # création de la viewport virtuelle
    allume_pixel(root_canvas, pro.projection(window, viewport, poi.Point(50,50)), root.winfo_height())

    # Bindings
    root_canvas.bind("<Button 1>", lambda event: bouger(event, canv=root_canvas, window=window, viewport=viewport, H_ecran = root.winfo_height()))#, liste_point=LISTE_POINTS))
    root_canvas.bind("<B1-Motion>", lambda event: bouger(event, canv=root_canvas, window=window, viewport=viewport, H_ecran = root.winfo_height()))#, liste_point=LISTE_POINTS))

    root_canvas.pack(fill = "both", expand = True) # Affichage
    root.mainloop()




def creer_viewport(canv : tk.Canvas, rectangle : rec.Rectangle, H_ecran):
    """ Création de la viewport virtuelle sur le canvas"""
    x = rectangle.p1.x
    y = H_ecran - rectangle.p1.y
    #y = rectangle.p1.y
    hauteur = rectangle.hauteur
    largeur = rectangle.largeur
    ident = canv.create_rectangle(x, y - hauteur, x + largeur, y, fill = "blue", tags='viewport')
    #ident = canv.create_rectangle(x, y, x + largeur, y + hauteur, fill = "blue", tags='viewport')

    return ident





def bouger(event: tk.Event, canv: tk.Canvas, window: rec.Rectangle, viewport: rec.Rectangle, H_ecran):#, liste_point):
    """ Fonction qui déplace la viewport virtuelle, elle efface tous les élements de la viewport,
    déplace la viewport et reconstruit les éléments."""

    canv.moveto('viewport', event.x, event.y-viewport.hauteur) # On bouge le rectangle viewport
    canv.delete('point') # On efface tous les points
    

    viewport.p1.x = event.x # Nouveau x à l'endroit du clic
    viewport.p1.y = H_ecran - event.y   # Symétrie du changement à l'espace écran
    viewport.p2.x = event.x + viewport.largeur  # Le x actuel + largeur de la viewport
    viewport.p2.y = viewport.p1.y + viewport.hauteur # Le y actuel + hauteur de la viewport

    # On effectue la projection pour toute la liste de points
    #for i in range(len(LISTE_POINTS)):
    #    LISTE_POINTS[i] = projection(window, viewport, LISTE_POINTS[i])
    #    allume_pixel(canv, LISTE_POINTS[i], root.winfo_height())
    #print(LISTE_POINTS)



def allume_pixel(canv: tk.Canvas, point: poi.Point, H_ecran):
    point_tmp = poi.Point(point.x, point.y)
    point_tmp = pro.sym_point(point_tmp, H_ecran)
    canv.create_oval(point_tmp.x-3, point_tmp.y-3, point_tmp.x+3, point_tmp.y+3, fill = "cyan", tags='point')




