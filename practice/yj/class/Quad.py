from Poly import Polygon
class Quadrangle(Polygon):
    lines = 4
    def calculated(self):
        self.area = self.width * self.height
