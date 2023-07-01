choice = True
mylist_sp = []
while choice:
    option = input("Would you like to \n (1)Add or \n (2)Remove items or \n (3)Quit?:")
    # print(option)
    if option == "1":
        add_text = input("What will be added?:\n")
        mylist_sp.append(add_text)
        # print(mylist_sp)
    elif option == "2":
        print("There are", len(mylist_sp), "items in the list.")
        num = int(input("Which item is deleted?:"))
        if num<len(mylist_sp):
            mylist_sp.pop(num)
        else:
            print("Incorrect selection.")

    elif option == "3":
        print("The following items remain in the list:")
        for x in mylist_sp:
            print(x)
        choice = False
    else:
        print("Incorrect selection.")
        choice = True
