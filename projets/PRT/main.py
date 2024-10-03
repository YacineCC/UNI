from __future__ import annotations
from PIL import Image
from couleur import Couleur, BLEU, BLANC, ROUGE, NOIR, BLANC, VERT, VIOLET, JAUNE
from camera import Camera
from point import Point
from sphere import Sphere
from vecteur import Vecteur
from plan import Plan
from lumiere import Lumiere
from moteur import Moteur
from materiaux import MAT, MIRROIR, VERRE, BRILLANT
from scene import Scene

def main(scene : Scene):
    """ Manuel d'utilisation : Vous avez à votre disposition une caméra
    paramétrable, vous pouvez définir une liste d'objets (plan et sphères)
    et une liste de lumières. Créez une classe Scene avec cette caméra et ces 
    listes d'objets et de lumières et lancez le main avec cette scène.
    Vous avez aussi à votre disposition des variables pré faites de couleurs et 
    de matériaux."""

    M = Moteur()
    L = (M.ray_tracing(scene))
    im = Image.new('RGB', (scene.camera.nc, scene.camera.nl))
    im.putdata(L)
    im.save("./images/test.png")

if __name__ == "__main__":    

    # Attention à ne pas mettre une résolution trop élevée, le temps de rendu est
    # exponentielle, les images du répertoire "images" sont en résolution 800
    # Pour des tests assez rapides on recommande une résolution d'environ 100.
    camera = Camera(origine=Point(0, 0, 3), up=Vecteur(Point(0, 1, 0)),
                    look_at=Point(0, 0, -15), focale=10, resolution = 100,
                      largeur_image=10, aspect_ratio=16/9, fov=120)
  
    PLAN_MUR_GAUCHE = Plan(pos=Point(-30, 0, 0), couleur=BLANC,direction=Vecteur(Point(1, 0, 0) ), materiaux=BRILLANT)
    PLAN_MUR_DROIT = Plan(pos=Point(30, 0, 0), couleur=BLANC,direction=Vecteur(Point(-1, 0, 0) ), materiaux=BRILLANT)

    PLAN_SOL = Plan(pos=Point(0, -5, 0), couleur=BLANC, direction=Vecteur(Point(0, 1, 0)), materiaux=BRILLANT)
    PLAN_PLAFOND = Plan(pos=Point(0, 20, 0), couleur=BLANC, direction=Vecteur(Point(0, -1, 0)), materiaux=BRILLANT)

    PLAN_MUR_FACE = Plan(pos=Point(0, 0, -35), couleur=BLANC, direction=Vecteur(Point(0, 0, 1)), materiaux=BRILLANT)
    PLAN_MUR_DERRIERE = Plan(pos=Point(0, 0, 35), couleur=BLANC, direction=Vecteur(Point(0, 0, -1)), materiaux=BRILLANT)

    SPHERE_1 = Sphere(pos=Point(-6, 0, -17), couleur=JAUNE,rayon=3, materiaux=BRILLANT)
    SPHERE_2 = Sphere(pos=Point(-4, 0, -13), couleur=VERT,rayon=3, materiaux=BRILLANT)
    SPHERE_3 = Sphere(pos=Point(4, 0, -13), couleur=ROUGE,rayon=3, materiaux=BRILLANT)
    SPHERE_4 = Sphere(pos=Point(0, 0, 13), couleur=VIOLET,rayon=3, materiaux=BRILLANT)
    # SPHERE_1 = Sphere(pos=Point(-6, 4, -17), couleur=JAUNE,rayon=3, materiaux=BRILLANT)
    # SPHERE_2 = Sphere(pos=Point(-4, 0, -13), couleur=VERT,rayon=3, materiaux=VERRE)
    # SPHERE_3 = Sphere(pos=Point(4, 0, -7), couleur=ROUGE,rayon=3, materiaux=VERRE)
    # SPHERE_4 = Sphere(pos=Point(0, 0, 13), couleur=VIOLET,rayon=3, materiaux=BRILLANT)

    # SPHERE_5 = Sphere(pos=Point(6, 4, -17), couleur=VIOLET,rayon=3, materiaux=MAT)
    # SPHERE_6 = Sphere(pos=Point(3, 1, -10), couleur=BLANC,rayon=3, materiaux=VERRE)
    # SPHERE_7 = Sphere(pos=Point(3, 8, -20), couleur=BLANC,rayon=3, materiaux=MIRROIR)

    LUMIERE_1 = Lumiere(Point(5, 10, 10), couleur=BLANC)
    LUMIERE_2 = Lumiere(Point(-5, 10, 10), couleur=BLANC)
    LUMIERE_3 = Lumiere(Point(0, -2, 3))
    LUMIERE_4 = Lumiere(Point(0, 0, 0))

    objets = [SPHERE_1, SPHERE_2, SPHERE_3, SPHERE_4, PLAN_SOL, PLAN_PLAFOND, PLAN_MUR_FACE, PLAN_MUR_DERRIERE, PLAN_MUR_DROIT, PLAN_MUR_GAUCHE]
    lumieres = [LUMIERE_1, LUMIERE_2]

    scene = Scene(camera, objets, lumieres)

    main(scene)