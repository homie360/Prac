"""This solves the type of triangle"""

def valid(sides):
    """..."""
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b 

def equilateral(sides):
    """..."""
    a, b, c = sides
    return valid(sides) and a == b == c

def isosceles(sides):
    """..."""
    a, b, c = sides
    return valid(sides) and (a == b or a == c or b == c)

def scalene(sides):
    """..."""
    a, b, c = sides
    return valid(sides) and (a != b and b != c and a != c)
