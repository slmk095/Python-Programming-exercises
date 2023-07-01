def calc():
    print("Calculator")

    should_continue = True

    while should_continue:

        num1 = int(input("Give the first number:"))

        num2 = int(input("Give the second number:"))

        while True:

            print("(1) +")
            print("(2) -")

            print("(3) *")
            print("(4) /")
            print("(5) Change numbers")
            print("(6) Quit")
            print("Current numbers:", num1, num2)

            option = int(input("Please select something (1-6):"))

            if option == 6:
                should_continue = False
                break

            if option == 5:
                break

            if 5 > option > 0:
                result = perform(option, num1, num2)
                print("The result is:", result)

    print("Thank you!")


def perform(option, num1, num2):
    if option == 1:
        return num1 + num2
    if option == 2:
        return num1 - num2
    if option == 3:
        return num1 * num2
    if option == 4:
        return num1 / num2


calc()
