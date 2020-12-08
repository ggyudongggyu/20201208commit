from Figu import Figure
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self.calculated()
    def calculated(self):
        self.area = 3.14 * self.radius ** 2
