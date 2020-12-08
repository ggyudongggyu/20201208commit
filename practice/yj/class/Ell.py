from Figu import Figure
class Ellipse(Figure):
    def __init__(self, long_radius , short_radius):
        self.long_radius = long_radius
        self.short_radius = short_radius
        self.calculated()
    def calculated(self):
        self.area = 3.14 * self.short_radius * self.long_radius
