
def encode(num):
    new_number = ""
    for digit in str(num):
        add_three = (digit + 3)
        add_three += new_number
    return new_number

print(encode(123))

def decode(num):
    pass

"""
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = int(input("Please enter your password to encode: "))
            encode(password)


if __name__ == '__main__':
    main()
"""
