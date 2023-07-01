import time

notebookName = "notebook.txt"


def file_Change(newname):
    try:
        open(newname, "r")
    except IOError:
        modified_file = open(newname, "w")
        print("No notebook with that name detected, created one.")
    return newname


try:
    sourcefile = open(notebookName, "r")
except IOError:
     f = open(notebookName, "w")
     print("No default notebook was found, created one.")

while True:
    print("Now using file", notebookName)
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Change the notebook")
    print("(5) Quit")
    value = input("Please select one: ")
    if value == "1":
        try:
            readfile = open(notebookName, "r")
            content = readfile.read()
            print(content)
            readfile.close()
        except Exception:
            pass

    elif value == "2":
        appendtext = input("Write a new note: ")
        appendtext2 = appendtext + ":::" + time.strftime("%X %x")
        writefile = open(notebookName, "a")
        content = writefile.write(appendtext2)
        writefile.close()
    elif value == "3":
        open(notebookName, "w").close()
        print("Notes deleted.")
    elif value == "4":
        name = input("Give the name of the new file: ")
        changeName = file_Change(name)
        notebookName = changeName
    elif value == "5":
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")
