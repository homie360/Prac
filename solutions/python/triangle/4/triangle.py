"""This solves the type of triangle"""

def valid(sides):
    """..."""
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]
    return 0 < side_a <= side_b + side_c and 0 < side_b <= side_a + side_c and 0 < side_c <= side_a + side_b

def equilateral(sides):
    """..."""
    side_a, side_b, side_c = sides
    return valid(sides) and side_a == side_b == side_c

def isosceles(sides):
    """..."""
    side_a, side_b, side_c = sides
    return valid(sides) and (side_a == side_b or side_b == side_c or side_a == side_c)

def scalene(sides):
    """..."""
    side_a, side_b, side_c = sides
    return valid(sides) and not (side_a == side_b or side_b == side_c or side_a == side_c)
