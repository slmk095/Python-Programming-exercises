track = True

while track:
    textprint = input("Write something:")
    if textprint == "quit":
        print("Bye Bye !")
        break
        track = False
    elif (textprint != "quit"):
                        print(textprint)
                        track = True
