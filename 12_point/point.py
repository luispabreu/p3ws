import math

class Point:
    """A simple point class which represents the x an y position of apoint in the Cartesian plane"""

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        pass

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __repr__(self):
        return 'Point' + self.__str__()

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        pass

    def distance_from(self, pt):
        x1 = self.x
        y1 = self.y
        x2 = pt.x
        y2 = pt.y
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    pass

def main():
    point = Point()
    print(point)
    point.move(2,-1)
    print(point)
    print(point.distance_from(Point(40,3)))    
    return 0

if __name__== "__main__":
    main()

    
    
    
