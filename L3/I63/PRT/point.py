from narray import Narray
import numpy as np
class Point(Narray):
    pass


    def distance(self, p2):
        return (((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2 + (p2.z - self.z) ** 2) ** 0.5)
if __name__ == "__main__":
    A = Point(0,0,0)
    B = Point(5,5,5)
    print(A.distance(B))
