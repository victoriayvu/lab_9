def start():
    while True:
        menu()
        option = int(input("\nPlease enter an option: "))
        if option == "1":
            num = int(input("Please enter your password to encode: "))
            encode()
        elif option == "2":
            decode()
            print(f"The encoded password is {num}, and the original password is {num}.")
        elif option == "3":
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