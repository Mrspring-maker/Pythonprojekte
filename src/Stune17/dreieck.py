import math
from geoform import GeoForm
class Dreick(GeoForm):
    def __init__(self,a , b, k1, k2):
        GeoForm.__init__(self)
        self.a = a
        self.b = b
        self.g = 180 - (a +b)
        self.k1 = k1
        self.k2 = k2



    def flaeche(self):
        return ( self.k1+self.k2*  math.sin(self.g ))
