"""
def main():


    score = float(input("Enter score: "))
    if score < 0 or 100<score:
        print("Invalid score")

    elif score >= 90:
        print("Excellent")
    elif score >= 50:
            print("Passable")
    else:
        print("Bad")

main()"""



def random_number():
    import random
    for x in range(1):
        rnum = print(random.randint(1,101))
    return rnum

number= random_number()

def result(score):

    if score < 0 or 100<score:
        results = "Invalid score"
    elif score >= 90:
        results = ("Excellent")
    elif score >= 50:
        results = ("Passable")
    else:
        results = ("Bad")

    return results


print(result(number))