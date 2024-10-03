from __future__ import annotations
from camera import Camera
from objet import Objet
from point import Point
from lumiere import Lumiere


class Scene:
    """ Les informations de la scène"""

    def __init__(self, camera : Camera, objets : list[Objet], lumieres : list[Lumiere], width : int, height : int): 
        self.camera = camera
        self.objets = objets
        self.lumieres = lumieres
        self.width = width
        self.height = height