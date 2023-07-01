myfile = input("Give the file name:")
try:
    content = open(myfile, "r")
    big_str = content.read()
    crt_num = int(big_str)
    res = crt_num/1000
    print("The result was")
except Exception:
        print("There seems to be no file with that name.")
else:
        print("The file contents were unsuitable.")