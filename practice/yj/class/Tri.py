from Poly import Polygon
class Triangle(Polygon):
    lines = 3
    def calculated(self):
        self.area = self.width * self.height / 2
