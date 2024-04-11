
def encode(num):
    new_number = ""
    for digit in str(num):
        add_three = str(int(digit) + 3)
        new_number += add_three
    return new_number


