def main():

    password = get_password()


    while len(password)<7:
        print("too short")
        password = input("enter pass again")

    print_asterisks(password)


def print_asterisks(password):
    for i in range(0, len(password)):
        print("*", end='')


def get_password():
    password = input("Enter password")
    return password


main()