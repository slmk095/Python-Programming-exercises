import time
from typing import re

notebookName = "notebook.txt"


def file_change(newname):
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
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Edit a note")
    print("(4) Delete a note")
    print("(5) Save and quit")
    value = input("Please select one: ")
    if value == "1":
        try:
            rf = open(notebookName, "r")
            content = rf.read()
            print(content)
            rf.close()
        except Exception:
            pass

    elif value == "2":
        appendtext = input("Write a new note: ")
        appendtext2 = appendtext + ":::" + time.strftime("%X %x")
        writefile = open(notebookName, "a")
        content = writefile.write(appendtext2)
        writefile.close()

    elif value == "3":
        f = open(notebookName, "r")
        num = len(f.readlines())
        print("The list has", num, "notes")
        n = int(input("Which of them will be changed?:"))

        if n <= num:
            edit_file = open(notebookName, "r")
            # ep = edit_file.seek(num)
            print(edit_file.readline(n))

            new_note = input("Give the new note:")
            file = open(notebookName, "a")
            file.write(new_note)
            fr = file.read()
            print(fr)

    elif value == "4":
        name = input("Give the name of the new file: ")
        changeName = file_change(name)
        notebookName = changeName
    elif value == "5":
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")
