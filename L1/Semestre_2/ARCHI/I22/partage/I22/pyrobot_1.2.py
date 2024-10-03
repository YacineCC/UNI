#!/usr/bin/env python3

# ----------------------------------------------------------------------
#  pyrobot : projet pedagogique de logique combinatoire
#            mise en oeuvre via des circuits combinatoires
#            v.20210218
# ----------------------------------------------------------------------

"""
Chaque robot comporte 4 reacteurs R et 4 radars r disposes comme suit :

        R4/r8
          |
   R3/r7-----R1/r5
          |
        R2/r6

La sortie (OUT) d'un composant est reliee a une entree (IN) d'un autre
composant par un fil qui peut comporter des noeuds o (nodes) ayant une
entree (non visible) et une sortie (elle-meme reliee a une entree IN).

          in
   OUT-----o-----IN
           |out
           ------IN
"""

from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
from tkinter import ttk
# from pickle import dump, load
# import cPickle as pickle
import json
# import gc

# ----------------------------------------------------------------------
# constantes et variables globales

LA, HA = 800, 600  # definition d'un canvas
rootl, rooth = 800, 650  # definition de la fenetre principale

# dico superviseur de tous les composants (cle : obj, val : ref)
dcomp = {}

curX, curY = 0, 0  # position courante du clic B1

soudure_flag = False  # mode soudure
noeud_flag = False  # ajout d'un noeud sur un fil
pause = False

noeud_ref = None  # reference au dernier noeud cree
id_fil = None  # id graphique du fil a souder courant

# dico de la logique du circuit (cle : obj, val : dico)
# structure : 'typ' (reacteur, radar, not, node, ...)
#             'orient' (orientation)
#             'in' {id_in, etat, id_out_lie, obj_lie}
#             'out' {id_out, etat, id_in_lie, obj_lie}
dlog = {}

atel = None  # instance courante de l'atelier
land = None  # instance courante du terrain
rob = None  # instance courante du robot

anim = None  # associee a after(), utilisee par after_cancel()

# ----------------------------------------------------------------------

class Composant():
    """
    classe mere des composants proposes dans la classe Atelier
    en plus des portes logiques, sont inclus les reacteurs et les radars
    l'affichage des classes filles depend de canv1

    la gestion des donnees se fait par l'intermediaire des tags graphiques
    car on manipule les composants via une interface graphique (tkinter)
    cela evite dans ce contexte la duplication des informations

    une selection recupere l'id graphique d'une *partie* d'un composant d'ou
    la necessite d'un identifiant unique (le tag objxx) par composant
    ce tag (objxx) est la cle du dico dcomp, dont la valeur reference l'objet
    """
    
    # compteur de composant (binding), les composants statiques
    # (reacteurs, ...) ont un numero inferieur a 10
    cpt = 0
    
    def __init__(self):
        Composant.cpt += 1
        self.obj = "obj"+str(Composant.cpt)  # reference du composant
        self.type = None  # type du composant (not, node, ...)
        self.id = None  # ref de l'objet graphique principal, voir draw
        self.p = []  # pattes E/S (id graphiques)
        self.ox, self.oy = 0, 0  # centre geometrique dans l'espace ecran
        # ajout de l'instance au dico (global) des composants
        dcomp[self.obj] = self

    def draw(self):
        """ a surcharger, propre a chaque composant """
        print("[ERREUR] draw() non surcharge")

    def get_cpt(cls):
        """ methode de classe pour connaitre cpt """
        return Composant.cpt

    def set_cpt(cls, pn):
        """ methode de classe pour gerer cpt """
        Composant.cpt = pn

    def calcul_origine(self):
        """ l'origine se calcule par rapport a self.id """
        lc = canv1.coords(self.id)
        n = len(lc)/2
        self.ox, self.oy = sum(lc[::2])//n, sum(lc[1::2])//n

    # def changer_origine(self, pox=0, poy=0):
    #     """ """
    #     lcomps = canv1.find_withtag(self.obj)
    #     # pour tous les constituants c du composant
    #     for c in lcomps:
    #         oldcoord = canv1.coords(c)
    #         for x, y in zip(oldcoord[::2], oldcoord[1::2]):
    #             newcoord += [self.ox-(y-self.oy), self.oy+(x-self.ox)]
    #         canv1.coords(c, newcoord)

    def get_obj(self):
        return self.obj
        
    def get_id(self):
        return self.id
        
    def get_p(self, pi):
        """ retourne l'ID graphique de la patte d'indice pi """
        if pi < len(self.p):
            return self.p[pi]
        else:
            return None
        
    def get_type(self):
        return self.type
        
    def get_orientation(self):
        pass

    def verif_in(self, pp):
        # print("[verif_in] tags", canv1.gettags(self.id), "ox, oy", self.ox, self.oy)
        # recherche de l'ID dans la liste self.p
        if not pp in self.p:
            print("[ERREUR] get_in", self.type, pp, self.p)
            return
        # liste des tags de la patte
        try:
            ltags = canv1.gettags(pp)
        except:
            print("[ERREUR] verif_in : type", self.type, ", pp", pp)
            return
        # ce n'est pas le bon type de patte
        if not 'in' in ltags:
            print("[ERREUR] get_in", self.type, 'ltags', ltags)
            return
        return ltags
        
    def get_in(self, pp):
        """
        plusieurs pattes IN (sauf pour la porte NOT)
        [E] pp id de la patte
        [S] valeur de la patte 
        """
        ltags = self.verif_in(pp)
        # tout est ok, on retourne la valeur du bit
        if ltags:
            return int([t for t in ltags if 'bit' in t][0][-1])
        else:
            return None

    def set_in(self, pp, pbit):
        """ [E] patte pp parmi plusieurs pattes IN possibles """
        ltags = self.verif_in(pp)
        if ltags:
            bit_tag = [t for t in ltags if 'bit' in t][0]
            # suppression du tag
            canv1.dtag(pp, bit_tag)
            # mise a jour du tag
            canv1.addtag_withtag('bit'+str(pbit), pp)
            # feedback couleur
            self.feedback_bit(pp)

    def verif_out(self):
        """
        la patte out est la derniere
        """
        # concerne la derniere patte de la liste self.p
        # un seul resultat possible [0], le bit est le dernier car [-1]
        ltags = canv1.gettags(self.p[-1])
        if not 'out' in ltags:
            print("[ERREUR] get_out", self.type)
            return
        return ltags

    def get_out(self):
        """
        [S] valeur du bit de sortie (la patte out est la derniere)
        """
        # concerne la derniere patte de la liste self.p
        # un seul resultat possible [0], le bit est le dernier car [-1]
        ltags = self.verif_out()
        if ltags:
            return int([t for t in ltags if 'bit' in t][0][-1])

    def set_out(self, pbit):
        """ une seule patte OUT par composant """
        ltags = self.verif_out()
        if ltags:
            # si le bit est identique a la valeur de sortie, on sort
            if pbit == self.get_out():
                return
            bit_tag = [t for t in ltags if 'bit' in t][0]
            # suppression du tag
            canv1.dtag(self.p[-1], bit_tag)
            # mise a jour du tag
            canv1.addtag_withtag('bit'+str(pbit), self.p[-1])
            # feedback couleur (non recursif)
            self.feedback_bit(self.p[-1])

    def get_id_out(self):
        """ retourne l'ID de l'unique patte out (sauf reacteur) """
        return self.p[-1]

    def get_patte_coord(self, pp):
        """ coord. de l'extremite d'une patte """
        if not pp in self.p:
            return
        lc = canv1.coords(pp)
        return lc[:2]

    def set_origine(self, px, py):
        self.ox = px
        self.oy = py

    def get_fil(self, pp):
        """ retourne l'ID du fil soude a la patte d'ID pp """
        # y a t'il un fil ?
        ltags = canv1.gettags(pp)
        ltmp = [ch for ch in ltags if 'fil' in ch]
        # la liste est vide
        if not ltmp:
            return
        if len(ltmp) > 1:
            print('[ERREUR] get_fil : deux fils ou plus')
            return
        # extraction de l'id du fil (un entier)
        return int(ltmp[0][3:])

    def del_fil(self, pp):
        """ efface l'ID du fil soude a la patte pp """
        # y a t'il un fil ?
        ltags = canv1.gettags(pp)
        ltmp = [ch for ch in ltags if 'fil' in ch]
        # la liste est vide
        if not ltmp:
            return
        if len(ltmp) > 1:
            print('[ERREUR] get_fil : deux fils ou plus')
            return
        canv1.dtag(pp, ltmp[0])

    def deplacer_fils(self):
        # pour toutes les pattes du composant
        for p1 in self.p:
            ltags = canv1.gettags(p1)
            # y a t'il un fil ?
            ltmp = [t for t in ltags if 'fil' in t]
            # la liste est vide => patte suivante
            if not ltmp:
                continue
            # quel type de patte ?
            p1type = 'in' if 'in' in ltags else 'out'
            # pour tous les fils de la patte courante
            # A FAIRE : un seul fil par patte
            for ch in ltmp:
                # extraction de l'id du fil (un entier)
                id_fil = int(ch[3:])
                # recherche de l'id de l'autre patte (unique)
                p2type = 'in' if p1type == 'out' else 'out'
                # TODO: list index out of range
                p2 = fil_get_in_out(id_fil, p2type)
                x, y = self.get_patte_coord(p1)  # extremite patte 1
                # traitement des pattes IN (p2 est une liste)
                # une seule est une vraie patte, les autres sont des nodes
                # on traite les fils des noeuds dans deformer_fil()
                if p2type == 'in':
                    for p in p2:
                        if not 'node' in canv1.gettags(p):
                            obj2 = get_obj(p)  # composant de patte 2
                            x2, y2 = dcomp[obj2].get_patte_coord(p)
                            # deformer_fil(id_fil, p, x, y, False)
                            deformer_fil(id_fil, p1, x2, y2, False)
                # traitement de la patte OUT
                else:
                    obj2 = get_obj(p2)  # composant de patte 2
                    x2, y2 = dcomp[obj2].get_patte_coord(p2)
                    # deformer_fil(id_fil, p2, x, y, False)
                    deformer_fil(id_fil, p1, x2, y2, False)  # globale

    def position(self, px, py):
        """ positionnement absolu du composant """
        # calcul centre geometrique (apres construction graphique)
        self.calcul_origine()
        # move : relatif
        canv1.move(self.obj, px-self.ox, py-self.oy)
        # mise a jour du repere local
        self.set_origine(px, py)

    def rotation90(self):
        """ changement d'orientation par rotation horaire de 90° """
        # a partir de obj_i, recuperation des id graphiques
        lcomps = canv1.find_withtag(self.obj)
        for c in lcomps:
            newcoord = []
            # recuperation des coordonnees d'un composant
            oldcoord = canv1.coords(c)
            for x, y in zip(oldcoord[::2], oldcoord[1::2]):
                newcoord += [self.ox-(y-self.oy), self.oy+(x-self.ox)]
            canv1.coords(c, newcoord)
            # deplacement des fils
            self.deplacer_fils()

    # NON UTILISE
    def rotation90_new(self):
        """ changement d'orientation par rotation horaire de 90° """
        # a partir de obj_i, recuperation des id graphiques
        lcomps = canv1.find_withtag(self.obj)
        self.calcul_origine()  # actualisation origine
        for c in lcomps:
            newcoord = []
            # recuperation des coordonnees d'un composant
            oldcoord = canv1.coords(c)
            canv1.move(c, -self.ox, -self.oy)
            oldcoord = canv1.coords(c)
            for x, y in zip(oldcoord[::2], oldcoord[1::2]):
                newcoord += [y, -x]
            canv1.coords(c, newcoord)
            canv1.move(c, self.ox, self.oy)
            # deplacement des fils

    def dilatation(self, pdx, pdy):
        self.calcul_origine()
        canv1.scale(self.obj, self.ox, self.oy, pdx, pdy)

    def feedback_bit(self, pp):
        """ change la couleur de la patte pp en fonction de sa valeur """
        if not pp in self.p:
            print("[ERREUR] feedback_bit")
            return
        ltags = canv1.gettags(pp)
        # les noeuds ne changent jamais de couleur
        if 'node' in ltags:
            return
        bit = int([t for t in ltags if 'bit' in t][0][-1])
        if bit == 0:
            canv1.itemconfigure(pp, fill='white')
        elif bit == 1:
            canv1.itemconfigure(pp, fill='red')
        else:
            print("[ERREUR] feedback_bit")

    def changer_etat(self, a, b):
        """ propre a chaque composant """
        print("[ERREUR] changer_etat() non surcharge pour", self.type)

    get_cpt = classmethod(get_cpt)  # methode de classe
    set_cpt = classmethod(set_cpt)  # methode de classe
    # methodes statiques : ne prennent aucun premier parametre,
    # travaillent independamment de toute donnee
    # class Test: def afficher(): ...
    # afficher = staticmethod(afficher)

# ----------------------------------------------------------------------

class Not(Composant):
    def __init__(self):
        Composant.__init__(self)  # delegation explicite
        self.type = 'not'
        self.p = [None, None]  # 2 pattes

    def draw(self):
        self.id = canv1.create_polygon(0, 10, 20, 10, 10, 20, fill='white', tags="gate not "+self.obj)
        canv1.create_oval(7, 20, 13, 26, outline='white', tags="gate not "+self.obj)
        self.p[0] = canv1.create_line(10, 0, 10, 10, fill='white', width=3, tags="gate not in bit0 "+self.obj)
        # inversion de l'ordre des coordonnees pour orienter la patte
        self.p[1] = canv1.create_line(10, 36, 10, 27, fill='red', width=3, tags="gate not out bit1 "+self.obj)
        self.position(LA/2, HA/2)
        # # calcul centre geometrique (apres construction graphique)
        # self.calcul_origine()
        # # canv1.move(self.obj, LA/2-self.ox+5, HA/2-self.oy+5)  # centre
        # canv1.move(self.obj, LA/2-self.ox, HA/2-self.oy)  # move : relatif
        # self.set_origine(LA/2, HA/2)

    def changer_etat(self, ppin, pbit):
        """ [E] ppin id de la patte in, pbit valeur du bit in """
        # si le bit en param n'est pas de la meme valeur
        if pbit != self.get_in(ppin):
            self.set_in(ppin, pbit)
            self.set_out(1-pbit)


class And(Composant):
    def __init__(self):
        Composant.__init__(self)
        self.type = 'and'
        self.p = [None, None, None]  # 3 pattes
        self.angle = 180  # angle de depart (start) de l'arc

    def draw(self):
        self.id = canv1.create_arc(92, 4, 118, 36, start=180, extent=180, fill='white', tags="gate and "+self.obj)
        self.p[0] = canv1.create_line(98, 10, 98, 20, fill='white', width=3, tags="gate and in bit0 "+self.obj)
        self.p[1] = canv1.create_line(112, 10, 112, 20, fill='white', width=3, tags="gate and in bit0 "+self.obj)
        # inversion de l'ordre des coordonnees pour orienter la patte out
        self.p[2] = canv1.create_line(105, 46, 105, 36, fill='white', width=3, tags="gate and out bit0 "+self.obj)
        self.position(LA/2, HA/2-6)
        # # calcul centre geometrique
        # self.calcul_origine()
        # canv1.move(self.obj, LA/2-self.ox, HA/2-self.oy-6)  # centre
        # self.set_origine(LA/2-self.ox, HA/2-self.oy-6)

    def rotation90(self):
        """ surcharge car la rotation d'un arc est particuliere """
        Composant.rotation90(self)
        self.angle -= 90  # 90 horaire
        canv1.itemconfigure(self.id, start=self.angle)  # 90 horaire

    def changer_etat(self, ppin, pbit):
        """ [E] ppin id d'une patte in, pbit valeur du bit in """
        # si le bit en param n'est pas de la meme valeur
        if pbit != self.get_in(ppin):
            self.set_in(ppin, pbit)
            # recherche de la valeur de l'autre patte in
            bit = self.get_in(self.p[0]) if ppin != self.p[0] else self.get_in(self.p[1])
            self.set_out(pbit & bit)


class Or(Composant):
    def __init__(self):
        Composant.__init__(self)
        self.type = 'or'
        self.p = [None, None, None]  # 3 pattes

    def draw(self):
        self.id = canv1.create_polygon(92, 20, 97, 31, 105, 36, 105, 36, 113, 31, 118, 20, 118, 20, 105, 26, 92, 20, 92, 20, smooth=True, fill='white', tags="gate or "+self.obj)
        self.p[0] = canv1.create_line(98, 10, 98, 20, fill='white', width=3, tags="gate or in bit0 "+self.obj)
        self.p[1] = canv1.create_line(112, 10, 112, 20, fill='white', width=3, tags="gate or in bit0 "+self.obj)
        # inversion de l'ordre des coordonnees pour orienter la patte out
        self.p[2] = canv1.create_line(105, 46, 105, 36, fill='white', width=3, tags="gate or out bit0 "+self.obj)
        self.position(LA/2, HA/2-6)

    def changer_etat(self, ppin, pbit):
        """ [E] ppin id d'une patte in, pbit valeur du bit in """
        # si le bit en param n'est pas de la meme valeur
        if pbit != self.get_in(ppin):
            self.set_in(ppin, pbit)
            # recherche de la valeur de l'autre patte in
            bit = self.get_in(self.p[0]) if ppin != self.p[0] else self.get_in(self.p[1])
            self.set_out(pbit | bit)


class Xor(Or):
    def __init__(self):
        Or.__init__(self)
        self.type = 'xor'

    def draw(self):
        Or.draw(self)
        # modification des tags or => xor
        canv1.dtag(self.id, 'or')
        canv1.addtag_withtag('xor', self.id)
        for p in self.p:
            canv1.dtag(p, 'or')
            canv1.addtag_withtag('xor', p)
        # ajout de l'arc qui distingue le xor du or
        non = canv1.create_line(92, 17, 105, 23, 118, 17, smooth=True, fill='white', tags="gate xor "+self.obj)
        canv1.move(non, LA/2-102, HA/2-35)

    def changer_etat(self, ppin, pbit):
        """ [E] ppin id d'une patte in, pbit valeur du bit in """
        # si le bit en param n'est pas de la meme valeur
        if pbit != self.get_in(ppin):
            self.set_in(ppin, pbit)
            # recherche de la valeur de l'autre patte in
            bit = self.get_in(self.p[0]) if ppin != self.p[0] else self.get_in(self.p[1])
            self.set_out(pbit ^ bit)


class Node(Composant):
    """ composant particulier : il n'a pas le tag gate """
    def __init__(self):
        # global noeud_flag
        Composant.__init__(self)
        self.type = 'node'
        self.p = [None, None]  # 2 pattes
        self.fil = None  # ID du fil sur lequel est fixe le noeud
        self.seg = None  # numero du segment du fil (1 ou 2 car coude)
        self.coef = None  # coef [0, 1] de la droite parametrique
        # noeud_flag = True
    
    def draw(self, pfil, px, py):
        """ affichage d'un disque sur le fil pfil """
        # global noeud_flag
        
        # etat de la patte OUT reliee par le fil pfil
        idout = fil_get_in_out(pfil, 'out')
        obj = get_obj(idout)
        bit = dcomp[obj].get_out()
        
        # patte IN invisible mais selection par tags
        self.id = self.p[0] = canv1.create_oval(px-3, py-3, px+3, py+3, state='hidden', tags='node in bit'+str(bit)+' '+self.obj)
        # patte OUT visible et selectionnable
        self.p[1] = canv1.create_oval(px-3, py-3, px+3, py+3, fill='white', outline='white', tags='node out bit'+str(bit)+' '+self.obj)
        
        # mise a jour tags "patte" IN et fil pfil (patte OUT : fin soudure)
        idfil = pfil[0]  # suppression du type tuple, on veut un entier
        canv1.addtag_withtag('in'+str(self.p[0]), pfil)
        canv1.addtag_withtag('fil'+str(idfil), self.p[0])
        
        # maj des attributs
        self.fil = idfil
        cfil = canv1.coords(pfil)
        seg1, seg2 = cfil[:4], cfil[2:]
        # si seg1 est en fait un point
        # if seg1[0] == seg1[2] and seg1[1] == seg1[3]:
        # si seg1 est quasiment un point
        if abs(seg1[0]-seg1[2]) <= 3 and abs(seg1[1]-seg1[3]) <= 3:
            seg1 = None
        # si seg2 est en fait un point
        # if seg2[0] == seg2[2] and seg2[1] == seg2[3]:
        # si seg2 est quasiment un point
        if abs(seg2[0]-seg2[2]) <= 3 and abs(seg2[1]-seg2[3]) <= 3:
            seg2 = None
        cnoeud = canv1.coords(self.p[1])
        xn, yn = (cnoeud[0]+cnoeud[2])/2.0, (cnoeud[1]+cnoeud[3])/2.0
        # for x,y in zip(cfil[0::2], cfil[1::2]):
        # determination du coef de la droite parametrique
        # il peut arriver que le segment soit un point
        try:
            # si le noeud est sur le 1er segment du fil
            if seg1 and xn-3 <= seg1[0] <= xn+3 and xn-3 <= seg1[2] <= xn+3:
                self.seg = 1
                ymin, ymax = min(seg1[1], seg1[3]), max(seg1[1], seg1[3])
                self.coef = 1.0 - abs((yn-ymin)/(ymax-ymin))
            elif seg1 and yn-3 <= seg1[1] <= yn+3 and yn-3 <= seg1[3] <= yn+3:
                self.seg = 1
                xmin, xmax = min(seg1[0], seg1[2]), max(seg1[0], seg1[2])
                self.coef = abs((xn-xmin)/(xmax-xmin))
            # si le noeud est sur le 2eme segment du fil
            elif seg2 and xn-3 <= seg2[0] <= xn+3 and xn-3 <= seg2[2] <= xn+3:
                self.seg = 2
                ymin, ymax = min(seg2[1], seg2[3]), max(seg2[1], seg2[3])
                self.coef = 1.0 - abs((yn-ymin)/(ymax-ymin))
            else:
                self.seg = 2
                xmin, xmax = min(seg2[0], seg2[2]), max(seg2[0], seg2[2])
                self.coef = abs((xn-xmin)/(xmax-xmin))
        except ZeroDivisionError:
            # print("[ERREUR] Node.draw : division par zéro")
            self.coef = 0.5

    def get_num_seg(self):
        return self.seg

    def get_coef(self):
        return self.coef
    
    def get_patte_coord(self, pp):
        """ surcharge : coord. de l'extremite d'une pseudo patte """
        if not pp in self.p:
            return
        lc = canv1.coords(pp)
        return (lc[0]+lc[2])/2.0, (lc[1]+lc[3])/2.0
    
    def changer_etat(self, ppin, pbit):
        """ [E] ppin id de la patte in, pbit valeur du bit in """
        # si le bit en param n'est pas de la meme valeur
        if pbit != self.get_in(ppin):
            self.set_in(ppin, pbit)
            self.set_out(pbit)

    def position(self, px, py):
        """ placement d'un noeud en coord. absolues """
        canv1.coords(self.p[0], px-3, py-3, px+3, py+3)
        canv1.coords(self.p[1], px-3, py-3, px+3, py+3)

    def del_it(self):
        """
        la destruction d'un noeud entraine *recursivement* celles :
          - des noeuds rattachees
          - du fil
        et la mise a jour des pattes IN des composants associes a
        *tous* les noeuds concernes par cette destruction
        """
        id_fil = canv1.find_withtag('out'+str(self.p[1]))
        # print('node p0', canv1.gettags(self.p[0]))
        # print('node p1', canv1.gettags(self.p[1]))
        canv1.delete(self.p[0])  # suppression disque IN (invisible)
        canv1.delete(self.p[1])  # suppression disque OUT
        if id_fil:
            # on peut avoir une liste si node sur fil de node
            # => solution recursive
            linfil = fil_get_in_out(id_fil, 'in')
            # a ce stade : au moins la patte IN du composant relie
            for i in linfil:
                o = get_obj(i)
                t = dcomp[o].get_type()
                # print('[del_it] type o', t)
                if dcomp[o].get_type() != 'node':
                    dcomp[o].del_fil(i)
                else:
                    dcomp[o].del_it()
        # suppression id du fil pour patte IN reliee au OUT du node
        canv1.delete(id_fil)  # suppression du fil du noeud
        # suppression dans le dico dcomp
        # print('del_it de', self.obj)
        dcomp.pop(self.obj)


class Reacteur(Composant):
    """ a creer avant les portes logiques """
    def __init__(self, porient):
        Composant.__init__(self)
        self.type = 'reacteur'
        self.p = [None]  # 1 patte OUT
        if porient in ('n', 's', 'e', 'o'):
            self.orient = porient
        else:
            print('[ERREUR] Radar.__init__ : mauvaise orientation')

    def draw(self):
        # reacteur droit par defaut
        self.p[0] = canv1.create_line(0, 25, 10, 25, fill='white', width=3, tags="reacteur in bit0 "+self.obj)
        self.id = canv1.create_polygon(10, 20, 30, 20, 40, 0, 40, 50, 30, 30, 10, 30, outline='cyan', fill='cyan', tags="reacteur "+self.obj)
        # canv1.move(self.obj, LA-75, HA/2-25)
        self.position(LA-50, HA/2)
    
    def get_id_out(self):
        """ surcharge : pas de patte out """
        return None
    
    def get_orientation(self):
        return self.orient
    
    def changer_etat(self, ppin, pbit):
        """ [E] ppin id d'une patte in, pbit valeur du bit in """
        # si le bit en param n'est pas de la meme valeur
        if pbit != self.get_in(ppin):
            self.set_in(ppin, pbit)


class Radar(Composant):
    """ a creer avant les portes logiques """
    def __init__(self, porient):
        Composant.__init__(self)
        self.type = 'radar'
        self.p = [None]  # 1 patte IN
        self.angle1 = 300  # angle de depart (start) de l'arc
        self.angle2 = 280  # angle de depart (start) de l'arc
        if porient in ('n', 's', 'e', 'o'):
            self.orient = porient
        else:
            print('[ERREUR] Radar.__init__ : mauvaise orientation')
    
    def get_in(self, pp):
        # surcharge : pas de patte IN
        return None
    
    def get_orientation(self):
        return self.orient
    
    def draw(self):
        # radar droit par defaut
        self.p[0] = canv1.create_line(0, 15, 10, 15, fill='white', width=3, tags="radar out bit0 "+self.obj)
        self.id = canv1.create_oval(10, 5, 30, 25, outline='green', fill='green', tags="radar "+self.obj)
        self.arc1 = canv1.create_arc(25, 5, 35, 25, start=300, extent=120, style='arc', outline='green', tags="radar "+self.obj)
        self.arc2 = canv1.create_arc(30, 0, 40, 30, start=280, extent=160, style='arc', outline='green', tags="radar "+self.obj)
        # canv1.move(self.obj, LA-125, HA/2+25)
        self.position(LA-100, HA/2+50)

    def rotation90(self):
        """ surcharge car la rotation d'un arc est particuliere """
        Composant.rotation90(self)
        self.angle1 -= 90  # 90 horaire
        self.angle2 -= 90  # 90 horaire
        canv1.itemconfigure(self.arc1, start=self.angle1)  # 90 horaire
        canv1.itemconfigure(self.arc2, start=self.angle2)  # 90 horaire
    
    def changer_etat(self, ppout, pbit):
        """ [E] ppout id de la patte out (non utilise), 
                pbit valeur du bit in """
        # si le bit en param n'est pas de la meme valeur
        if pbit != self.get_out():
            self.set_out(pbit)
    
    def test_circuit(self):
        if canv1.itemcget(self.id, 'fill') == 'green':
            coul, bit = 'red', 1
        else:
            coul, bit = 'green', 0
        canv1.itemconfigure(self.obj, fill=coul)
        # line (self.p) n'a pas de param outline
        canv1.itemconfigure(self.id, outline=coul)
        canv1.itemconfigure(self.arc1, outline=coul)
        canv1.itemconfigure(self.arc2, outline=coul)
        # changement d'etat
        self.changer_etat(self.p[0], bit)
        # propagation
        maj_patte_in(self.p[0], bit)



# ----------------------------------------------------------------------

class Atelier():
    """
    programmation du comportement d'un robot par circuits combinatoires
    """
    def __init__(self):
        Composant.set_cpt(0)
        canv1.delete(ALL)

    def creer_reacteurs(self):
        # reacteur droit par defaut
        r = Reacteur('e')
        r.draw()
        # r.dilatation(2,2)
        # reacteur bas
        r = Reacteur('s')
        r.draw()
        r.position(LA/2, HA-50)
        r.rotation90()
        # reacteur gauche
        r = Reacteur('o')
        r.draw()
        r.position(50, HA/2)
        r.rotation90() ; r.rotation90()
        # reacteur haut
        r = Reacteur('n')
        r.draw()
        r.position(LA/2, 50)
        r.rotation90() ; r.rotation90() ; r.rotation90()

    def creer_radars(self):
        # radar droit par defaut
        r = Radar('e')
        r.draw()
        # radar bas
        r = Radar('s')
        r.draw()
        r.position(LA/2-50, HA-100)
        r.rotation90()
        # radar gauche
        r = Radar('o')
        r.draw()
        r.position(100, HA/2-50)
        r.rotation90() ; r.rotation90()
        # radar haut
        r = Radar('n')
        r.draw()
        r.position(LA/2+50, 100)
        r.rotation90() ; r.rotation90() ; r.rotation90()

    def creer_corbeille(self):
        """ destruction des composants (gate) non relies """
        x0, y0 = LA-50, HA-50
        d = 25
        canv1.create_rectangle(x0, y0, x0+d, y0+d, fill='grey80', tags='trash')  # corps
        canv1.create_rectangle(x0-5, y0, x0+d+5, y0-10, fill='white')  # couvercle
        canv1.create_line(x0+5, y0-10, x0+5, y0-15, x0+d-5, y0-15, x0+d-5, y0-10, width=2, fill='grey90')  # poignee
        canv1.create_line(x0+5, y0+5, x0+5, y0+d-5, width=3, fill='grey50')  # deco
        canv1.create_line(x0+12, y0+5, x0+12, y0+d-5, width=3, fill='grey50')  # deco
        canv1.create_line(x0+20, y0+5, x0+20, y0+d-5, width=3, fill='grey50')  # deco

    def draw(self):
        """
        affichage de l'interieur du robot
        IN: pdx, pdy facteurs d'echelle
        """
        # canv1.create_oval(50, 50, LA*pdx-50, HA*pdy-50, width=20*min(pdx, pdy), outline='blue')
        canv1.create_oval(50, 50, LA-50, HA-50, width=20, outline='blue')
        self.creer_reacteurs()
        self.creer_radars()  # id = 26 une fois termine reacteurs et radars
        self.creer_corbeille()
        Composant.set_cpt(10)  # les portes logiques commencent a obj11


# ----------------------------------------------------------------------

class Terrain():
    """
    creation d'un terrain subdivise en carres de taille egale
    l'affichage depend de canv2
    /!\ repere orthonorme INDIRECT
    """
    def __init__(self, pdef = 100):
        self.title = ''  # titre de la fenetre (du niveau)
        self.M, self.N = 0, 0  # dimension du niveau (nombre de cases)
        self.mat = []
        self.res = pdef  # definition de chaque case (en px)
        self.ir, self.jr = 0, 0  # coord. de la case de depart
        self.ia, self.ja = 0, 0  # coord. de la case d'arrivee

    def read(self, pnom):
        """ lecture du fichier de nom pnom """
        try:
            fd = open(pnom, 'r', encoding='utf-8')
        except OSError:
            showerror("Terrain - initialisation", "Problème à l'ouverture du fichier du niveau")
            return False
        # 1ere ligne - titre de la fenetre (du niveau)
        self.title = fd.readline()
        # 2ieme ligne - dimension du niveau (M colonnes, N lignes)
        self.M, self.N = [int(i) for i in iter(fd.readline().split())]
        # lecture ligne par ligne du niveau
        self.mat = []
        ligne = fd.readline()
        nb = 0
        while ligne:
            # la ligne comporte le bon nombre de car (sans '\n')
            if len(ligne[:-1]) != self.M:
                showerror("Terrain - initialisation", "fichier de niveau corrompu\n"+str(self.M)+" car attendus mais "+str(len(ligne[:-1]))+" car lus")
                return False
            self.mat += [[]]
            self.mat[-1] += [c for c in ligne[:-1]]  # sans '\n'
            nb += 1
            ligne = fd.readline()
        fd.close()
        if nb != self.N:
            showerror("Terrain - initialisation", "fichier de niveau corrompu\n"+str(self.N)+" lignes attendues mais "+str(nb)+" lignes lues")
            return False
    
        return True
    
    def is_start(self, pi, pj):
        """ la case (pi, pi) est-elle la case de depart ? """
        try:
            case = self.mat[pj][pi]
        except:
            print('[ERREUR] Terrain.is_start')
            return
        return case == 'R'
    
    def is_goal(self, pi, pj):
        """ la case (pi, pi) est-elle la case d'arrivee ? """
        try:
            case = self.mat[pj][pi]
        except:
            print('[ERREUR] Terrain.is_goal')
            return
        return case == 'A'
    
    def scale(self, pdef=None):
        """ changement d'echelle """
        if pdef:
            self.res = pdef
        else:
            if self.M == 0 or self.N == 0:
                print('[ERREUR] Terrain.scale : un terrain doit être chargé')
                return
            # calcul de l'echelle (en pourcentage)
            l, h = int(canv2.cget('width')), int(canv2.cget('height'))
            dx, dy = l/self.M, h/self.N
            self.res = min(dx, dy)
        return self.res

    def draw(self):
        self.scale()  # calcul de l'echelle apres chargement du terrain
        d = self.res  # /!\ echelle
        canv2.delete(ALL)  # on efface tout
        # affichage
        for j in range(self.N):
            for i in range(self.M):
                c = self.mat[j][i]
                # mur
                if c == '#':
                    canv2.create_rectangle(i*d, j*d, i*d+d, j*d+d, fill='blue', tags='mur')
                # case de depart du robot
                elif c == 'R':
                    self.ir, self.jr = i, j
                    i0, j0 = i*d, j*d
                    canv2.create_oval(i0, j0, i0+d, j0+d, fill='white', tags='depart')
                    canv2.create_polygon(i0+d/4+d/10, j0+d/4, i0+d/4+d/10, j0+3*d/4, i0+3*d/4+d/10, j0+d/2, fill='black', tags='depart')
                    # homothetie par rapport au centre de la case
                    canv2.scale('depart', i0+d/2, j0+d/2, 0.3, 0.3)
                # case d'arrivee du robot
                elif c == 'A':
                    self.ia, self.ja = i, j
                    canv2.create_arc(i*d, j*d, i*d+d, j*d+d, extent=180.0, fill='white', tags='arrivee')
                    canv2.create_polygon(i*d+d, j*d+d/2, i*d+d/2, j*d+d, i*d, j*d+d/2, fill='white', tags='arrivee')
                    canv2.create_oval(i*d+d/3, j*d+d/3, i*d+d-d/3, j*d+d-d/3, fill='black', tags='arrivee')
                    # homothetie par rapport au centre de la case
                    canv2.scale('arrivee', i*d+d/2, j*d+d/2, 0.3, 0.3)
                elif c == ' ':
                    pass  # espace vide
                else:
                    showerror("Terrain - affichage", "affichage correct du niveau compromis")

# ----------------------------------------------------------------------

class Robot():
    """
    classe principale des robots, modele statique (aucune animation)
    creation graphique dans le canvas canv2
    """
    def __init__(self, pmap, pcoul = 'blue'):
        if not pmap:
            print('[ERREUR] Robot.__init__ : terrain non fourni')
            return
        self.map = pmap  # un robot est toujours associe a une grille
        self._i, self._j = 0, 0  # position sur une grille
        self._ox, self._oy = 0, 0  # centre geometrique dans l'espace ecran
        self.id = canv2.create_oval(10, 30, 10+60, 30+40, fill=pcoul, tags='robot')
        # bumpers (dans l'ordre N, S, O, E)
        canv2.create_rectangle(10+20, 30-6, 10+40, 30-3, fill='white', tags='robot')
        canv2.create_rectangle(10+20, 30+40+3, 10+40, 30+40+6, fill='white', tags='robot')
        canv2.create_rectangle(10-6, 30+10, 10-3, 30+30, fill='white', tags='robot')
        canv2.create_rectangle(10+60+3, 30+10, 10+60+6, 30+30, fill='white', tags='robot')
        # gaz (dans l'ordre N, S, O, E ; caches au depart)
        canv2.create_rectangle(10+20, 30-20, 10+40, 30-10, fill='orange', stipple='gray50', tags=['robot', 'gazn'], state='hidden')
        # canv2.create_rectangle(10+20, 30+40+10, 10+40, 30+40+20, fill='orange', stipple='gray50', tags=['robot', 'gazs'], state='hidden')
        canv2.create_polygon(10+20, 30+40+10, 10+40, 30+40+10, 10+30, 30+40+20, fill='orange', stipple='gray50', tags=['robot', 'gazs'], state='hidden')
        canv2.create_rectangle(10-20, 30+10, 10-10, 30+30, fill='orange', stipple='gray50', tags=['robot', 'gazo'], state='hidden')
        canv2.create_rectangle(10+60+10, 30+10, 10+60+20, 30+30, fill='orange', stipple='gray50', tags=['robot', 'gaze'], state='hidden')
        # antenne
        canv2.create_rectangle(10+20-3, 0, 10+20, 30, fill='white', tags='robot')
        canv2.create_oval(10+20-4, 0, 10+20+1, 5, fill='white', outline='white', tags='robot')
        # pince
        canv2.create_rectangle(10+40+5, 30+40-2, 10+40+10, 30+40+10, fill='white', tags='robot')
        canv2.create_rectangle(10+40+10, 30+40+5-1, 10+40+15, 30+40+10-1, fill='black', outline='white', width=2, tags='robot')
        canv2.create_oval(10+40+15, 30+40+1, 10+40+30, 30+40+11, fill='black', outline='white', width=2, tags='robot')
        # mise a l'echelle et placement sur la case depart => classes filles
        # petite correction de placement
        canv2.move('robot', self.map.res/10, self.map.res/10)

    def _get_pos(self):
        # calcul du centre geometrique
        x1, y1, x2, y2 = canv2.coords(self.id)
        self._ox, self._oy = (x1+x2)//2, (y1+y2)//2
        return self._ox, self._oy
    
    def _get_i(self):
        return self._i
    
    def _get_j(self):
        return self._j
    
    def delete(self):
        """ suppression de tous les elements tk ayant le tag robot """
        canv2.delete('robot')

    def gas(self, pi, pj):
        """ animation des gaz pour les reacteurs concernes (-1, 0 ou 1) """
        # alternance du motif
        bitmapold = canv2.itemcget('gazn', 'stipple')
        bitmap = 'gray50' if bitmapold == 'gray25' else 'gray25'
        # extinction de tous les reacteurs
        canv2.itemconfig('gazn', state='hidden', stipple=bitmap)
        canv2.itemconfig('gazs', state='hidden', stipple=bitmap)
        canv2.itemconfig('gazo', state='hidden', stipple=bitmap)
        canv2.itemconfig('gaze', state='hidden', stipple=bitmap)
        if pi == -1:
            canv2.itemconfig('gaze', state='normal')
        if pi == 1:
            canv2.itemconfig('gazo', state='normal')
        if pj == -1:
            canv2.itemconfig('gazs', state='normal')
        if pj == 1:
            canv2.itemconfig('gazn', state='normal')
    
    def move(self, pi, pj):
        """ position absolue dans la grille associee """
        ox, oy = self._get_pos()
        d = self.map.res  # /!\ echelle
        # fx = d/100
        # si mur alors on ne bouge pas (A FAIRE : verifier au depart ?)
        if self.map.mat[pj][pi] != '#':
            # canv2.move('robot', pi*d-ox*fx+d/2, pj*d-oy*fx+10*fx+d/2)
            canv2.move('robot', (pi-self._i)*d, (pj-self._j)*d)
            self._i, self._j = pi, pj  # maj de la position du robot
        else:
        #     print('ligne', pj, self.map.mat[pj])
        #     print('case', pj, pi, self.map.mat[pj][pi])
        # plus souple : en deux temps = mouvement avec glissement
            if self.map.mat[pj][self._i] != '#':
                canv2.move('robot', 0, (pj-self._j)*d)
                self._j = pj  # maj de la position du robot
            if self.map.mat[self._j][pi] != '#':
                canv2.move('robot', (pi-self._i)*d, 0)
                self._i = pi  # maj de la position du robot
    
    def scale(self, pres = 100):
        # base 100
        canv2.scale('robot', 0, 0, pres/100, pres/100)
        # fx = pres/100
        # canv2.scale('robot', 10, 30, pres/100, pres/100)
    
    def is_wall(self, pdir):
        """
        verification de la presence d'un mur dans la direction pdir a partir
        de la position courante du robot
        """
        if not pdir in ('n', 's', 'e', 'o'):
            print('[ERREUR] Robot.wall : mauvaise direction')
            return True
        dd = {'n':(0,-1), 's':(0,1), 'e':(1,0), 'o':(-1,0)}  # indirect
        di, dj = dd[pdir][0], dd[pdir][1]
        # pas de verif de debordement car mur tout autour
        if self.map.mat[self._j+dj][self._i+di] != '#':
            return False
        else:
            return True
    
    ox = property(_get_pos)
    oy = property(_get_pos)
    i = property(_get_i)
    j = property(_get_j)

class Robot1(Robot):
    """ Robot avec banniere et animation d'un carre qui va et vient """
    def __init__(self, pmap):
        Robot.__init__(self, pmap)  # delegation explicite
        # creation des param propres a l'animation interne du robot
        self.dx, self.sens = 0, 1
        ox, oy = self._get_pos()
        self.idban1 = canv2.create_rectangle(ox-20, oy-3, ox+20, oy+3, fill='black', tags='robot')
        self.idban2 = canv2.create_rectangle(ox-20+self.dx, oy-3, ox-20+6+self.dx, oy+3, fill='white', tags='robot')
        # mise a l'echelle (pas avant car ajout de details)
        self.scale(self.map.res)
        # placement sur la case depart
        self.move(self.map.ir, self.map.jr)

    def anim(self):
        """ petite animation personnelle, ici un curseur qui va et vient """
        fx = self.map.res/100  # facteur homothetique
        if self.dx >= (40-6)*fx:
            self.sens = -1
        if self.dx <= 0:
            self.sens = 1
        self.dx = self.dx + (self.sens*6)*fx
        canv2.move(self.idban2, (6*self.sens)*fx, 0)

# ----------------------------------------------------------------------
# FONCTIONS GLOBALES

def get_obj(pid = None):
    """
    a partir de l'id de la figure selectionnee ou du pid fourni
    retourne le code objet propre a l'appli
    """
    # id unique de l'objet graphique du canvas
    if not pid:
        id = canv1.find_withtag('current')
        if not id:
            return None
    else:
        id = pid    
    # recuperation du tag unique obj_i dans la liste des tags
    try:
        obj = [ch for ch in canv1.gettags(id) if 'obj' in ch][0]
    except:
        return None
    return obj


def nouvel_atelier():
    global atel, dcomp, dlog
    dcomp, dlog = {}, {}  # reset des dico superviseurs
    # del(atel)
    atel = Atelier()
    atel.draw()


def deformer_fil(fil, patte, px, py, new):
    """
    redessine un fil en forme de L
    tracer d'une ligne brisee de l'origine de la patte au pointeur souris
    la ligne brisee a la forme de 2 segments a angle droit
    pour l'orienter "correctement", on a recours au produit scalaire
    le parametre new fait le distingo entre creation et modification
    [E] fil id du fil, patte id de la patte, (px, py) position souris
    """
    lc = canv1.coords(patte)
    u, v = lc[:2], lc[2:]  # u 1er point, v 2eme point
    ps = sum([x * y for x, y in zip(u, v)])
    # si le produit scalaire est negatif alors dans le sens de la patte
    if ps < 0:
        canv1.coords(fil, u[0], u[1], u[0], py, px, py)
    else:
        canv1.coords(fil, u[0], u[1], px, u[1], px, py)
    # traitement des noeuds IN attaches au fil
    lid = canv1.find_withtag('fil'+str(fil))
    ln = []  # liste des id des noeuds
    for id in lid:
        ltags = canv1.gettags(id)
        if 'node' in ltags and 'in' in ltags:
            ln += [id]
    # pour tous les noeuds IN trouves
    # (si on ajoute aussi les noeuds OUT => recursion infinie)
    for n in ln:
        # print('tags de n =>', canv1.gettags(n))
        obj = get_obj(n)
        num, coef = dcomp[obj].get_num_seg(), dcomp[obj].get_coef()
        if ps < 0:
            if num == 1:
                dcomp[obj].position(u[0], coef*u[1]+(1-coef)*py)
            else:
                dcomp[obj].position(coef*u[0]+(1-coef)*px, py)
        else:
            if num == 1:
                dcomp[obj].position(coef*u[0]+(1-coef)*px, u[1])
            else:
                dcomp[obj].position(px, coef*u[1]+(1-coef)*py)
        # deplacement du fil qui part du noeud n
        # id du fil de la patte out du noeud n
        idout = dcomp[obj].get_id_out()
        # list index out of range
        # print('tags de idout', idout, '=>', canv1.gettags(idout))
        outfil = [t for t in canv1.gettags(idout) if 'fil' in t]
        # un noeud peut ne pas avoir de fil a cet instant
        if len(outfil) == 0:
            continue
        idf = int(outfil[0][3:])
        # patte de destination
        lin = fil_get_in_out(idf, 'in')
        for p in lin:
            # on ne traite que l'unique vraie patte IN
            ltp = canv1.gettags(p)
            # print('tags de p', p, '=>', ltp)
            # input()
            if ltp and not 'node' in ltp and 'in' in ltp:
                pobj = get_obj(p)
                x2, y2 = dcomp[pobj].get_patte_coord(p)
                # creation patte bidon pour eviter recursion infinie
                # x1, y1 = dcomp[obj].get_patte_coord(idout)
                # idtmp = canv1.create_line(x1, y1, x1+5, y1)
                deformer_fil(idf, idout, x2, y2, False)
                # canv1.itemconfigure(p, fill='blue')


def fil_get_in_out(pfil, pp=None):
    """
    retourne le ou les IDs des pattes reliees par le fil pfil
    [E] pp type de la patte ('in' ou 'out')
    """
    # le composant n'a pas de fil relie
    if not pfil:
        return
    ltags = canv1.gettags(pfil)
    # pfil est-il bien l'ID d'un fil ?
    if not 'fil' in ltags:
        return
    
    # chaines inxx et outxx
    lchin = [t for t in canv1.gettags(pfil) if 'in' in t]
    # A FAIRE : on peut avoir une liste de pattes IN greffees au fil
    idin = []
    if lchin:
        # print(len(lchin), "pattes IN sur le fil")
        for ch in lchin:
            idin += [int(ch[2:])]  # 'in' 2 lettres
    chout = [t for t in canv1.gettags(pfil) if 'out' in t]
    # une seule patte OUT possible
    idout = None
    if chout:
        idout = int(chout[0][3:])  # 'out' 3 lettres
    
    if not pp:
        return idin, idout  # une liste et un entier
    elif pp=='in':
        return idin  # une liste d'entiers (ID)
    elif pp=='out':
        return idout  # un entier (ID)
    else:
        print("[ERREUR] fil_get_in_out", pp)


def maj_patte_in(pid, pbit):
    """
    mise a jour *recursive* des pattes des composants lies
    [E] pid ID patte d'entree (IN)
        pbit etat de la patte de sortie (OUT), via un fil, en amont
    """
    obj = get_obj(pid)
    dcomp[obj].changer_etat(pid, pbit)
    # appel recursif
    # ID de la patte de sortie (OUT) du composant obj
    # derniere patte de la liste self.p
    id_out = dcomp[obj].get_id_out()
    # pas de patte out (reacteur)
    if not id_out:
        return
    # a quelle patte est reliee la patte out de obj (info dans le fil)
    id_fil = dcomp[obj].get_fil(id_out)
    if id_fil:
        # TODO: list index out of range
        # /!\ c'est une liste
        lid_in = fil_get_in_out(id_fil, 'in')
        # boucle sur la liste
        bit = dcomp[obj].get_out()  # sortie du composant ayant patte pid
        for id_in in lid_in:
            maj_patte_in(id_in, bit)


def sauver_robot():
    """
    construction et sauvegarde de la logique du circuit
    champs pour les reacteurs :
    {'typ', 'orient', 'in':{'idin', 'bit', 'idout', 'objout'}, 'out':None}
    champs pour les radars :
    {'typ', 'orient', 'out':{'idout', 'bit', 'idin', 'objin'}, 'in':None}
    champs pour les portes not et les noeuds :
    {'typ', 'in':{'idin', 'bit', 'idout', 'objout'}, 'out':{'idout', 'bit', 'idin', 'objin'}}
    champs pour les portes a deux entrees (in) :
    {'typ', 'in':{'idin', 'bit', 'idout', 'objout'}, 'out':{'idout', 'bit', 'idin', 'objin'}, 'in2':{'idin', 'bit', 'idout', 'objout'}}
    """
    global dlog
    
    fic = filedialog.asksaveasfilename(
        filetypes=(("Pyrobot", "*.rob"), ("Tout", "*.*")))

    # si un nom a ete saisi
    if fic:
        try:
            # fd = open(fic, 'wb')  # binary pour pickle
            fd = open(fic, 'w', encoding='utf-8')  # string pour json
        except:
            showerror("Erreur", "Impossible de sauvegarder le circuit")
            return
        # instanciation du dico dlog
        dlog = {}  # reset indispensable sinon effet cumulatif
        # cas des parties fixes (reacteurs et radars)
        for i in range(1, 9):
            obj = 'obj'+str(i)
            typ = dcomp[obj].get_type()
            ori = dcomp[obj].get_orientation()
            id = dcomp[obj].get_p(0)  # ID de la seule patte
            idfil = dcomp[obj].get_fil(id)
            idlie, objlie = None, None
            io = 'out' if typ == 'reacteur' else 'in'
            if idfil:
                idlie = fil_get_in_out(idfil, io)  # liste si 'in'
                if io == 'in':
                    # recherche de la "vraie" patte IN (sans les nodes)
                    for p in idlie:
                        if not 'node' in canv1.gettags(p):
                            objlie = get_obj(p)
                            break
                # io == 'out'
                else:
                    # A FAIRE : bug pour radar (wrong # args l. 141)
                    objlie = get_obj(idlie)
            # reacteur : R in ---------- out X
            if typ == 'reacteur':
                bit = dcomp[obj].get_in(id)
                dlog[obj] = {'typ':typ, 'orient':ori, 'in':{'idin':id, 'bit':bit, 'idout':idlie, 'objout':objlie}, 'out':None}
            # radar : R out ---------- in X
            else:
                bit = dcomp[obj].get_out()
                if not idlie:
                    idin = None  # cas du radar sans fil
                else:
                    for idin in idlie:
                        objin = get_obj(idin)
                        if dcomp[objin].get_type() != 'node':
                            break
                dlog[obj] = {'typ':typ, 'orient':ori, 'out':{'idout':id, 'bit':bit, 'idin':idin, 'objin':objlie}, 'in':None}

        # cas des composants en nombre variables
        nbcomp = 0
        for i in range(11, Composant.get_cpt()+1):
            obj = 'obj'+str(i)
            # le composant peut avoir ete efface graphiquement (node par ex)
            if not obj in dcomp.keys():
                continue
            typ = dcomp[obj].get_type()
            # print('preparation sauvegarde de', obj, 'de type', typ)
            dlog[obj] = {'typ':typ}
            # rang de la patte de sortie (out)
            if typ in ('not', 'node'):
                nout = 1
            else:
                nout = 2
            
            # pour tous les composants (2 ou 3 pattes)
            idi, ido = dcomp[obj].get_p(0), dcomp[obj].get_p(nout)
            biti, bito = dcomp[obj].get_in(idi), dcomp[obj].get_out()
            idfili, idfilo = dcomp[obj].get_fil(idi), dcomp[obj].get_fil(ido)
            # pour les composants a 3 pattes
            if not typ in ('not', 'node'):
                idi2 = dcomp[obj].get_p(1)
                biti2 = dcomp[obj].get_in(idi2)
                idfili2 = dcomp[obj].get_fil(idi2)
            
            # on ne sauvegarde pas les composants non relies
            # si porte not non reliee alors composant suivant ou erreur
            if typ in ('not', 'node'):
                if not idfili and not idfilo:
                    dlog.pop(obj)  # not isole (impossible pour node)
                    continue
                if not idfili or not idfilo:
                    showerror("Erreur", "Sauvegarde impossible : porte NOT ou NODE non connectée")
                    fd.close()
                    return
                # il faut effacer les infos des pattes reliees
                # A FAIRE : effacer aussi pour la 3eme patte !
                # A FAIRE : et dans le cas de noeuds sur le fil ?
                # for idbug in (idfili, idfilo):
                #     if idbug:
                #         lidi, ido = fil_get_in_out(idbug)  # relies par fil
                #         dcomp[get_obj(ido)].del_fil(ido)
                #         for idi in lidi:
                #             dcomp[get_obj(idi)].del_fil(idi)
                # dlog.pop(obj)
                # continue
            # si composant a 3 pattes non relies alors suivant ou erreur
            if not typ in ('not', 'node'):
                if not idfili and not idfilo and not idfili2:
                    dlog.pop(obj)
                    continue
                if not idfili or not idfilo or not idfili2:
                    showerror("Erreur", "Sauvegarde impossible : porte AND, OR ou XOR non connectée")
                    fd.close()
                    return
            
            # 2 pattes, 1 in et 1 out (not ou node)
            # X in ---------- out N in ---------- out X'
            idlieo = fil_get_in_out(idfili, 'out')
            objlieo = get_obj(idlieo)  # objet d'ou vient l'info
            lidliei = fil_get_in_out(idfilo, 'in')  # liste
            for idliei in lidliei:
                objin = get_obj(idliei)
                if dcomp[objin].get_type() != 'node':
                    break  # on a trouve un objin qui n'est pas node
            objliei = get_obj(idliei)  # objet ou va l'info
            dlog[obj].update({'in':{'idin':idi, 'bit':biti, 'idout':idlieo, 'objout':objlieo}, 'out':{'idout':ido, 'bit':bito, 'idin':idliei, 'objin':objliei}})
            # 3 pattes, 2 in et 1 out => on ajoute une patte in2
            #                       in  ---------- out X'
            # X in ---------- out C
            #                       in2 ---------- out X"
            if not typ in ('not', 'node'):
                idlieo2 = fil_get_in_out(idfili2, 'out')
                objlieo2 = get_obj(idlieo2)  # objet d'ou vient l'info
                dlog[obj].update({'in2':{'idin':idi2, 'bit':biti2, 'idout':idlieo2, 'objout':objlieo2}})
            nbcomp += 1
            # print(obj, dlog[obj])
        # sauvegarde effective
        json.dump(dlog, fd)  # pickle.dump(dlog, fd)
        fd.close()
        # print(nbcomp, "composant(s) sauvegarde(s)")
        dlog = {}  # reset a nouveau : un robot *doit* etre charge


def charger_robot():
    global dlog, rob
    
    # un exercice doit avoir ete charge
    if not land:
        showerror("Erreur", "Exercice non chargé")
        return
    
    fic = filedialog.askopenfilename(
        filetypes=(("Pyrobot", "*.rob"), ("Tout", "*.*")))
    
    # annule
    if not fic:
        return
    # si un nom a ete saisi
    else:
        try:
            fd = open(fic, 'r', encoding='utf-8')  # string pour json
        except:
            showerror("Erreur", "Impossible de charger le circuit")
            return
    dlog = json.load(fd)
    fd.close()
    
    # affichage du robot graphique (il depend de land)
    # canv2.delete('robot')  # on efface tous tags robot
    if rob:
        rob.delete()
    # del rob
    # gc.collect()
    rob = Robot1(land)
    # rob.scale(land.res)  # /!\ echelle
    # rob.move(1, 1)  # test de deplacement absolu
    
    # mise a jour des controles (go, pause, stop)
    dbout2['5Go'].configure(state='normal')


def charger_niveau():
    global land
    fic = filedialog.askopenfilename(
        filetypes=(("Niveau", "*.niv"), ("Tout", "*.*")))

    # annule
    if not fic:
        return
    
    land = Terrain()
    ok = land.read(fic)
    if ok:
        land.draw()
        dbout2['2Robot'].configure(state='normal')


def maj_dlog(po, pp, pb):
    """
    mise a jour *recursive* des composants lies
    [E] po objet comportant une patte IN
        pp identifiant de la patte IN (il peut y en avoir deux)
        pb etat de la sortie (OUT) reliee en amont
    """
    # quelle patte ?
    # print('maj_dlog pour', po, dlog[po]['typ'])
    # composant a une seule entree (not, node)
    if not dlog[po]['typ'] in ('and', 'or', 'xor'):
        in1 = dlog[po]['in']['bit'] = pb
    # composant a deux entrees
    else:
        if dlog[po]['in']['idin'] == pp:
            in1 = dlog[po]['in']['bit'] = pb
            in2 = dlog[po]['in2']['bit']
        elif dlog[po]['in2']['idin'] == pp:
            in1 = dlog[po]['in']['bit']
            in2 = dlog[po]['in2']['bit'] = pb
        else:
            print('[ERREUR] maj_dlog', po, dlog[po], pp, pb)
            return
    
    # mise a jour de l'etat de la sortie du composant po
    if dlog[po]['typ'] == 'not':
        bit = 1-in1
    elif dlog[po]['typ'] == 'and':
        bit = in1 & in2
    elif dlog[po]['typ'] == 'or':
        bit = in1 | in2
    elif dlog[po]['typ'] == 'xor':
        bit = in1 ^ in2
    elif dlog[po]['typ'] == 'node':
        bit = in1
    # cas du reacteur (pas de sortie)
    if dlog[po]['out']:
        dlog[po]['out']['bit'] = bit
        # print('maj sortie de', po, 'out', dlog[po]['out']['bit'])
    
    # recherche du composant (in) liee au composant po
    # cas du reacteur (pas de sortie)
    if not dlog[po]['out']:
        relie = None
    else:
        relie = dlog[po]['out']['objin']
        patte = dlog[po]['out']['idin']
    # mise a jour du circuit si le radar est relie
    if relie is not None:
        maj_dlog(relie, patte, bit)
    
    # y a t'il des noeuds sur la sortie de po ?
    for o in dlog.keys():
            if dlog[o]['typ'] == 'node' and dlog[o]['in']['objout'] == po:
                # print('noeud', o, 'en sortie de', dlog[po]['typ'], '(bit', dlog[po]['out']['bit'], ')')
                # relie = dlog[o]['out']['objin']
                # patte = dlog[o]['out']['idin']
                relie = o
                patte = dlog[o]['in']['idin']
                # bit = relie.get_out()
                maj_dlog(relie, patte, bit)


def animation_robot():
    global anim
    
    # pas de niveau, de robot ou de circuit
    if not land or not rob or not dlog:
        return
    
    # petite animation propre a chaque type de robot
    rob.anim()
    
    # A FAIRE : extinction des feux
    
    # scrutation des composants du robot a la recherche des radars
    tdir = ('n', 's', 'e', 'o')
    # les cles sont des etiquettes objxx
    for k in dlog.keys():
        obs = False  # obstacle
        if dlog[k]['typ'] == 'radar':
            # obstacle devant le radar courant ?
            for d in tdir:
                if dlog[k]['orient'] == d and rob.is_wall(d):
                    obs = True
            # mise a jour de l'etat du radar
            bit = 1 if obs else 0
            # dcomp[dlog[k]['typ']].changer_etat(None, bit)
            dlog[k]['out']['bit'] = bit
            # recherche du composant (in) *directement* lie au radar
            relie = [dlog[k]['out']['objin']]
            patte = [dlog[k]['out']['idin']]
            # recherche des noeuds ayant directement ce radar en objout
            for o in dlog.keys():
                if dlog[o]['typ'] == 'node' and dlog[o]['in']['objout'] == k:
                    # relie += [dlog[o]['out']['objin']]
                    # patte += [dlog[o]['out']['idin']]
                    relie += [o]
                    patte += [dlog[o]['in']['idin']]
            # mise a jour du circuit si le radar est relie
            for i in range(len(relie)):
                # on peut avoir la liste [None]
                if relie[i]:
                    # print("radar", dlog[k]['orient'], "relié à", relie[i])
                    maj_dlog(relie[i], patte[i], bit)
                
    # scrutation des composants du robot a la recherche des reacteurs
    dd = {'n':(0,1), 's':(0,-1), 'e':(-1,0), 'o':(1,0)}  # indirect et poussee
    idd = {'n':'s', 's':'n', 'e':'o', 'o':'e'}
    i, j = 0, 0
    for k in dlog.keys():
        if dlog[k]['typ'] == 'reacteur':
            # si entree a 1 on deplace le robot dans la direction
            if dlog[k]['in']['bit'] == 1:
                # print('reacteur', k, 'on')  # DEBUG
                ori = dlog[k]['orient']
                # verification possibilite mouvement
                # => mouvement diagonal, reporte sur move
                # if not rob.is_wall(idd[ori]):
                di, dj = dd[ori]
                i, j = i+di, j+dj
    # print("i, j :", i, j)
    # print("------------------------")
    
    # mouvement du robot (et A FAIRE gestion des feux)
    oldi, oldj = rob.i, rob.j
    # gestion des feux
    rob.gas(i, j)
    rob.move(rob.i+i, rob.j+j)
    
    # si le robot ne bouge pas alors on arrete l'animation
    if rob.i == oldi and rob.j == oldj:
        # l'animation peut ne jamais avoir demarre
        if anim:
            root.after_cancel(anim)
        anim = None  # utile ?
        showerror("Robot", "Le robot est immobilisé")
        dbout2['4Pause'].configure(state='disabled')
        dbout2['3Stop'].configure(state='disabled')
        dbout2['2Robot'].configure(state='disabled')
        return
    
    # si le robot parvient au but
    if rob.map.is_goal(rob.i, rob.j):
        # l'animation peut ne jamais avoir demarre
        if anim:
            root.after_cancel(anim)
        anim = None  # utile ?
        showinfo("Problème résolu", "Le robot est bien arrivé")
        dbout2['4Pause'].configure(state='disabled')
        dbout2['3Stop'].configure(state='disabled')
        dbout2['2Robot'].configure(state='disabled')
        return
    
    canv2.update_idletasks()
    # if not pause:
    anim = root.after(500, animation_robot)


def simulation(pa):
    """ effets des controles de l'animation du robot """
    global anim
    # A FAIRE : verifier qu'un niveau et un robot ont ete charge
    if pa == 'stop':
        if anim:
            root.after_cancel(anim)  # A FAIRE : un vrai stop
        anim = None
        dbout2['5Go'].configure(state='disabled')
        dbout2['4Pause'].configure(state='disabled')
        dbout2['3Stop'].configure(state='disabled')
    elif pa == 'pause':
        if anim:
            root.after_cancel(anim)
        dbout2['5Go'].configure(state='normal')
        dbout2['4Pause'].configure(state='disabled')
    elif pa == 'go':
        dbout2['5Go'].configure(state='disabled')
        dbout2['4Pause'].configure(state='normal')
        dbout2['3Stop'].configure(state='normal')
        anim = None  # utile ?
        animation_robot()
    else:
        print('[ERREUR] simulation : action inconnue')


def afficher_aide():
    d = 20
    i, j = 0, 0
    # icone depart
    icondep = Canvas(text1, width=d, height=d, bg='grey20', highlightthickness=0)
    icondep.create_oval(i*d, j*d, i*d+d, j*d+d, fill='white')
    icondep.create_polygon(i*d+d/4+d/10, j*d+d/4, i*d+d/4+d/10, j*d+3*d/4, i*d+3*d/4+d/10, j*d+d/2, fill='black')
    # icone arrivee
    iconarr = Canvas(text1, width=d, height=d, bg='grey20', highlightthickness=0)
    iconarr.create_arc(i*d, j*d, i*d+d, j*d+d, extent=180.0, fill='white')
    iconarr.create_polygon(i*d+d, j*d+d/2, i*d+d/2, j*d+d, i*d, j*d+d/2, fill='white')
    iconarr.create_oval(i*d+d/3, j*d+d/3, i*d+d-d/3, j*d+d-d/3, fill='black')
    # icone mur
    iconmur = Canvas(text1, width=d, height=d, bg='grey20', highlightthickness=0)
    iconmur.create_rectangle(i*d, j*d, i*d+d, j*d+d, fill='blue')
    # icone porte not
    iconnot = Canvas(text1, width=d, height=d, bg='grey20', highlightthickness=0)
    iconnot.create_polygon(0, 10, 20, 10, 10, 20, fill='white', tags='inot')
    iconnot.create_oval(7, 20, 13, 26, outline='white', tags='inot')
    iconnot.create_line(10, 0, 10, 10, fill='white', width=3, tags='inot')
    iconnot.create_line(10, 36, 10, 27, fill='red', width=3, tags='inot')
    iconnot.scale('inot', 0, 0, d/20, d/36)  # dx, dy : difference (max-min)
    # icone porte and
    iconand = Canvas(text1, width=d, height=d, bg='grey20', highlightthickness=0)
    iconand.create_arc(92, 4, 118, 36, start=180, extent=180, fill='white', tags='iand')
    iconand.create_line(98, 10, 98, 20, fill='white', width=3, tags='iand')
    iconand.create_line(112, 10, 112, 20, fill='white', width=3, tags='iand')
    iconand.create_line(105, 46, 105, 36, fill='white', width=3, tags='iand')
    iconand.move('iand', -92, -4)  # Ox, Oy : -min
    iconand.scale('iand', 0, 0, d/26, d/42)  # dx, dy : difference (max-min)
    # icone or
    iconor = Canvas(text1, width=d, height=d, bg='grey20', highlightthickness=0)  # borderwidth=2 ?
    iconor.create_polygon(92, 20, 97, 31, 105, 36, 105, 36, 113, 31, 118, 20, 118, 20, 105, 26, 92, 20, 92, 20, smooth=True, fill='white', tags='ior')
    iconor.create_line(98, 10, 98, 20, fill='white', width=3, tags='ior')
    iconor.create_line(112, 10, 112, 20, fill='white', width=3, tags='ior')
    iconor.create_line(105, 46, 105, 36, fill='white', width=3, tags='ior')
    iconor.move('ior', -92, -10)  # Ox, Oy : -min
    iconor.scale('ior', 0, 0, d/26, d/36)  # dx, dy : difference (max-min)
    # icone xor
    iconxor = Canvas(text1, width=d, height=d, bg='grey20', highlightthickness=0)
    iconxor.create_polygon(92, 20, 97, 31, 105, 36, 105, 36, 113, 31, 118, 20, 118, 20, 105, 26, 92, 20, 92, 20, smooth=True, fill='white', tags='ixor')
    iconxor.create_line(98, 10, 98, 20, fill='white', width=3, tags='ixor')
    iconxor.create_line(112, 10, 112, 20, fill='white', width=3, tags='ixor')
    iconxor.create_line(105, 46, 105, 36, fill='white', width=3, tags='ixor')
    iconxor.create_line(92, 17, 105, 23, 118, 17, smooth=True, fill='white', tags='ixor')
    iconxor.move('ixor', -92, -10)  # Ox, Oy : -min
    iconxor.scale('ixor', 0, 0, d/26, d/36)  # dx, dy : difference (max-min)
    # icone node
    iconnode = Canvas(text1, width=d, height=d, bg='grey20', highlightthickness=0)
    iconnode.create_oval(5, 5, d-5, d-5, fill='white')
    # icone moteur
    iconmot = Canvas(text1, width=d, height=d, bg='grey20', highlightthickness=0)
    iconmot.create_line(0, 25, 10, 25, fill='white', width=3, tags='imot')
    iconmot.create_polygon(10, 20, 30, 20, 40, 0, 40, 50, 30, 30, 10, 30, outline='cyan', fill='cyan', tags='imot')
    iconmot.scale('imot', 0, 0, d/40, d/50)  # dx, dy : difference (max-min)
    # icone radar
    iconrad = Canvas(text1, width=d, height=d, bg='grey20', borderwidth=0, highlightthickness=0)
    iconrad.create_line(0, 15, 10, 15, fill='white', width=3, tags='irad')
    iconrad.create_oval(10, 5, 30, 25, outline='green', fill='green', tags='irad')
    iconrad.create_arc(25, 5, 35, 25, start=300, extent=120, style='arc', outline='green', tags='irad')
    iconrad.create_arc(30, 0, 40, 30, start=280, extent=160, style='arc', outline='green', tags='irad')
    iconrad.scale('irad', 0, 0, d/40, d/30)  # dx, dy : difference (max-min)
    # icone radar active (rouge)
    iconrad2 = Canvas(text1, width=d, height=d, bg='grey20', borderwidth=0, highlightthickness=0)
    iconrad2.create_line(0, 15, 10, 15, fill='white', width=3, tags='irad')
    iconrad2.create_oval(10, 5, 30, 25, outline='red', fill='red', tags='irad')
    iconrad2.create_arc(25, 5, 35, 25, start=300, extent=120, style='arc', outline='red', tags='irad')
    iconrad2.create_arc(30, 0, 40, 30, start=280, extent=160, style='arc', outline='red', tags='irad')
    iconrad2.scale('irad', 0, 0, d/40, d/30)  # dx, dy : difference (max-min)
    
    text1.insert('end', "\nLa barre d'onglets\n\n", 'titre')
    text1.insert('end', "Elle permet de naviguer dans l'application en choisissant entre \"Atelier\", \"Exercice\" ou \"Aide\". Sous les deux premiers onglets, des boutons permettent d'effectuer les actions associées.\n\n", 'normal')
    
    text1.insert('end', "L'onglet \"Atelier\"\n\n", 'titre')
    text1.insert('end', "Dans cette fenêtre, les boutons not, and, or, xor et node permettent d'ajouter un composant dans le circuit du robot soit respectivement : ", 'normal')
    text1.window_create('end', window=iconnot)
    text1.insert('end', " une porte NON, ", 'normal')
    text1.window_create('end', window=iconand)
    text1.insert('end', " une porte ET, ", 'normal')
    text1.window_create('end', window=iconor)
    text1.insert('end', " une porte OU, ", 'normal')
    text1.window_create('end', window=iconxor)
    text1.insert('end', " une porte OU exclusif, et ", 'normal')
    text1.window_create('end', window=iconnode)
    text1.insert('end', " un doubleur de signal (en ajoutant un noeud sur un fil)\n\nLe bouton droit de la souris permet d'orienter chaque composant suivant les 4 directions cardinales (nord, sud, est, ouest). Le bouton ", 'normal')
    text1.insert('end', " Souder ", 'touche')
    text1.insert('end', " permet de passer en mode \"fer à souder\" (ou fil), ce qui permet de souder les composants entre eux, avec les radars ", 'normal')
    text1.window_create('end', window=iconrad)
    text1.insert('end', " et les moteurs ", 'normal')
    text1.window_create('end', window=iconmot)
    text1.insert('end', ", ou de supprimer un fil mal placé. Le bouton ", 'normal')
    text1.insert('end', " Sauver ", 'touche')
    text1.insert('end', " permet de sauvegarder le montage dans un fichier \"robot\" d'extension \".rob\". Les radars peuvent être activés ", 'normal')
    text1.window_create('end', window=iconrad2)  # on ne peut utiliser une window qu'a un seul endroit (?)
    text1.insert('end', " pour tester le circuit.\n\n", 'normal')
    text1.insert('end', "", 'normal')
    
    text1.insert('end', "L'onglet \"Exercice\"\n\n", 'titre')
    text1.insert('end', "Dans cette fenêtre, le bouton ", 'normal')
    text1.insert('end', " Niveau ", 'touche')
    text1.insert('end', " (pour niveau d'exercice) permet de charger un exercice, un fichier de suffixe \".niv\".\n\nUne fois l'exercice chargé, trois types d'objets sont représentés : ", 'normal')
    text1.window_create('end', window=icondep)
    text1.insert('end', " symbolise l'emplacement de départ du robot, ", 'normal')
    text1.window_create('end', window=iconarr)
    text1.insert('end', " symbolise le but à atteindre et ", 'normal')
    text1.window_create('end', window=iconmur)
    text1.insert('end', " symbolise un mur infranchissable\n\nUne fois le robot construit et sauvegardé depuis l'atelier, le bouton ", 'normal')
    text1.insert('end', " Robot ", 'touche')
    text1.insert('end', " permet de l'utiliser dans l'exercice en chargeant un fichier de suffixe \".rob\". Le bouton ", 'normal')
    text1.insert('end', " Go ", 'touche')
    text1.insert('end', " permet alors de lancer la simulation, le bouton ", 'normal')
    text1.insert('end', " Pause ", 'touche')
    text1.insert('end', " de suspendre cette dernière et le bouton ", 'normal')
    text1.insert('end', " Stop ", 'touche')
    text1.insert('end', " de l'arrêter.\n\n\n", 'normal')
    # "De petites flammes simulent les jets de gaz et permettent de visualiser le fonctionnement du robot.\n\n\n", 'normal')
    text1.insert('end', "                                                                         Auteur : C. Nguyen (2021)", 'normal')

    text1.configure(state='disabled')


# ----------------------------------------------------------------------
# BINDINGS

def creer_not():
    comp = Not()
    # dcomp[comp.obj] = comp
    comp.draw()

def creer_and():
    comp = And()
    # dcomp[comp.obj] = comp
    comp.draw()

def creer_or():
    comp = Or()
    comp.draw()

def creer_xor():
    comp = Xor()
    comp.draw()

def creer_node():
    global noeud_flag
    # global noeud_ref
    # noeud_ref = Node()
    # /!\ creation et affichage differe au moment de cliquer sur un fil (b1_agir_fil)
    noeud_flag = True

def creer_soudure():
    # impossible d'utiliser correctement les methodes de ttk et
    # de toute facon le flag est necessaire
    global soudure_flag

    style = ttk.Style()
    # print(bsoud.state(), bsoud.cget('state'), type(bsoud.cget('state'))
    # if bsoud.cget('state') == NORMAL:  # <class '_tkinter.Tcl_Obj'>
    # print('AVANT', bsoud.instate(['pressed']))
    # if not bsoud.instate(['pressed']):
    if not soudure_flag:
        soudure_flag = True
        # ret = bsoud.state(['pressed'])  # /!\ list [] obligatoire
        # print('retour de state()', ret)
        # print('APRES', bsoud.instate(['pressed']), bsoud.cget('state'))
        style.configure("bsoud.TButton", relief=SUNKEN, background="orange")
        canv1.configure(cursor='pencil')  # cursor='target'
        # desactivation des boutons des composants
        for txt in ('1NOT', '2AND', '3OR', '4XOR', '5node'):
            dbout1[txt].configure(state='disabled')
    else:
        soudure_flag = False
        # bsoud.state(['!pressed'])
        style.configure("bsoud.TButton", relief=RAISED, background="grey90")
        canv1.configure(cursor='arrow')
        # activation des boutons des composants
        for txt in ('1NOT', '2AND', '3OR', '4XOR', '5node'):
            dbout1[txt].configure(state='normal')
    # print('QUIT', bsoud.instate(['pressed']))

def b1_pos_curseur(event):
    global curX, curY
    
    curX, curY = event.x, event.y

def b1_deplacement(event):
    """
    deplacement des composants et des fils
    a condition de ne pas etre en mode soudure
    """
    global curX, curY  # ancienne position du curseur souris
    
    if soudure_flag:
        return
    obj = get_obj()
    # deplacement relatif de toutes les parties du dessin
    dX, dY = event.x-curX, event.y-curY
    canv1.move(obj, dX, dY)
    # deplacement de(s) fil(s) rattaché(s) s'il y a lieu
    dcomp[obj].deplacer_fils()
    # maj de la position courante
    # dcomp[obj].set_origine(dX, dY)
    curX, curY = event.x, event.y
    dcomp[obj].set_origine(curX, curY)

def b1_soudure_debut(event):
    """
    creation d'un nouveau fil de soudure a condition d'etre en mode soudure
    le binding ne s'active que sur un objet graphique de tag 'in' ou 'out'
    """
    global id_fil
    # pas en mode soudure
    if not soudure_flag:
        return
    tid = canv1.find_withtag('current')  # id de la patte (tuple 1 elem !)
    id = tid[0]  # suppression du type tuple, on veut un entier
    # /!\ il ne peut y avoir qu'un fil par patte
    obj = get_obj()  # obj correspondant a l'ID current
    if dcomp[obj].get_fil(id):
        showerror("Erreur", "Cette patte a déjà un fil")
        return
    ltags = canv1.gettags(id)
    es = 'in' if 'in' in ltags else 'out'
    # /!\ il ne peut y avoir qu'un fil par patte IN
    # if es == 'in':
    #     obj = get_obj()  # obj correspondant a l'ID current
    #     if dcomp[obj].get_fil(id):
    #         showerror("Erreur", "La patte d'entrée a déjà un fil")
    #         return
    # print(es, dcomp[get_obj()].get_out())  # out bit (get_obj global)
    x, y = canv1.coords(id)[:2]
    id_fil = canv1.create_line(x, y, event.x, event.y, fill='orange', tags="fil "+es+str(id))  # inxx ou outxx est le tag de patte d'ou part le fil

def b1_strapping(event):
    """ redessine le fil pendant l'etirement de celui-ci """
    # pas en mode soudure ou pas de fil courant
    if not soudure_flag or not id_fil:
        return
    # conservation de la patte d'ou part le fil par selection du bouton 1
    id = canv1.find_withtag('current')
    ltags = canv1.gettags(id)
    # if 'node' in ltags:
    #     print('[b1_strapping] ltags', ltags)
    # on n'agit que s'il s'agit d'une patte (in ou out)
    if 'in' in ltags or 'out' in ltags:
        # A FAIRE ? si un composant n'est pas deja relie a cette patte
        deformer_fil(id_fil, id, event.x, event.y, False)

def b1_soudure_fin(event):
    """
    trace definitif du nouveau fil de soudure a condition d'etre sur une
    patte et d'etre en mode soudure
    """
    global id_fil  #, noeud_flag
    
    # pas en mode soudure ou pas de fil courant
    if not soudure_flag or not id_fil:
        return
    
    # la patte de depart
    tid = canv1.find_withtag('current')  # id de la patte (tuple 1 elem !)
    id1 = tid[0]  # suppression du type tuple, on veut un entier
    ltags = canv1.gettags(id1)
    es1 = 'in' if 'in' in ltags else 'out'  # E/S 1
    
    # l'objet d'arrivee
    lid = canv1.find_overlapping(event.x-5, event.y-5, event.x+5, event.y+5)
    es2 = None  # E/S 2
    # un objet graphique a t'il bien le tag in ou out (patte) ?
    for id2 in lid:
        ltags = canv1.gettags(id2)
        if 'in' in ltags and es1 == 'out':
            es2 = 'in'
            break
        elif 'out' in ltags and es1 == 'in':
            es2 = 'out'
            break
    
    # patte d'arrivee non conforme
    if not es2:
        showerror("Erreur", "Problème lors de la soudure")
        canv1.delete(id_fil)  # si on ne soude pas, on detruit le fil
        id_fil = None
        return
    else:
        obj = get_obj(id2)
        if dcomp[obj].get_fil(id2):
            showerror("Erreur", "La patte a déjà un fil")
            canv1.delete(id_fil)  # si on ne soude pas, on detruit le fil
            id_fil = None
            return
    
    # mise en place definitive de la soudure sur la patte d'arrivee
    coordp = canv1.coords(id2)  # coordonnees de la patte
    # pour conserver la forme en L i.e l'angle droit
    deformer_fil(id_fil, id1, coordp[0], coordp[1], False)
    
    # fil : ajout du tag correspondant a la 2ieme patte
    canv1.addtag_withtag(es2+str(id2), id_fil)
    # mise a jour des composants concernes (memorisation de l'id fil)
    canv1.addtag_withtag('fil'+str(id_fil), id1)  # patte depart
    canv1.addtag_withtag('fil'+str(id_fil), id2)  # patte arrivee
    
    # mise a jour des valeurs de bit et feedback couleur
    if es2 == 'in':
        # quelle est la valeur de la patte out ?
        obj1 = get_obj(id1)  # id => ref interne
        bit = dcomp[obj1].get_out()
        # maj patte in
        maj_patte_in(id2, bit)
    else:
        # la patte out est le 2eme objet
        bit = dcomp[get_obj(id2)].get_out()
        maj_patte_in(id1, bit)
    # reset id_fil (global)
    id_fil = None
    # reset noeud_flag
    # noeud_flag = False

def b1_agir_fil(event):
    """
    - destruction d'un fil en mode soudure et maj des composants
    OU
    - ajout d'un noeud sur un fil
    """
    global noeud_ref, noeud_flag
    
    id = canv1.find_withtag('current')  # id d'un fil (tuple 1 elem !)
    
    # mode AJOUT d'un noeud
    if noeud_flag:
        # creation d'un disque sur le fil courant
        noeud_ref = Node()
        x, y = event.x, event.y
        noeud_ref.draw(id, x, y)
        noeud_flag = False
        return
    
    # pas en mode soudure
    if not soudure_flag:
        return
    
    # mode DESTRUCTION d'un fil
    # recuperation des ID des pattes reliees par le fil
    lidi, ido = fil_get_in_out(id)
    # recuperation des composants auxquels elles appartiennent
    objout = get_obj(ido)
    # print('type out', dcomp[objout].get_type())
    dcomp[objout].del_fil(ido)  # destruction ID du fil dans patte OUT
    # pour tous les IN (1 patte et N nodes)
    for idi in lidi:
        objin = get_obj(idi)
        # print('type in', dcomp[objin].get_type())
        dcomp[objin].del_fil(idi)  # del ID du fil dans tags patte IN
        # mise a jour recursive des composants
        maj_patte_in(idi, 0)
        # destruction des noeuds et de leur fil associe
        if dcomp[objin].get_type() == 'node':
            dcomp[objin].del_it()
    # destruction effective du fil selectionne
    canv1.delete(id)
    
def b3_rotation90(event):
    """ rotation successive de 90 degres """
    obj = get_obj()
    dcomp[obj].rotation90()  # toujours pas de rotation dans tkinter

def b1_test_circuit(event):
    """ gadget pour activer un radar en mode atelier """
    # ne rien faire en mode soudure
    if soudure_flag:
        return
    
    obj = get_obj()
    dcomp[obj].test_circuit()  # pas de verif : binding d'un radar

def b1_corbeille(event):
    """"""
    lid = canv1.find_overlapping(event.x-5, event.y-5, event.x+5, event.y+5)
    for id in lid:
        if 'trash' in canv1.gettags(id):
            idcomp = canv1.find_withtag('current')  # le composant a detruire
            obj = get_obj(idcomp)  # l'objet associe
            # s'il y a des pattes instanciees
            if dcomp[obj].p:
                fil_present = False
                for patte in dcomp[obj].p:
                    if dcomp[obj].get_fil(patte) is not None:
                        fil_present = True
                if not fil_present:
                    # print('le composant', dcomp[obj].get_type(), 'est détruit')
                    # suppression graphique
                    lcomps = canv1.find_withtag(obj)
                    for c in lcomps:
                        canv1.delete(c)
                    # suppression dans le dico
                    dcomp.pop(obj)
                else:
                    showerror("Corbeille", 'le composant '+dcomp[obj].get_type()+' a un fil')

def selec_feedback(event):
    """ feedback de selection d'un fil ou d'une patte """
    id = canv1.find_withtag('current')
    ltags = canv1.gettags(id)
    if 'fil' in ltags:
        canv1.itemconfigure(id, width=3)
    else:
        canv1.itemconfigure(id, width=5)

def deselec_feedback(event):
    """ retour a la normal """
    id = canv1.find_withtag('current')
    ltags = canv1.gettags(id)
    if 'fil' in ltags:
        canv1.itemconfigure(id, width=1)
    else:
        canv1.itemconfigure(id, width=3)

def root_config(event):
    """
    binding de (re)configuration de la fenetre principale, cela permet :
      - de redefinir la taille des canvas
      - par voie de consequence, la taille des objets graphiques
    dans le cas d'un changement alors que des objets sont affiches,
    il faut les detruire et les afficher avec une nouvelle taille.
    """
    global LA, HA, rootl, rooth, atel
    
    l, h = root.winfo_width(), root.winfo_height()
    # la difference de hauteur entre root et canvas est tjrs de 50
    if rootl != l or rooth != h:
    # if l != LA or h != HA+50:
        # tabctrl.config(width=l, height=h)
        # dxy = min(l/rootl, h/rooth)
        LA, HA = l, h-50
        # atelier
        canv1.configure(width=LA, height=HA)
        cpt = Composant.get_cpt()
        lfil = canv1.find_withtag('fil')
        # mise a l'echelle si pas de composants ni de fils
        if atel and cpt < 11 and not lfil:
            # del(atel)
            # atel = Atelier()
            # atel.draw()
            nouvel_atelier()
        # exercice
        canv2.configure(width=l, height=h-50)
        rootl, rooth = l, h


# ----------------------------------------------------------------------
# TESTS

def anim():
    bitmap = 'gray50' if sens == 1 else 'gray25'
    canv2.itemconfig(idessai, stipple=bitmap)

def idle_func():
    if rob:
        rob.anim()
    canv2.update_idletasks()
    if not pause:
        root.after(100, idle_func)

def clavier(event):
    if event.char == 'd':
        # print(rob.is_wall('e'))
        rob.move(rob.i+1, rob.j)
    elif event.char == 'q':
        rob.move(rob.i-1, rob.j)
    elif event.char == 'z':
        rob.move(rob.i, rob.j-1)
    elif event.char == 's':
        rob.move(rob.i, rob.j+1)

# ----------------------------------------------------------------------
# MAIN

root=Tk()
# root.geometry(str(LA)+'x'+str(HA+50))
root.title("pyrobot - atelier de logique combinatoire")
# TEST : les canvas ne prennent pas le clavier
# root.bind("<KeyPress>", clavier)

tabctrl = ttk.Notebook(root, width=LA, height=HA)

tab1 = ttk.Frame(tabctrl)
tabctrl.add(tab1, text='Atelier', sticky='n')  # Atelier
f11 = Frame(tab1)
# dico avec cles prefixees d'un chiffre pour ordre d'affichage
dcom1 = {'1NOT':creer_not, '2AND':creer_and, '3OR':creer_or, '4XOR':creer_xor, '5node':creer_node}
# ID des boutons
dbout1 = {'1NOT':None, '2AND':None, '3OR':None, '4XOR':None, '5node':None}
for txt in sorted(dcom1.keys()):
    dbout1[txt] = ttk.Button(f11, text=txt[1:], command=dcom1[txt])
    dbout1[txt].pack(side=LEFT)
bnew = ttk.Button(f11, text='Nouveau', command=nouvel_atelier)
bnew.pack(side=RIGHT)
bsave = ttk.Button(f11, text='Sauver', command=sauver_robot)
bsave.pack(side=RIGHT)
style1 = ttk.Style()
style1.configure("bsoudon.TButton", state='pressed', background="red")
style2 = ttk.Style()
style2.configure("bsoudoff.TButton", state='normal')
bsoud = ttk.Button(f11, text='Souder', style="bsoud.TButton", command=creer_soudure)
bsoud.pack(side=RIGHT)
f11.pack(expand=True, fill=X)
canv1 = Canvas(tab1, width=LA, height=HA, bg='grey20')
canv1.pack()
canv1.tag_bind('gate', '<1>', b1_pos_curseur)
canv1.tag_bind('gate', '<B1-Motion>', b1_deplacement)
canv1.tag_bind('gate', '<3>', b3_rotation90)
canv1.tag_bind('gate', '<ButtonRelease-1>', b1_corbeille)
canv1.tag_bind('in', '<1>', b1_soudure_debut)
canv1.tag_bind('in', '<B1-Motion>', b1_strapping)
canv1.tag_bind('in', '<ButtonRelease-1>', b1_soudure_fin)
canv1.tag_bind('out', '<1>', b1_soudure_debut)
canv1.tag_bind('out', '<B1-Motion>', b1_strapping)
canv1.tag_bind('out', '<ButtonRelease-1>', b1_soudure_fin)
canv1.tag_bind('fil', '<1>', b1_agir_fil)
# feedbacks
canv1.tag_bind('in', '<Enter>', selec_feedback)
canv1.tag_bind('in', '<Leave>', deselec_feedback)
canv1.tag_bind('out', '<Enter>', selec_feedback)
canv1.tag_bind('out', '<Leave>', deselec_feedback)
canv1.tag_bind('fil', '<Enter>', selec_feedback)
canv1.tag_bind('fil', '<Leave>', deselec_feedback)
# retour visuel du circuit en manipulant les radars
canv1.tag_bind('radar', '<1>', b1_test_circuit)

style2 = ttk.Style()
# style2.configure("TFrame", background="red")
# print(style2.layout("TFrame"))
# tab2 = ttk.Frame(tabctrl, style='TFrame')
tab2 = ttk.Frame(tabctrl)
tabctrl.add(tab2, text='Exercice', sticky='n')
# tab2.pack(fill=X, expand=1)
f21 = Frame(tab2)
# dico des commandes
dcom2 = {'1Niveau':charger_niveau, '2Robot':charger_robot, '3Stop':lambda:simulation('stop'), '4Pause':lambda:simulation('pause'), '5Go':lambda:simulation('go')}
# ID des boutons
dbout2 = {'1Niveau':None, '2Robot':None, '3Stop':None, '4Pause':None, '5Go':None}
for txt in sorted(dcom2.keys()):
    dbout2[txt] = ttk.Button(f21, text=txt[1:], command=dcom2[txt])
    if txt[0] in ('1', '2'):
        dbout2[txt].pack(side=LEFT)
    else:
        dbout2[txt].pack(side=RIGHT)
        dbout2[txt].configure(state='disabled')
dbout2['2Robot'].configure(state='disabled')
f21.pack(expand=True, fill=X)
canv2 = Canvas(tab2, width=LA, height=HA, bg='black')
# canv2 = Canvas(tab2, bg='black')
canv2.pack(expand=True, fill=BOTH)
# tab2.pack(expand=True, fill="both")

# tab3 = ttk.Frame(tabctrl)
# tabctrl.add(tab3, text='Intégration', sticky='n')
# f31 = Frame(tab3)
# f31.pack(expand=True, fill=X)
# canv3 = Canvas(tab3, width=LA, height=HA, bg='grey20')
# canv3.pack()
# canv3.create_text(LA/2, HA/2, text="Coming soon", anchor='center', font=('Helvetica', -80, 'bold'), fill='grey95', stipple='gray25')

tab4 = ttk.Frame(tabctrl)
tabctrl.add(tab4, text='Aide', sticky='n')
f41 = Frame(tab4)
f41.pack(expand=True, fill=X)
text1 = Text(tab4, width=110, height=43, bg='grey20')  # dim : nb car
text1.pack(side=TOP, pady=10)
text1.tag_config('titre', foreground='red')
text1.tag_config('normal', foreground='white')
text1.tag_config('touche', background='white', foreground='black')
afficher_aide()

tabctrl.pack(expand=True, fill="both")


root.wait_visibility()
# une fois la root affichee, on peut prendre en compte sa taille
# pour adapter la taille des canvas et donc des objets affiches
root.bind("<Configure>", root_config)

# case de taille 100 x 100 px
# canv.create_rectangle(400-50, 300-50, 400+50, 300+50, outline='red', width=2)
# animation
# idessai = canv.create_rectangle(10, 10, 60, 60, fill='red', stipple='gray50')

# 1er atelier au lancement
atel = Atelier()
atel.draw()
# centre geometrique
# canv1.create_oval(LA/2-3, HA/2-3, LA/2+3, HA/2+3, fill='green')

# idle_func()

root.mainloop()
exit(0)
