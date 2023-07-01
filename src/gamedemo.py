import random
import sys

tie = 0
win = 0
count = 0


def makeYourChoice(user_input, computer_input):

    global tie
    global win
    global count

    if user_input == computer_input:
        print("It is a tie!")
        tie = int(tie) + 1
        count = int(count) + 1

    elif user_input == "Foot" and computer_input == "Nuke":
        print("You LOSE!")
        count = int(count) + 1

    elif user_input == "Foot" and computer_input == "Cockroach":
        print("You WIN!")
        win = int(win) + 1
        count = int(count) + 1

    elif user_input == "Nuke" and computer_input == "Foot":
        print("You WIN!")
        win = int(win) + 1
        count = int(count) + 1

    elif user_input == "Nuke" and computer_input == "Cockroach":
        print("You LOSE!")
        count = int(count) + 1

    elif user_input == "Cockroach" and computer_input == "Foot":
        print("You LOSE!")
        count = int(count) + 1

    elif user_input == "Cockroach" and computer_input == "Nuke":
        print("You WIN!")
        win = int(win) + 1
        count = int(count) + 1

    elif user_input == "Quit":
         print("You played " + str(count) + " rounds, and won " + str(win) + " rounds, playing tie in " + str(tie) + " rounds.")
         sys.exit(0)
    else:
        print("Incorrect selection.")


def main():


    while True:

        user = input("Foot, Nuke or Cockroach? (Quit ends): ")

        print("You chose:", user)

        mylist = ['Foot', 'Nuke', 'Cockroach']

        computer = random.choice(mylist)

        print("Computer chose:", computer)

        makeYourChoice(user, computer)

if __name__ == "__main__":
    main()
