from Figu import Figure
class Polygon(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.calculated()
