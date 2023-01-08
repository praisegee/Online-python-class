
import turtle


class Polygon:
    def __init__(self, size, shape, sides):
        self.size = size
        self.shape = shape
        self.sides = sides
        self.inter_angle = (self.sides - 2) * 180
        self.angle = self.inter_angle / self.sides

    def draw(self):
        t = turtle.Turtle()
        for i in range(self.sides):
            t.forward(100)
            t.left(180 - self.angle)
        turtle.done()


# s = Polygon(40, 'square', 4)
p = Polygon(70, 'pentagon', 10)
# s.draw()
p.draw()
