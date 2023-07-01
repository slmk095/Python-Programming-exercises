def tester(givenstring="Too short"):
    return givenstring


def main():

    prtext = True
    while prtext:
        value = input("Write something (quit ends):")
        result = tester(value)
        if result != "quit":

            if len(result) < 10:
                print("Too short")

            elif len(result) > 10:
                print(result)
                test ="X"
                if test in result:
                        print("X spotted!")

        else:
            quit()
            prtext = False


if __name__ == "__main__":
    main()