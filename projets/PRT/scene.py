from __future__ import annotations
from camera import Camera
from objet import Objet
from point import Point
from lumiere import Lumiere

class Scene:
    """ Une scène est définie par une caméra, les lumières présentes et les
    objets qui la composent."""

    def __init__(self, camera : Camera, objets : list[Objet], lumieres : list[Lumiere]): 
        self.camera = camera
        self.objets = objets
        self.lumieres = lumieres
        