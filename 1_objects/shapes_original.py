import math
# we have classes and objects because we want to bundle data and functions


''' INHERITANCE: we have parents and children of classes, where children inherit structure from the parents... 
by seperating classes from objects we can implement inheritance without changing too much  '''


class Shape:
    # init always first, bec.
    def __init__(self, name):
        self.name = name

    #
    def perimeter(self):
        # to signify that this does nothing, we raise an error
        raise NotImplementedError("perimeter missing")

    def area(self):
        # now, we pass aka nothing happens but we raise an error
        raise NotImplementedError("area missing")

    def density(self, weight):
        return weight / self.area()


# this is a child of the shape class

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)  # parent class structure gets inherited
        self.side = side

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2

    def density(self, weight):
        return weight/self.area()


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return (self.radius ** 2) * math.pi

    def density(self, weight):
        return weight/self.area()


examples = [Square("sq", 2), Circle("cr", 4)]

for thing in examples:
    n = thing.name
    p = thing.perimeter()
    a = thing.area()
    print(f"{n} has perimeter {p:.2f} and area {a:.2f}.")
