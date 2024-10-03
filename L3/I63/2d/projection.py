import point as poi, rectangle as rec

def projection(window: rec.Rectangle, viewport: rec.Rectangle, point: poi.Point):
    # Obtenu de la matrice de projection et du vecteur
    x = ((viewport.largeur / window.largeur) * point.x) + viewport.p1.x - ((viewport.largeur * window.p1.x) / window.largeur)
    y = (viewport.hauteur / window.hauteur) * point.y + (viewport.hauteur * window.p1.y) / window.hauteur + viewport.p1.y
    return poi.Point(x, y)



def sym_point(point: poi.Point, H_ecran):
    point.y = H_ecran - point.y
    return point