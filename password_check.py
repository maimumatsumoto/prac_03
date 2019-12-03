password = input("Enter password")



while len(password)<7:
    print("too short")
    password = input("enter pass again")

for i in range(0,len(password)):
    print("*", end='')