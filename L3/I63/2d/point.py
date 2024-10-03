class Point:

    def __init__(self, px, py):
        self.__x = px
        self.__y = py
        
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y
    

    @y.setter
    def y(self, val):
        self.__y = val

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __repr__(self) -> str:
        return str(self)