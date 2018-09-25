class Shape:
    def __init__(self):
        pass

    @staticmethod
    def printType():
        print("Shape")

class Rectangle(Shape):
        def __init__(self):
            super().__init__()
            self.length=0
            self.width=0
        def draw(self):
            print("draw ractangle")

class Trainagle(Shape):
    def __init__(self):
        super().__init__()
        self.a = 0
        self.b = 0
        self.c = 0

    def draw(self):
        print("Draw Trainagle")

r = Rectangle()
r.draw()
t=Trainagle()
t.draw()