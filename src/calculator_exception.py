import math


def calc():
    print("Calculator")

    should_continue = True
    numbers = {"num1": None, "num2": None}

    while should_continue:

        numbers["num1"] = get_number()
        numbers["num2"] = get_number()

        while True:

            print("(1) +")
            print("(2) -")

            print("(3) *")
            print("(4) /")
            print("(5)sin(number1/number2)")
            print("(6)cos(number1/number2)")
            print("(7) Change numbers")
            print("(8) Quit")
            print("Current numbers:", numbers["num1"], numbers["num2"])

            option = int(input("Please select something (1-6):"))

            if option == 8:
                should_continue = False
                break

            if option == 7:
                break

            if 7 > option > 0:
                result = perform(option, numbers["num1"], numbers["num2"])
                print("The result is:", result)

    print("Thank you!")


def get_number():
    try:
        number = int(input("Give a number: "))
        return number
    except (TypeError, ValueError):
        print('This input is invalid.')
        return get_number()


def perform(option, num1, num2):
    if option == 1:
        return num1 + num2
    if option == 2:
        return num1 - num2
    if option == 3:
        return num1 * num2
    if option == 4:
        return num1 / num2
    if option == 5:
        return math.sin(num1 / num2)
    if option == 6:
        return math.cos(num1 / num2)


calc()
