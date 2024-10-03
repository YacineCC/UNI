from ray import Ray
from point import Point
from couleur import Couleur
from vecteur import Vecteur
from scene import Scene
from camera import Camera
from sphere import Sphere
from lumiere import Lumiere
from PIL import Image
import numpy as np
from plan import Plan

class Moteur:

    nb_max_rec = 0
    
    def intersection_plus_proche(self, scene : Scene, rayon : Ray):
        MAX_DIST = 1e3
        min_dist = MAX_DIST
        closest_obj = None
        for objet in scene.objets:
            dist = objet.intersection(rayon)
            #print(dist)

            if dist == None or dist < 0 :
            
                continue
            
            if dist < min_dist :
                #print(dist)
                min_dist = dist
                closest_obj = objet
        
        return min_dist, closest_obj


    def calcul_couleur(self, scene : Scene, rayon : Ray):
        self.nb_max_rec += 1
        if self.nb_max_rec >= 5:
            return(Couleur(Point(0, 0, 0)))
        
        min_dist, closest_obj = self.intersection_plus_proche(scene, rayon)
                
        # Si pas d'intersection trouvée, couleur noire
        if closest_obj is None:
            return(Couleur(Point(0, 0, 0)))
        else:
            # Sinon on met la couleur de l'objet
            pt = rayon.get_point(min_dist)
            
            
            
            normale = closest_obj.normale(pt)
            
            

            #L.append(closest_obj.couleur.tup)

            # Lumière = ambiant + diffus + speculaire
            # Couleur du pixel = Couleur_de_l'objet * Lumière


            # color = Couleur(Point(0, 0, 0))
            # for lumiere in scene.lumieres:
            #     direction_lum = Vecteur(lumiere.position,pt).normalisation()
            #     print(lumiere.position, pt, direction_lum)
            #     color += normale.prod_scal(direction_lum) * closest_obj.couleur
            # #L.append((int(min(color.x, 255)), int(min(color.y, 255)), int(min(color.z, 255)))) # Pour gérer plusieurs sources de lumières.
            # return color


            color = Couleur(Point(0, 0, 0))
            for lumiere in scene.lumieres: # Pour gérer plusieurs sources de lumières.
                
                
                
                
                direction_lum = Vecteur(lumiere.position, pt).normalisation() # Dans notre monde la lumière va dans l'autre sens.
                n_pt = Point(pt.x + 0.01 * normale.x, pt.y + 0.01 * normale.y, pt.z + 0.01 * normale.z)
                rayon_ombr = Ray(n_pt, direction_lum)
                min_dist_ombr, closest_obj_ombr = self.intersection_plus_proche(scene, rayon_ombr)

                if closest_obj_ombr != None:
                    if min_dist_ombr < pt.distance(lumiere.position):
                        return Couleur(Point(0, 0, 0))


                ambiant = closest_obj.ka
                diffus = normale.prod_scal(direction_lum) * closest_obj.kd


                rayon_reflet = (direction_lum).reflet(normale).normalisation()
                speculaire = rayon_reflet.prod_scal(rayon.direction) 

                speculaire = (speculaire ** 50) * closest_obj.ks
                #print(speculaire)
                lumiere_coef =  ambiant + diffus + speculaire
                #lumiere_coef = speculaire 

                #color = closest_obj.couleur.prod_comp(lumiere_coef)

                color += closest_obj.couleur * (ambiant + diffus) + lumiere.couleur * speculaire 
            #return color
        


        rayon_reflechi = rayon.direction.reflet(normale)
        #print(rayon_reflechi)
        # if closest_obj.coef_r > 0 and self.nb_max_rec == 1:
        #     print(color, self.nb_max_rec, ambiant, speculaire, diffus)
        #     pass

        new_pt = Point(pt.x + 0.01 * normale.x, pt.y + 0.01 * normale.y, pt.z + 0.01 * normale.z)
        #print(new_pt)
        tmp = self.calcul_couleur(scene, Ray(new_pt, rayon_reflechi))
        # if tmp.x !=0 and tmp.y !=0 and tmp.z != 0:
        #     print(tmp)
        color =  color * (1 - closest_obj.coef_r) + tmp * closest_obj.coef_r
        return color


    def ray_casting(self, scene : Scene):
        
        L = []
        nb_inter = 0
        # r_vue = scene.camera.rayon_vue(319, 199)
        # print("rayon direction : ",r_vue.direction)
        # dist = scene.objets[0].intersection(r_vue)
        # print(dist)
        # return
        #compteur = 0
        for y in range(scene.camera.hauteur*10) :
            
            for x in range(scene.camera.largeur*10):
                # if y == 0:
                #     print("x", x)
                
                #pixel = scene.camera.pixel(x,y) # point du centre du pixel pour le rayon_vue
                #origine = scene.camera.focale # foyer
                rayon_vue = scene.camera.rayon_vue(x, y)
                # if compteur < 20:
                #     compteur += 1
                #     print(compteur,"Rayon",rayon_vue.direction)
                
                        #color = closest_obj.couleur * (lumiere_coef)
                self.nb_max_rec = 0
                color = self.calcul_couleur(scene, rayon_vue)

                L.append((int(color.x), int(color.y), int(color.z)))



                    # for objet in scene.objets:
                    #     if objet != i:
                    #         dist = objet.intersection(norm, lumiere)
                    #         if dist < 0:
                    #             L.append((0, 0, 0))

            
        print("nb inter", nb_inter)
        return L


if __name__ == "__main__":

    pass