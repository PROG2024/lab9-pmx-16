"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest

class CircleTest(unittest.TestCase):
    
    def setUp(self):
        self.circle1 = Circle(2)
        self.circle2 = Circle(3)
        self.circle3 = Circle(5.5)
        self.circle4 = Circle(3.14)

    def test_two_circle_positive_radii(self):
        added_circle = self.circle2.add_area(self.circle1)
        added_circle2 = self.circle3.add_area(self.circle4)
        added_circle3 = self.circle4.add_area(self.circle1)
        added_circle4 = self.circle2.add_area(self.circle4)
        self.assertAlmostEqual(added_circle.get_area(), self.circle2.get_area() + self.circle1.get_area())
        self.assertAlmostEqual(added_circle2.get_area(), self.circle3.get_area() + self.circle4.get_area())
        self.assertAlmostEqual(added_circle3.get_area(), self.circle1.get_area() + self.circle4.get_area())
        self.assertAlmostEqual(added_circle4.get_area(), self.circle4.get_area() + self.circle2.get_area())
            
    def test_one_circle_has_zero_radius(self):
        zero_circle = Circle(0)
        added_circle = zero_circle.add_area(self.circle1)
        added_circle2 = self.circle3.add_area(zero_circle)
        self.assertAlmostEqual(added_circle.get_area(), self.circle1.get_area())
        self.assertAlmostEqual(added_circle2.get_area(), self.circle3.get_area())


    def test_radius_is_neg_raise_exception(self):
        with self.assertRaises(Exception):
            circle_neg = Circle(-3)
            circle_neg2 = Circle(-5.44)
            circle_neg3 = Circle(-10.00)

if __name__ == "__main__":
    unittest.main()
