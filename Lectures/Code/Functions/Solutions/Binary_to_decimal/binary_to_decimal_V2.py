def check_digits(digits):
    for digit in digits:
        if digit not in '01':
            return False
    return True


def get_binary_number(prompt):
    binary_number = input(f"{prompt}: ")

    while not check_digits(binary_number):
        print(binary_number, "is not a binary number!\nTry again!")
        binary_number = input(f"{prompt}: ")

    return binary_number


def binary_to_decimal(binary_number):
    decimal_number = 0

    for i, digit in enumerate(binary_number):
        decimal_number += int(digit) * 2 ** (len(binary_number) - 1 - i)

    return decimal_number


def conversion():
    binary_number = get_binary_number("Inserisci digits")

    print(f"Binary: {binary_number}")

    print(f"Decimal: {binary_to_decimal(binary_number)}")


def main():
    again = True
    while again:
        conversion()

        choice = ""
        while choice != 'Y' and choice != 'N':
            choice = input("Altra conversione? [Y or N]: ")

        if choice == 'N':
            again = False

    print("BYE!")


if __name__ == "__main__":
    main()
