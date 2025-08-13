'''
Let’s say we have a Graphic object, and both individual graphics (like a circle or square) and compositions of
graphics (like a group of circles or squares) should be treated uniformly
'''
from abc import ABC ,abstractmethod
#Component
class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass
#Leaf
class Circle(Graphic):
    def draw(self):
        print("Drawing a Circle")

class Square(Graphic):
    def draw(self):
        print("Drawing a Square")
        
#Composite
class Group(Graphic):
    def __init__(self):
        self.graphics = []
    def add(self,graphic:Graphic):
        self.graphics.append(graphic)
    def remove(self,graphic:Graphic):
        self.graphics.remove(graphic)
    def  draw(self):
        print("Drawing Group of Graphics:")
        for graphic in self.graphics:
            graphic.draw()

# Client code
circle = Circle()
square = Square()
group = Group()
group.add(circle)
group.add(square)
# Drawing individual and composite objects
circle.draw()
square.draw()
group.draw()


'''
Output:
Drawing a Circle
Drawing a Square
Drawing Group of Graphics:
Drawing a Circle
Drawing a Square
'''
        
