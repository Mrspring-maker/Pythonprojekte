from geoform import GeoForm
class Rechteck(GeoForm):

    def __init__(self, a,):
        GeoForm.__init__(self)
        self.a = a
    def umfang(self):
        return 4 * self.a
    def flaeche(self):
        return 2 * self.a
