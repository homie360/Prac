"""Determine whether a number is an Armstrong number."""

def is_armstrong_number(number):
    """Check whether a number is an Armstrong number.

    An Armstrong number equals the sum of its own digits, each raised
    to the power of the number of digits.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    total_sum = 0
    digits_to_be_checked = str(number)
    lenght_of_digits = len(digits_to_be_checked)
    for digit in digits_to_be_checked:
        total_sum = total_sum + int(digit) ** lenght_of_digits

    return total_sum == number