from __future__ import annotations
from ray import Ray
from point import Point
from couleur import Couleur, BLEU, BLANC, ROUGE, NOIR, BLANC, VERT, VIOLET, JAUNE
from vecteur import Vecteur
from scene import Scene
from camera import Camera
from sphere import Sphere
from lumiere import Lumiere
from PIL import Image
import numpy as np
from plan import Plan
from objet import Objet
from time import time

class Moteur:
    """ C'est ici que tourne l'algorithme du ray tracing, décomposé en plusieurs
    petites méthodes pour une meilleure lisibilitée et comprehension."""

    # Epsilon utile pour décaler légerement un point d'intersection vers sa
    # normale pour éviter de re intersecter le même objet immediatement.
    EPSILON = 0.00000001
    # Nombre maximum de récursion qui défini la fidélité du rendu mais aussi son
    # temps de calcul.
    NB_REC_MAX = 3

    def intersection_plus_proche(self, scene : Scene, rayon : Ray):
        """ Renvoi la distance minimale d'intersection d'un rayon dans une scene
        ainsi que l'objet intersecté. Renvoi None et une distance infini si pas 
        d'intersection."""

        DIST_MAX = 1e3
        dist_min = DIST_MAX
        obj_plus_proche = None
        for objet in scene.objets:
            # La méthode d'intersection est propre au type d'objet (plan, sphère).
            dist = objet.intersection(rayon)
        
            if dist < dist_min :
                dist_min = dist
                obj_plus_proche = objet
        
        return dist_min, obj_plus_proche

    def ombre_portees(self, scene, pt, normale, direction_lum, lumiere):
        """ Renvoi True si la couleur au point d'intersection sera noire,
        pour se faire on envoi un shadow ray, du point d'intersection vers les
        sources lumineuses et verifier que le rayon n'intersecte pas un autre
        objet."""
        n_pt = pt + (self.EPSILON * normale)
        rayon_ombr = Ray(n_pt, direction_lum)
        dist_min_ombr, obj_plus_proche_ombr = self.intersection_plus_proche(scene, rayon_ombr)

        if obj_plus_proche_ombr != None:

            if dist_min_ombr < pt.distance(lumiere.position):
                    return True
        else:
            return False
        
        


    def phong(self, closest_obj : Objet, normale : Vecteur,
               direction_lum : Vecteur, rayon : Ray, lumiere : Lumiere):
        """ Illumination de Phong comme vu en TD, la lumière ambiante étant
        indépendante des sources de lumières on ne la calcule qu'une seule fois.
        Il nous reste donc le diffus et le spéculaire. Diffus = Io.kd(L.N) et
        dépend donc l'angle de la lumière avec la normale.
        spéculaire = ks.(R.v)^n et dépend donc de l'angle du rayon réfléchi et
        avec l'observateur, comme avec le reflet d'une montre ou d'un pare-brise
        de voiture au bâtiment Y1..."""


        diffus = normale.prod_scal(direction_lum) * closest_obj.materiaux.diffus
        diffus = diffus * closest_obj.couleur
        diffus = lumiere.couleur.prod_comp(diffus)

        rayon_reflet = (direction_lum).reflet(normale)
        rv = rayon_reflet.prod_scal(rayon.direction) 
        speculaire = (rv ** closest_obj.materiaux.n) * closest_obj.materiaux.speculaire
        speculaire *= lumiere.couleur
        
        return diffus + speculaire

    def couleur_reflechie(self, scene, rayon, normale, pt, nb_rec : int, n1 : float, n2):
        """ Essence même du ray tracing, sa récursivite. La méthode renvoie
        la couleur calculée du rayon réfléchie à partir du point d'intersection
        d'origine et de la direction du rayon réfléchie."""

        rayon_reflechi = rayon.direction.reflet(normale)
        new_pt = pt + (self.EPSILON * normale)
        tmp = self.calcul_couleur(scene, Ray(new_pt, rayon_reflechi), nb_rec + 1, n1, n2)

        return tmp
    
    def couleur_refractee(self, scene : Scene, rayon : Ray, normale : Vecteur,
                           pt : Point, nb_rec : int, n1 : float, n2):
        """ Essence même du ray tracing, sa récursivite. La méthode renvoie
        la couleur calculée du rayon réfracté à partir du point d'intersection
        d'origine et de la direction du rayon réfracté."""

        origine_refraction = pt - (self.EPSILON * normale)
        direction_refraction = rayon.direction.refraction(normale, n1, n2)

        # On regarde si l'angle n'est pas critique et donc pas de réfléxion
        # interne totale.
        if(direction_refraction != None):
            tmp = self.calcul_couleur(scene, Ray(origine_refraction, direction_refraction), nb_rec + 1, n1, n2)
            return tmp
        else:
            return None

    def calcul_couleur(self, scene : Scene, rayon : Ray, nb_rec : int, n1 : float, n2 : float):
        """ Partie récursive de l'algorithme qui sera appelé autant de fois que
        la profondeur max de récursion par pixel, retourne une couleur qui prend
        en compte si c'est une ombre, les différentes sources de lumières et
        leur couleur, les réfléxions et réfractions."""

        # On arrête l'algorithme pour ce pixel si on atteint la profondeur max
        # de récursion.
        if nb_rec > self.NB_REC_MAX:
            return NOIR

        # On prend l'objet intersecté le plus proche ainsi que sa distance.
        dist_min, obj_plus_proche = self.intersection_plus_proche(scene, rayon)
                
        # Si pas d'intersection trouvée, couleur noire
        if obj_plus_proche is None:
            return NOIR
        
        # Coordonnées du point d'intersection.
        pt = rayon.get_point(dist_min)
        
        # Normale au point d'intersection, la méthode pour avoir la normale est
        # propre à chaque type d'objet.
        normale = obj_plus_proche.normale(pt)
        
        # On commence avec une couleur noire (0, 0, 0).
        color = NOIR
        
        # On y ajoute la lumière ambiante.
        # Qui ne dépend pas des sources lumineuses
        #color = closest_obj.couleur * closest_obj.materiaux.ambiant 
        for lumiere in scene.lumieres: 
        
            direction_lum = Vecteur(lumiere.position, pt).normalisation()
        
            if self.ombre_portees(scene, pt, normale, direction_lum, lumiere):
                # On retourner la couleur noir, ou 0.1 * la couleur initiale
                # pour des ombres plus douces.
                return obj_plus_proche.couleur * 0.1
                #return NOIR
            

            # On ajoute l'illumination de Phong.
            color += self.phong(obj_plus_proche, normale, direction_lum, rayon, lumiere)


        # Si la surface de l'objet est réfléchissante on ajoute à notre couleur
        # la couleur trouvée par le rayon réfléchi avec un appel de cet
        # algorithme. La couleur finale dépend du coefficient de réfléxion, plus
        # il est élevé, plus l'objet aura la couleur de ceux environant et moins
        # de sa propre couleur.
        if obj_plus_proche.materiaux.coef_r > 0:
            tmp = self.couleur_reflechie(scene, rayon, normale, pt, nb_rec, n1, n2)
            color =  color * (1 - obj_plus_proche.materiaux.coef_r) + tmp * obj_plus_proche.materiaux.coef_r
            
        
        # Pour determiné si le rayon traverse un objet et va en sortir on
        # on regarde le signe du produit scalaire entre ce rayon et la normale.
        # Si on sort d'un objet alors le prochain milieu est l'air.
        if rayon.direction.prod_scal(normale) < 0:
            n2 = 1
        else:
            n2 = obj_plus_proche.materiaux.indice_refraction

        # Si l'objet est transparenc on ajoute à notre couleur la couleur
        # trouvée par le rayon réfracté avec un nouvel appel de cet algorithme.
        if obj_plus_proche.materiaux.transparence:
            tmp = self.couleur_refractee(scene, rayon, normale, pt, nb_rec, n1, n2)
            
            # Pour l'instant on ne teste qu'avec du verre donc le coefficient est
            # de 1 à terme il faudrait ajouter le coefficient de transparence au
            # matériau d'un objet pour avoir différents niveaux de translucidité. 
            coef_t = 1
            
            color = color * (1 - coef_t) + tmp * coef_t

        return color



    def gamma_correction(self, L : list[tuple], gamma, maxi):
        """ Application de la gamma correction sur la matrice de couleurs final.
        La gamma correction est nécéssaire pour passé du monde linéaire qu'on a
        créer, au monde perçu par nos yeux qui est plus logarithmique. Par
        exemple dans notre scène si on ajoute une deuxième source lumineuse, il
        ne faut pas que l'image devienne deux fois plus illuminée. Cela
        s'explique par nos yeux qui se sont adaptés pour pouvoir voir dans des
        environements peu éclairés sans être aveuglé par d'autres environement
        plus éclairés."""

        # Application de la formule du TD, 255.(im/max(im))^gamma
        res = []

        for i in range(len(L)):
            r = int(((L[i][0] / maxi) ** gamma) * 255)
            v = int(((L[i][1] / maxi) ** gamma) * 255)
            b = int(((L[i][2] / maxi) ** gamma) * 255)
            tmp = (r, v, b) 
            res.append(tmp)
        
        return res



    def ray_tracing(self, scene : Scene):
        """ L'algorithme principal du ray tracing. Pour chaque pixel de notre
        scène, on tire un rayon de vue à partir de notre caméra, l'intersection
        avec un objet ou non, les propriétés de cet objet, les positions des
        autres objets de la scène ainsi leurs propriétés et la positions des 
        sources lumineuses jouera un rôle dans la couleur final du pixel.
        L'algorithme est récursif pour chaque rayon envoyé plusieurs autres
        le seront en fonction d'un profondeur de récursion qui déterminera le 
        niveau de fidélité de l'image finale."""

        start_time = time()
        L = []
        maxi = 0

        for y in range(scene.camera.nl) :
            for x in range(scene.camera.nc):

                nb_rec = 0
                rayon_vue = scene.camera.rayon_vue(x, y)
                # Le rayon part de la caméra donc le mileu c'est l'air.
                indice_r_courant = 1
                color = self.calcul_couleur(scene, rayon_vue, nb_rec, indice_r_courant, None)
                test = max(color.r, color.v, color.b)
                if test > maxi:
                    maxi = test

                L.append((color.r, color.v, color.b))

        L = self.gamma_correction(L, 2.2, maxi)       
        end_time = time()
        print(f"rendu en {round(end_time-start_time,2)} s")
        return L


if __name__ == "__main__":

    pass