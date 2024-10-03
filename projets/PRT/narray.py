from __future__ import annotations
import numpy as np

class Narray:
    """ Classe fondamentale du projet pour le calcul vectoriel, on utilise un
    numpy array pour une meilleure efficacité."""

    def __init__(self, x : int, y: int, z: int):
        self.__np_arr = np.array((x, y, z))
    
    """ Les méthodes suivantes sont des décorateurs pour accéder ou modifier le
    np array."""
    @property
    def x(self) -> int:
        return self.__np_arr[0]

    @x.setter
    def x(self, val : int):
        self.__np_arr[0] = val

    @property
    def y(self) -> int:
        return self.__np_arr[1]

    @y.setter
    def y(self, val : int):
        self.__np_arr[1] = val

    @property
    def z(self) -> int:
        return self.__np_arr[2]

    @z.setter
    def z(self, val : int):
        self.__np_arr[2] = val

    @property
    def arr(self) -> int:
        return self.__np_arr

    @arr.setter
    def arr(self, val : np.array):
        self.__np_arr = val

    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'
    
    def __repr__(self) -> str:
        return str(self)
    

