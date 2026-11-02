# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if width <= 0 or height <=0:
            raise ValueError("width and height cannot be less than or equal to 0 ")
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = (self.width * 2) + (self.height *2)
        return perimeter 




    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
