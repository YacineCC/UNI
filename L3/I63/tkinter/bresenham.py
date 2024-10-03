from point import *
LISTE_POINTS = []




def pente(p1: Point, p2: Point) -> float:
    return (p2.y - p1.y)/(p2.x - p1.x)

def segment_naif(p1: Point, p2: Point):
    """ Fonction naïve pour tracer un segment, pas optimal !!"""
    global LISTE_POINTS
    a = (p2.y - p1.y) / (p2.x - p1.x)
    b = p1.y - a * p1.x 
    for x in range(p1.x, p2.x):

        LISTE_POINTS += [Point(x, a * x + b)]


def bresenham_1(p1, p2, canv, H_ecran):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    dec = dx - 2 * dy
    x = p1.x
    y = p1.y
    while(x <= dx):
        allume_pixel(canv, Point(x, y), H_ecran)
        
        if(dec < 0):
            dec = dec + 2 * dx
            y = y + 1
        dec = dec - 2 * dy
        x = x + 1

def bresenham_2(p1, p2, canv, H_ecran):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    dec = dx - 2 * dy
    x = p1.x
    y = p1.y
    while(x <= dx):
        allume_pixel(canv, Point(y, x), H_ecran)
        
        if(dec < 0):
            dec = dec + 2 * dx
            y = y + 1
        dec = dec - 2 * dy
        x = x + 1

def bresenham(p1, p2, canv, H_ecran):
    if( pente(p1, p2) < 1) :
        bresenham_1(p1, p2, canv, H_ecran)
    else:
        p1.x, p2.x = p1.y, p2.y
        bresenham_2(p1, p2, canv, H_ecran)