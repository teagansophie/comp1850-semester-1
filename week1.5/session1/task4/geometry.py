# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

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



# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle
class Circle:
    """
    class returning the area and perimeter of a circle 
    Taking centre at 0,0
    """

    def  __init__(self, radius, centre = Point(0.0,0.0)):
        self.r = radius
        self.c = centre


    def area(self):
        """
        calculates circles area
        """
        return math.pi * self.r * self.r 
        

    def perimeter(self):
        """
        calculates circles perimeter
        """
        return 2 * math.pi * self.r


