
def main():
    print_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            cel_to_fahr()
        elif choice == "F":
            fahr_to_cel()
        else:
            print("Invalid option")
        print_menu()
        choice = input(">>> ").upper()
    print("Thank you.")


def print_menu():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)



def fahr_to_cel():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))


def cel_to_fahr():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))



main()