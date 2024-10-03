from PIL import Image
from couleur import Couleur
from camera import Camera
from point import Point
from sphere import Sphere
from vecteur import Vecteur
from plan import Plan
from lumiere import Lumiere
from moteur import Moteur

from scene import Scene


def main(scene : Scene):
    M = Moteur()


    
    L = (M.ray_casting(scene))


    im = Image.new('RGB', (scene.width*10, scene.height*10))
    im.putdata(L)
    im.save("test.png")



    #PIL_image = Image.fromarray(np.array(L))

    #PIL_image = Image.fromarray(L.astype('uint8'), 'RGB')

if __name__ == "__main__":
    WIDTH = 32
    HEIGHT = 20
    

    camera = Camera(Point(0, 0, 0), [HEIGHT, WIDTH], Vecteur(Point(0, 0, 1)), Vecteur(Point(0, 1, 0)), 5)


    #objets = [Sphere(Point(0, 0, 0), r=0.1), Sphere(Point(10, 10, -10), r=0.5), Sphere(Point(-10, -10, -2), r=0.5)]
    PLAN_MUR_GAUCHE = Plan(pos=Point(-30, 0, 0), coul=Couleur(Point(255, 255, 255)),dir=Vecteur(Point(1, 0, 0) ), coef_r=0.85)
    PLAN_MUR_DROIT = Plan(pos=Point(30, 0, 0), coul=Couleur(Point(255, 255, 255)),dir=Vecteur(Point(-1, 0, 0) ), coef_r= 0)
    PLAN_SOL = Plan(pos=Point(0, -2, 0), coul=Couleur(Point(255, 255, 255)), dir=Vecteur(Point(0, 1, 0)), coef_r=0.85)
    PLAN_MUR_FACE = Plan(pos=Point(0, 0, -10), coul= Couleur(Point(255, 255, 255)), dir=Vecteur(Point(0, 0, 1)), coef_r=0)
    PLAN_PLAFOND = Plan(pos=Point(0, 20, 0), coul= Couleur(Point(255, 255, 255)), dir=Vecteur(Point(0, -1, 0)), coef_r= 0.85)


    #objets = [Sphere(pos=Point(-6, 6, -3), coul=Couleur(Point(0, 255, 0)), r=4, coef_r=0.85), Sphere(pos=Point(5, 0, -1), coul=Couleur(Point(255, 255, 255)),r=3, coef_r=0.85), PLAN_MUR_FACE, PLAN_SOL, PLAN_MUR_GAUCHE,PLAN_MUR_DROIT, PLAN_PLAFOND]
    objets = [Sphere(pos=Point(-4, 2, -5), r=3, coef_r=0.2), Sphere(pos=Point(4, 2, -5), coul=Couleur(Point(255, 255, 255)),r=3, ambiant=0.1, coef_r=0.2), PLAN_MUR_FACE, PLAN_SOL, PLAN_MUR_GAUCHE,PLAN_MUR_DROIT, PLAN_PLAFOND]

    LUMIERE_1 = Lumiere(Point(-10, 5, 3))
    LUMIERE_2 = Lumiere(Point(-5, 10, 5))
    LUMIERE_3 = Lumiere(Point(0, -3, -5))
    lumieres = [LUMIERE_1]#, LUMIERE_2]# LUMIERE_3]

    scene = Scene(camera, objets, lumieres, WIDTH, HEIGHT)

    main(scene)