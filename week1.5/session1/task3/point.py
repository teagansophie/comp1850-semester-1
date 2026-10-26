# Week 1.5, Session 1: Task 3
import math 

class Point:
    """
    A Point in 2D space.
    """
    def __init__(self, x_coordinate, y_coordinate):    # Add constructor here
        """
        Creates a point, given x and y coordinates
        """
        self.x = x_coordinate
        self.y = y_coordinate


    def distance(self):
        """
        Returns distance from origin to x and y 
        """
        return math.hypot(self.x, self.y)


    def distance_to(self, point):
        """
        Returns distance from this point to specified point.
        """

    
        return math.hypot(self.x - point.x, self.y - point.y)




p = Point(2.9,6.2)
q = Point(2.5, 5.3)
# print(p.x)
# print(p.y)


print(p.distance_to(q))

