# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

import pytest

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance_to(p2) == 5.0

    
    # complete the implementation for
    # testing distance_to()

def test__circle_constructor():
        c = Circle(5.0)
        assert c.radius == 5.0
        assert c.centre.x == 0.0
        assert c.centre.y == 0.0

        c2 = Circle(4.0, Point(1.0,2.0))
        assert c2.radius == 4.0
        assert c2.centre.x == 1.0
        assert c2.centre.y == 2.0

    


def test_area():
     circle = Circle(5)
     assert circle.area() == pytest.approx(78.53981633974483)

def test_perimeter():
     circle = Circle(2)
     assert circle.perimeter() == pytest.approx(12.566370614359172)

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates
