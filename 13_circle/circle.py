import math

from point import Point


class Circle:
    """This is a class of circles"""

    def __init__(self, c=None, r=1):
        if (c is None):
            self.c = Point(0,0)
        else:
            self.c = c
        assert r >= 0
        self.r = r
        pass

    def __str__(self):
        return '((' + str(self.c.x) + ', ' + str(self.c.y) + '), ' + str(self.r) + ')'

    def __repr__(self):
        return 'Circle' + self.__str__()

    def move(self, dx, dy):
        self.c.move(dx, dy)

    def intersection_area(self, other_circle):
        distance = self.c.distance_from(other_circle.c)
        if distance >= (self.r + other_circle.r):
            return 0
        if distance <= abs(self.r - other_circle.r):
            if self.r >= other_circle.r:
                return math.pi * (other_circle.r**2)
            else:
                return math.pi * (self.r**2)
            pass
        else:
            d1 = (self.r**2 - other_circle.r**2 + distance**2) / (2 * distance)
            d2 = math.sqrt(self.r**2 - d1**2)
            a = self.r**2 + math.asin(d2 / self.r)
            b = other_circle.r**2 * math.asin(d2 / other_circle.r)
            c = d1 * math.sqrt(self.r**2 - d2**2)
            d = d2 * math.sqrt(other_circle.r**2 - d2**2)
            return a + b - c - d
        pass
    
        

    
    
