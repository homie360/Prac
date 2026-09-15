def is_armstrong_number(number):
    total_sum = 0
    digits_to_be_checked = str(number)
    lenght_of_digits = len(digits_to_be_checked)
    for digit in digits_to_be_checked:
        total_sum = total_sum + int(digit) ** lenght_of_digits

    return total_sum == number