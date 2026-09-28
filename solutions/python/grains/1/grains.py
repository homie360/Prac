""" Functions for calculating the number of grains on a chessboard"""

def square(number):
    """ 
    calculates the number of grains on a given sqaure.
    Parameters:
        number(int): the square index on the chessboard between 1 - 64
    Returns(int):
        the number of grains present on that particular square on the chessboard
    Raises(str):
        A ValueError message for numbers outside from 1 to 64
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    exponent = number - 1
    return 2 ** exponent
def total():
    """
    calculates the total number of grains on the chessboard
    Returns:
        total_sum(int): the total number of grains existing on the whole chessboard.  
    """
    total_sum = 0
    for number in range(1, 65):
        total_sum = total_sum + square(number)
    return total_sum
