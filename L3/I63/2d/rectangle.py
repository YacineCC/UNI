import point as poi

class Rectangle:
    """ Un rectangle est défini par deux points"""
    def __init__(self, xy1 : poi.Point, xy2 : poi.Point):
        self.__p1 = xy1
        self.__p2 = xy2
        self.__hauteur = self.__p2.y - self.__p1.y
        self.__largeur = self.__p2.x - self.__p1.x

    @property
    def p1(self):
        return self.__p1
    @p1.setter
    def p1(self, val):
        self.__p1 = val


    @property
    def p2(self):
        return self.__p2
    @p2.setter
    def p2(self, val):
        self.__p2 = val

    @property
    def hauteur(self):
        return self.__hauteur
    @hauteur.setter
    def hauteur(self, val):
        self.__hauteur = val

    @property
    def largeur(self):
        return self.__largeur
    @largeur.setter
    def largeur(self, val):
        self.__largeur = val

