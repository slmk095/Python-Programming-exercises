

filename = input("Give a file name:")

myfile = open(filename,'w')

addedtext = input("Write something:")

print("Wrote",addedtext,"to the file",filename)

myfile.write(addedtext)

myfile.close()