def tester(givenstring="Too short"):
    if givenstring == "quit":
        quit()
    else:
        if len(givenstring) > 10:
            return 1
        else:
            return 0

def main():
    defdemo = True
    while defdemo:
        value = input("Write something (quit ends):")
        result = tester(value)
        if result != "quit":

            if result == True:

                print(value)
            elif result == False:
                print("Too short")

        else:
            quit()
            defdemo = False


if __name__ == "__main__":
    main()