def delist(mylist):
    string = ""
    for i in range(0, len(mylist)):
            string = string + "€$€" + str(mylist[i])
    return string
