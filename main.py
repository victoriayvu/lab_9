
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

def start():
    while True:
        menu()
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            num = int(input("Please enter your password to encode: "))
            encoded = encode(num)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {num}.")
        elif option == 3:
            break
def menu():
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    return


if __name__ == "__main__":
    start()