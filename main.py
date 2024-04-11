
def encode(num):
    new_number = ""
    for digit in str(num):
        add_three = str(int(digit) + 3)
        new_number += add_three
    return new_number

def decoder(new_number):
    result = ''
    for digit in str(new_number):
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result
