# Let's define a sub-function
def printer_function(word1, word2):
    print("We got parameters", word1, "and", word2)


# This is the main function
def main():
    string_1 = "10"
    string_2 = "2008"

    # Let's call the sub-function here
    printer_function(string_1, string_2)


# This code tells the interpreter the name
# of the main function which starts the program.

if __name__ == "__main__":
    main()
